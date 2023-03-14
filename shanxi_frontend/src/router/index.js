import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/test',
      name: 'Test',
      component: () => import('@/pages/Test')
    },
    {
      path: '/',
      name: 'Home',
      component: () => import('@/pages/home')
    },
    {
      path: '/home',
      name: 'Home',
      component: () => import('@/pages/home')
    },
    {
      path: '/history',
      name: 'History',
      component: () => import('@/pages/ShanxiHistory')
    },
     {
      path: '/CulturalWork',
      name: 'CulturalWork',
      component: () => import('@/pages/CulturalWork')
    },
     {
      path: '/ShanxiFolk',
      name: 'ShanxiFolk',
      component: () => import('@/pages/ShanxiFolk')
    },
     {
      path: '/MaterialFolk',
      name: 'MaterialFolk',
      component: () => import('@/pages/MaterialFolk')
    },
     {
      path: '/SpiritualFolk',
      name: 'SpiritualFolk',
      component: () => import('@/pages/SpiritualFolk')
    },
     {
      path: '/DialectFolk',
      name: 'DialectFolk',
      component: () => import('@/pages/DialectFolk')
    },
    {
      path: '/ShanxiFood',
      name: 'ShanxiFood',
      component: () => import('@/pages/ShanxiFood')
    },
     {
      path: '/ShanxiOpera',
      name: 'ShanxiOpera',
      component: () => import('@/pages/ShanxiOpera')
    },
     {
      path: '/ShanxiLiterature',
      name: 'ShanxiLiterature',
      component: () => import('@/pages/ShanxiLiterature')
    },
     {
      path: '/SearchBook',
      name: 'SearchBook',
      component: () => import('@/pages/SearchBook')
    },
    {
      path: '/product',
      name: 'CulturalProduct',
      component: () => import('@/pages/CulturalProduct')
    },
    {
      path: '/Index',
      name: 'Index',
      component: () => import('@/pages/Index')
    },
    {
      path: '/Index3',
      name: 'Index3',
      component: () => import('@/pages/Index3')
    },
     {
      path: '/SingleBook',
      name: 'SingleBook',
      component: () => import('@/pages/SingleBook')
    },
    {
      path: '/Opera1',
      name: 'Opera1',
      component: () => import('@/pages/Opera1')
    },
    {
      path: '/Opera2',
      name: 'Opera2',
      component: () => import('@/pages/Opera2')
    },
    {
      path: '/Opera3',
      name: 'Opera3',
      component: () => import('@/pages/Opera3')
    },
    {
      path: '/Opera4',
      name: 'Opera4',
      component: () => import('@/pages/Opera4')
    },
    {
      path: '/Food1',
      name: 'Food1',
      component: () => import('@/pages/Food1')
    },
    {
      path: '/Food2',
      name: 'Food2',
      component: () => import('@/pages/Food2')
    },
    {
      path: '/Food3',
      name: 'Food3',
      component: () => import('@/pages/Food3')
    },
    {
      path: '/Food4',
      name: 'Food4',
      component: () => import('@/pages/Food4')
    },
    {
      path: '/DialectDisplay',
      name: '/DialectDisplay',
      component: () => import('@/pages/DialectDisplay')
    },
    {
      path: '/DialectClassification',
      name: '/DialectClassification',
      component: () => import('@/pages/DialectClassification')
    }
  ]
})
