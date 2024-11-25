<template>
  <div id="chat-container">
    <div id="chat-messages" ref="chatMessages">
      <div
        v-for="(msg, index) in chatHistory"
        :key="index"
        :class="['message', { 'message-right': msg.sender === '나', 'message-left': msg.sender !== '나' }]"
      >
        <div class="sender">{{ msg.sender }}</div>
        <div class="content">{{ msg.content }}</div>
      </div>
    </div>
    <div id="user-input">
      <input
        @keyup.enter="sendMessage"
        type="text"
        placeholder="메시지를 입력하세요..."
        v-model.trim="message"
      />
      <button @click="sendMessage">전송</button>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick, onBeforeMount } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

// 상태 변수
const message = ref('')
const chatHistory = ref([])
const chatMessages = ref(null) // 채팅 박스를 참조하기 위한 ref

// OpenAI API 설정
const apiKey = import.meta.env.VITE_APP_GPT_API_KEY;
const apiEndpoint = 'https://api.openai.com/v1/chat/completions'


// 스크롤을 최신 메시지로 이동하는 함수
function scrollToBottom() {
  nextTick(() => {
    if (chatMessages.value) {
      chatMessages.value.scrollTop = chatMessages.value.scrollHeight;
    }
  });
}

// 메시지 추가 함수
function addMessage(sender, content) {
  chatHistory.value.push({ sender, content })
  scrollToBottom(); // 메시지 추가 후 자동 스크롤
}

// ChatGPT API 요청
async function fetchAIResponse() {
  try {
    // chatHistory를 js array로 변환
    const messages = chatHistory.value.map(msg => ({
      role: msg.sender === '나' ? 'user' : 'assistant',
      content: msg.content, // 여기서 msg.content를 custom prompt로 변환
    }));
    
    // 시스템 메시지 추가 (대화 설정)
    messages.unshift({
      role: 'system',
      content: 'You are a helpful assistant.',
    });
    
    const response = await axios.post(
      apiEndpoint,
      {
        model: "gpt-4o-mini",
        messages: messages,
        // temperature: 0.8,
        // top_p: 1,
        // frequency_penalty: 0.5,
        // presence_penalty: 0.5,
        stop: ["Stop"],
      },
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${apiKey}`,
        },
      }
    );
    return response.data.choices[0].message.content
  } catch (error) {
    console.error("API 요청 중 오류 발생:", error)
    return "AI 상담사의 응답을 가져오는 데 실패했습니다."
  }
}

// 메시지 서버로 보내는 함수
function storeMessage(msg) {
  axios({
    method: 'post',
    url: `${userStore.URL}/accounts/chat/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    },
    data: msg,
  })
  .then((res) => {
    console.log("RECEIVE SUCCESS")
    console.log(res)
  })
  .catch((err) => {
    console.log("SAVE DATA FAILED")
    console.log(err.response.data)
  })
}

// 메시지 전송 함수
async function sendMessage() {
  if (!message.value) return

  // 사용자 메시지 추가
  addMessage('나', message.value)

  // ChatGPT 응답 가져오기
  const aiResponse = await fetchAIResponse()

  // 챗봇 메시지 추가
  addMessage('AI 상담사', aiResponse)
  
  // 서버에 메시지 전송
  storeMessage(chatHistory.value.slice(-2))

  // 입력 필드 초기화
  message.value = ''
}

// chatHistory 서버에서 불러오기
onBeforeMount(() => {
  // 서버로 이전 대화 내용 가져오기
  axios({
    method: 'get',
    url: `${userStore.URL}/accounts/chat/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    },
  })
    .then((res) => {
      console.log("LOAD HISTORY SUCCESS")
      chatHistory.value = res.data
      scrollToBottom()
    })
    .catch((err) => {
      console.log("LOAD HISTORY FAILD")
      console.log(err)
    })
})
</script>

<style>
/* 전체 컨테이너 */
#chat-container {
  display: flex; /* 플렉스 박스 활성화 */
  flex-direction: column; /* 세로 정렬 */
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  background: #f9f9f9;
  height: 700px; /* 높이 조정 */
}

/* 메시지 박스 */
#chat-messages {
  flex: 1; /* 남는 공간을 모두 차지 */
  overflow-y: auto; /* 스크롤 활성화 */
  border: 1px solid #ddd;
  margin-bottom: 1rem;
  padding: 0.5rem;
  background: white;
}

/* 기본 메시지 스타일 */
.message {
  display: flex;
  flex-direction: column;
  margin-bottom: 0.5rem;
  max-width: 60%;
  word-wrap: break-word;
}

.message-left {
  align-items: flex-start;
}

.message-right {
  align-items: flex-end;
  margin-left: auto;
}

/* 발신자 정보 스타일 */
.sender {
  font-size: 0.8rem;
  color: #9e9e9e; /* 지정된 색상 사용 */
}

/* 메시지 내용 스타일 */
.content {
  padding: 0.5rem 1rem;
  border-radius: 10px;
}

/* 내 메시지 스타일 */
.message-right .content {
  background: #3572ef;
  color: white;
}

/* 상대방 메시지 스타일 */
.message-left .content {
  background: #d7d7d7;
  color: black;
}

/* 입력 영역 */
#user-input {
  display: flex;
  gap: 0.5rem;
  padding-top: 0.5rem; /* 입력창 위쪽 여백 */
  border-top: 1px solid #ddd; /* 시각적 구분선 */
}

#user-input input {
  flex: 1; /* 입력 필드가 버튼보다 넓게 */
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 8px;
}

#user-input button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 8px;
  background: #050c9c;
  color: white;
  cursor: pointer;
}

#user-input button:hover {
  background: #3572ef;
}
</style>
