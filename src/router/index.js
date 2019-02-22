import Vue from 'vue';
import Router from 'vue-router';
import Customers from '@/components/Customers';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Customers',
      component: Customers,
    },
  ],
  mode: 'history',
});
