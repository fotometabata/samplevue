// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import moment from 'moment'

// コンポーネント読込
import HelloButton from '@/button/HelloButton'
Vue.component(HelloButton.name, HelloButton)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

/**
 * 日付を yyyy-mm-dd に変換するフィルター
 */
Vue.filter('date_format', function (val) {
  return moment(val).locale('ja').format('YYYY年MM月DD日(ddd) HH時mm分ss秒')
})
