import { createWebHistory, createRouter } from "vue-router";
import UserLogin from "../components/UserLogin.vue";
import HomePage from "../components/HomePage.vue";
import HackathonOverview from "../components/dashboards/hackathons/HackathonOverview";

const routes = [
  {
    path: "/",
    name: "Login",
    component: UserLogin,
  },
  {
    path: "/home",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/hackathons",
    name: "Hackathons",
    component: HackathonOverview,
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes: routes
});

export default router;
