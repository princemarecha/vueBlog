import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import HomeView from '../views/HomeView.vue'
import Blog from '../views/Blog.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/:category_slug/:blog_slug',
    name: 'blog',
    component: Blog
  },
  {
    path: '/:category_slug',
    name: 'category',
    component: Category

  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin:true
    }
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: Login
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
