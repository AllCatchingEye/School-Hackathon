import { createWebHistory, createRouter } from "vue-router";
import UserLogin from "../components/UserLogin.vue";
import HelloWorld from "../components/HelloWorld.vue";
import UserList from "../components/UserList.vue";

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
    path: "/list",
    name: "List",
    component: UserList,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes
});

export default router;