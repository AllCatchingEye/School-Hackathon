import { createWebHistory, createRouter } from "vue-router";
import UserLogin from "../components/UserLogin.vue";
import HelloWorld from "../components/HelloWorld.vue";
import HomePage from "../components/HomePage.vue";

const routes = [
  {
    path: "/",
    name: "Login",
    component: UserLogin,
  },
  {
    path: "/hello",
    name: "Hello",
    component: HelloWorld,
  },
  {
    path: "/home",
    name: "Home",
    component: HomePage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes
});

export default router;