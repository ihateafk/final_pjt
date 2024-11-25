<!-- <template>
  <div>
    추천 챗봇
    <div id='chat-container'>
      <button @click="addnumber">+</button>
      <div id="chat-messages">
        <p  v-for="content in chatting">
          {{ content }}
        </p>
      </div>
      <div id="user-input">
        <input type="text" placeholder="Enter your message..." v-model="user_input">
        <button @click="chatCompletion">Send</button>
      </div>
    </div>
    {{ response_message }}
  </div>
</template>

<script setup>
import axios from 'axios';
import OpenAI from 'openai';
import { computed, ref, watch } from 'vue';

const numberSet = ref([])
let i = 1
const addnumber = function () {
  numberSet.value.unshift(i++)
}

const chatting = ref([])
const user_input = ref('')
const response = ref('')
const response_message = ref('')

const openai = new OpenAI({
  apiKey: import.meta.env.VITE_APP_GPT_API_KEY,
  dangerouslyAllowBrowser: true,
})

const chatCompletion = async function() {
  response.value = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      {
        role: 'system',
        content: [{ type: 'text', text: 'You are a competent bank advisor.'}]
      },
      {
        role: 'user',
        content: [{ type: 'text', text: user_input.value }]
      }
    ]
  })
  console.log(response.value)
  console.log(response.value.choices)
  console.log(response.value.choices[0])
  console.log(response.value.choices[0].message)
}

watch(() => response.value, () => response_message.value = response.value.choices[0].message)
</script>

<style lang="css" scoped>
#chat-container {
    width: 800px;
    height: 800px;
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
</style> -->