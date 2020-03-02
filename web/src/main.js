import Vue from 'vue'
import App from './App.vue'
import router from './router'
import i18n from './i18n'

Vue.config.productionTip = false;

// set language
if (!localStorage['auth']) localStorage.setItem('auth', 'OPCI_');

// mount app
new Vue({ router, i18n, render: h => h(App) }).$mount('#app');
