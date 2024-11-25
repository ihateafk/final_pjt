<!-- <template>
  <body>
    <div id="chat-container">
        <div id="chat-messages" ref="chatMessages"></div>
        <div id="user-input">
            <input @keyup.enter="userInputEvent" type="text" placeholder="메시지를 입력하세요..." v-model.trim="message"/>
            <button @click="sendButtonEvent">전송</button>
        </div>
    </div>
  </body>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';

const message = ref('')
// 채팅 메시지를 표시할 DOM
const chatMessages = ref([])
// 사용자 입력 필드
const userInput = document.querySelector('#user-input input');
// 전송 버튼
const sendButton = document.querySelector('#user-input button');
// 발급받은 OpenAI API 키를 변수로 저장
const apiKey = import.meta.env.VITE_APP_GPT_API_KEY;
// OpenAI API 엔드포인트 주소를 변수로 저장
const apiEndpoint = 'https://api.openai.com/v1/chat/completions'
function addMessage(sender, message) {
    // 새로운 div 생성
    const messageElement = document.createElement('div');
    // 생성된 요소에 클래스 추가
    messageElement.className = 'message';
     // 채팅 메시지 목록에 새로운 메시지 추가
    messageElement.textContent = `${sender}: ${message}`;
    chatMessages.prepend(messageElement);
}
// ChatGPT API 요청
async function fetchAIResponse(prompt) {
    // API 요청에 사용할 옵션을 정의
    axios({
      method: 'post',
      url: apiEndpoint,
      headers: {
        "Content-Type": 'application/json',
        Authorization: `Bearer ${apiKey}`
      },
      data: JSON.stringify({
        model: "gpt-4o-mini",
        message: [
          {
            role: "system",
            content: ""
          },
          {
            role: "user",
            content: prompt
          }
        ],
        temperature: 0.8, // 모델의 출력 다양성
        max_tokens: 1024, // 응답받을 메시지 최대 토큰(단어) 수 설정
        top_p: 1, // 토큰 샘플링 확률을 설정
        frequency_penalty: 0.5, // 일반적으로 나오지 않는 단어를 억제하는 정도
        presence_penalty: 0.5, // 동일한 단어나 구문이 반복되는 것을 억제하는 정도
        stop: ["Stop"],
      })
    })
      .then((res) => {
        console.log(res)
        const data = res.json()
        const aiResponse = data.choices[0].message.content
        return aiResponse
      })
      .catch((err) => {
        console.log(err)
      })
    // const requestOptions = {
    //     method: 'POST',
    //     // API 요청의 헤더를 설정
    //     headers: {
    //         'Content-Type': 'application/json',
    //         'Authorization': `Bearer ${apiKey}`
    //     },
    //     body: JSON.stringify({
    //         model: "gpt-4o-mini",  // 사용할 AI 모델
    //         messages: [{
    //             role: "user", // 메시지 역할을 user로 설정
    //             content: prompt // 사용자가 입력한 메시지
    //         }, ],
    //         temperature: 0.8, // 모델의 출력 다양성
    //         max_tokens: 1024, // 응답받을 메시지 최대 토큰(단어) 수 설정
    //         top_p: 1, // 토큰 샘플링 확률을 설정
    //         frequency_penalty: 0.5, // 일반적으로 나오지 않는 단어를 억제하는 정도
    //         presence_penalty: 0.5, // 동일한 단어나 구문이 반복되는 것을 억제하는 정도
    //         stop: ["Human"], // 생성된 텍스트에서 종료 구문을 설정
    //     }),
    // };
    // API 요청후 응답 처리
    // try {
    //     const response = await fetch(apiEndpoint, requestOptions);
    //     const data = await res.json();
    //     const aiResponse = data.choices[0].message.content;
    //     return aiResponse;
    // } catch (error) {
		// console.error('OpenAI API 호출 중 오류 발생:', error);
    //     return 'OpenAI API 호출 중 오류 발생';
    // }
}
// 전송 버튼 클릭 이벤트 처리
const sendButtonEvent = async () => {
    // 사용자가 입력한 메시지
    // message.value = userInput.value.trim();
    // 메시지가 비어있으면 리턴
    if (message.value.length === 0) return;
    // 사용자 메시지 화면에 추가
    addMessage('나', message);
    userInput.value = '';
    //ChatGPT API 요청후 답변을 화면에 추가
    const aiResponse = await fetchAIResponse(message);
    addMessage('챗봇', aiResponse);
    message.value = ''
}
// 사용자 입력 필드에서 Enter 키 이벤트를 처리
const userInputEvent = () => {
  sendButtonEvent()
}
</script>

<style lang="css" scoped>
body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}
.message {
    border-top: 1px solid #ccc;
    padding: 10px;
    margin-top: 5px;
    background-color: #e6e6e6;
}
#chat-container {
    width: 400px;
    height: 600px;
    display: flex;
    flex-direction: column;
    border: 1px solid #ccc;
}
#chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 10px;
    display: flex;
    flex-direction: column-reverse;
}
#user-input {
    display: flex;
    padding: 10px;

}
#user-input input {
    flex: 1;
    padding: 10px;
    outline: none;
}
#user-input button {
    border: none;
    background-color: #1e88e5;
    color: white;
    padding: 10px 15px;
    cursor: pointer;
}
</style> -->