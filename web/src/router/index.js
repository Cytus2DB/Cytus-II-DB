import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '@/views/Home.vue';
import Login from '@/views/Login.vue';
import NotFound from '@/views/NotFound.vue';

import auth from '@/auth';

Vue.use(VueRouter);

const routes = [{
    name: 'Not Found',
    path: '*',
    component: NotFound,
  }, {
    name: 'Home',
    path: '/',
    component: Home,
  }, {
    name: 'Login',
    path: '/login',
    component: Login,
  }, {
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
  }, {
    name: 'DB',
    path: '/db',
    component: () => import(/* webpackChunkName: "db" */ '@/views/DB.vue'),
    children: [{
      name: 'DB Query',
      path: ':folder/:id',
      component: () => import(/* webpackChunkName: "db" */ '@/components/System/QueryDB.vue'),
    }]
  }, {
    name: 'OS',
    path: '/os',
    component: () => import(/* webpackChunkName: "os" */ '@/views/OS.vue'),
    children: [{
      name: 'OS Query',
      path: ':folder/:id',
      component: () => import(/* webpackChunkName: "os" */ '@/components/System/QueryOS.vue'),
    }]
  },
]

const router = new VueRouter({
  routes
});

router.beforeEach((to, from, next)=>{
  if (to.path=='/login' || auth()) next(); else next('/login');
});

export default router
