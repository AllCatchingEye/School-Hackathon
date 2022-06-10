import { createWebHistory, createRouter } from "vue-router";
import UserLogin from "../components/UserLogin.vue";
import HelloWorld from "../components/HelloWorld.vue";
import UserOverview from "../components/UserOverview.vue";
import DashboardComponent from "../components/DashboardComponent.vue";
import UserSurvey from "../components/UserSurvey.vue";
import UserManagement from "../components/UserManagement.vue";

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
    path: "/user-overview",
    name: "UserOverview",
    component: UserOverview,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: DashboardComponent,
  },
  {
    path: "/survey",
    name: "Survey",
    component: UserSurvey,
  },
  {
    path: "/management",
    name: "Management",
    component: UserManagement,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes
});

export default router;