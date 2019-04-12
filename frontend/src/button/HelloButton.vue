<template>
    <div>
        <input type="button" v-bind:value="button_message">
    </div>
</template>

<script>
export default {
  name: 'HelloButton',
  data () {
    return {
      button_message: 'Hello Button'
    }
  }
}
</script>
