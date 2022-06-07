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
    path: "/Hello",
    name: "Hello",
    component: HelloWorld,
  },
  {
    path: "/List",
    name: "List",
    component: UserList,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;