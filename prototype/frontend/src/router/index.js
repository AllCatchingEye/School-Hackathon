import { createWebHistory, createRouter } from "vue-router";
import UserLogin from "../components/dashboards/users/UserLogin.vue";
import UserOverview from "../components/dashboards/users/EntryList.vue";
import DashboardComponent from "../components/dashboards/main/DashboardMain.vue";
import HackathonOverview from "../components/dashboards/hackathons/EntryList";
import SelectHackathon from "../components/dashboards/keys/SelectHackathon";
import KeyOverview from "../components/dashboards/keys/overview/KeyOverview";
import baseScreen from "../components/childScreen/BaseScreen";
import OrganisationOverview from "../components/dashboards/organisations/EntryList";




const routes = [
  
  {
    path: "/submission/:hackathonSlug?/:uuid?",
    name: "baseScreen",
    component: baseScreen
  },
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
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes
});

export default router;
