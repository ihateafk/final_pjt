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
        placeholder="무엇을 도와드릴까요?"
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

// OpenAI API 설정
const apiKey = import.meta.env.VITE_APP_GPT_API_KEY;
const apiEndpoint = 'https://api.openai.com/v1/chat/completions'

// 상태 변수
const message = ref('')
const chatHistory = ref([])
const chatMessages = ref(null)
const prompt = 
`# 페르소나
너는 세계에서 가장 유능한 재무설계사야. 너는 고객들에게 좋은 금융 상품을 추천해 줘야해. 고객들은 상품을 따로 찾아보지 않아서 니가 고객들에게 정확한 정보만 전달해 줘야해. 고객들에게 답변할 때는 답변 조건을 지키며 대답해야해.
# 답변 조건
1. 예금, 적금 정보는 반드시 'https://finlife.fss.or.kr/finlife/main/main.do?'에서 필요한 정보를 찾아서 답변할 것
2. 상품 추천을 해 줄 때 상품의 금리, 가입 금액, 가입 기간을 등을 물어서 추천해 줄 것
3. 실제로 존재하는 은행 및 상품만 말할 것
4. 현재 판매 중인 상품만 추천해 줄 것
5. 고객의 구체적인 요청이 없다면 상품은 제2금융권의 상품까지 추천해 줄 것
6. 주택청약저축 상품은 고객이 청약저축이나 주택청약 같이 요구하지 않으면 추천하지 말 것
7. 답변에 금융상품통합비교공시 및 그 사이트 주소를 자주 넣지 말 것
8. 예금, 적금 정보는 예시를 참고하여 실제 은행 및 상품의 정보를 알려줄 것
# 상품 추천 시 출력 형식 예시
## 예금
1. @@은행 "%%%%예금"
   - 금리 : 2.70% (24개월 기준)
   - 최고 우대 금리 : 2.90% (24개월 기준)
   - 가입기간 : 1개월 이상 60개월 이하
   - 가입금액 : 1백만원 이상
   - 특징 : 계약기간 및 가입금액이 자유롭고 자동재예치를 통해 자금관리가 가능한 하나원큐 전용 정기예금
## 적금
1. ????은행 "***적금"
   - 금리 : 3.70% (12개월 기준)
   - 최고 우대 금리 : 없음
   - 가입기간 : 12개월
   - 가입금액 : 월 최대 50만원
   - 특징 : 언제 어디서나 쉽고 빠르게 가입할 수 있는 적금`


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
  scrollToBottom() // 메시지 추가 후 자동 스크롤
}

// ChatGPT API 요청
async function getAIResponse() {
  // chatHistory를 js array로 변환
  const messages = chatHistory.value.map(msg => ({
    role: msg.sender === '나' ? 'user' : 'assistant',
    content: msg.content
  }))

  // 시스템 메시지 추가 (대화 설정)
  messages.unshift({
    role: 'system',
    content: prompt,
  })

  let response
  
  await axios.post(
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
  )
    .then((res) => {
      response = res.data.choices[0].message.content
    })
    .catch((err) => {
      console.error("API 요청 중 오류 발생:", err)
      response = "AI 상담사의 응답을 가져오는 데 실패했습니다."
    })
  
  return response
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
  const aiResponse = await getAIResponse()

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
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  background: #f9f9f9;
  height: 700px;
}

/* 메시지 박스 */
#chat-messages {
  flex: 1;
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
  overflow-wrap: break-word;
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
