import Vue from 'vue'
import App from './App.vue'
import router from './router'
import i18n from './i18n'

Vue.config.productionTip = false;

// set language
if (!localStorage['auth']) localStorage.setItem('auth', 'OPCI_');

// mount app
new Vue({
  router,
  i18n,
  render: h => h(App)
}).$mount('#app')

// statistics
/*
const umeng = document.createElement("script");
umeng.src = "https://v1.cnzz.com/z_stat.php?id=1278083824&web_id=1278083824";
umeng.language = "JavaScript";
umeng.id = "cnzz";
document.body.appendChild(umeng);
*/