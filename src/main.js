// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

/* eslint-disable no-new */
import Vue from 'vue'
import App from './App'
import router from './router'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './styles/normalize.css'

import VueLoading from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/vue-loading.css'

import UUID from "vue-uuid";

import {store} from './store/store'

import VueCookies from 'vue-cookies'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueLoading)
Vue.use(UUID)
Vue.use(VueCookies)

new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
