import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/Home.vue';
import Login from '@/views/Login.vue';

import auth from '@/auth';

Vue.use(VueRouter);

const routes = [
  {
    name: 'Home',
    path: '/',
    component: Home,
  },
  {
    name: 'Login',
    path: '/login',
    component: Login,
  },
  {
    path: '/im',
    component: () => import(/* webpackChunkName: "im" */ '@/views/iM.vue'),
    children: [{
      name: 'iM',
      path: '',
      component: () => import(/* webpackChunkName: "im" */ '@/components/iM/List.vue')
    },{
      name: 'cyTus Post',
      path: ':id',
      component: () => import(/* webpackChunkName: "im" */ '@/components/iM/Post.vue')
    }]
  },
  {
    name:  'OS',
    path:  '/os',
    alias: ['/os/t/id?', '/os/c/:chara/:id?', ],
    component: () => import(/* webpackChunkName: "os" */ '@/views/OS.vue'),
  },
  {
    name: 'DB',
    path: '/db/:chara?/:id?',
    component: () => import(/* webpackChunkName: "db" */ '@/views/DB.vue'),
  }
]

const router = new VueRouter({
  routes,
  beforeEach(to, from, next) {
    console.log(to.path.startsWith('/login')||auth());
    if (to.path.startsWith('/login')||auth()) {
      if (window._czc)
        window._czc.push(["_trackPageview", to.path, from.path]);
      next();
    } else next('/login');
  }
});

export default router
