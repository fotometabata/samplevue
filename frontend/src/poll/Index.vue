<template>
    <div>
        {{msg}}<br>
        <div v-for="data in questions" v-bind:key="'question_id:' + data.id">
          {{data.questionText}}<br>
          <div v-if="data.choices.length">
            <div class="c-card" v-for="c in data.choices" :key="c.id">
              <label>
                <input type="radio" v-model="vote" v-bind:value="c.id">
                {{c.choiceText + ' 投票数：' + c.votes}}
              </label>
            </div>
            <input type="button" @click="onChoiceUpdate" :disabled="!voteEnabled(data.choices)" value="投票">
          </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PollComponent',
  data () {
    return {
      msg: 'Poll display successfully',
      questions: [],
      vote: null
    }
  },
  methods: {
    fetchData () {
      axios.get(`${process.env.API_ENDPOINT}questions/`).then(res => {
        this.questions = res.data.results
      })
    },
    onChoiceUpdate () {
      if (!this.vote) {
        return
      }
      axios.post(`${process.env.API_ENDPOINT}choices/${this.vote}/`).then(res => {
        this.fetchData()
      })
    },
    voteEnabled (choices) {
      if (!this.vote) {
        return false
      }
      return choices.some(x => x.id === this.vote) // 選択されたidが選択肢の中に含まれていれば活性
    }
  },
  mounted () {
    this.fetchData()
  }
}
</script>
