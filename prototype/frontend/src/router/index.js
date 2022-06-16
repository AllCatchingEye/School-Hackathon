import { createWebHistory, createRouter } from "vue-router";
import UserLogin from "../components/dashboards/users/UserLogin.vue";
import UserOverview from "../components/dashboards/users/UserOverview.vue";
import DashboardComponent from "../components/dashboards/main/DashboardMain.vue";
import HackathonOverview from "../components/dashboards/hackathons/HackathonOverview";
import OrganisationOverview from "../components/dashboards/organisations/OrganisationOverview";
import ToDoMain from "../components/todo/ToDoMain"

const routes = [
  {
    path: "/login",
    name: "Login",
    component: UserLogin,
  },
  {
    path: "/user-overview",
    name: "UserOverview",
    component: UserOverview,
  },
  {
    path: "/hackathons",
    name: "Hackathons",
    component: HackathonOverview,
  },
  {
    path: "/schools",
    name: "Organisation",
    component: OrganisationOverview,
  },
  {
    path: "/",
    name: "Dashboard",
    component: DashboardComponent,
  },
  {
    path: "/todo",
    name: "Todo",
    component: ToDoMain,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes
});

export default router;
