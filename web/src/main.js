import Vue from 'vue';
import VueGtag from "vue-gtag";
import App from './App.vue';
import i18n from './i18n';
import router from './router';

Vue.config.productionTip = false;

Vue.use(VueGtag, {
  config: {
    id: location.hostname.indexOf("gitee.io")==-1?"UA-159441633-1":"UA-159441633-2"
  }
}, router);

// set language
if (!localStorage['auth']) localStorage.clear(), localStorage['auth'] = 'OPCI_';

// mount app
new Vue({ router, i18n, render: h => h(App) }).$mount('#app');
