import { createWebHistory, createRouter } from "vue-router";
import UserLogin from "../components/dashboards/users/UserLogin.vue";
import UserOverview from "../components/dashboards/users/EntryList.vue";
import DashboardComponent from "../components/dashboards/main/DashboardMain.vue";
import HackathonOverview from "../components/dashboards/hackathons/EntryList";
import baseScreen from "../components/childScreen/BaseScreen";
import SelectHackathon from "../components/dashboards/keys/SelectHackathon";
import KeyOverview from "../components/dashboards/keys/overview/KeyOverview";
import OrganisationOverview from "../components/dashboards/organisations/EntryList";
import SelectHackathonSubmission from "../components/dashboards/submissions/SelectHackathon";
import KeyOverviewSubmission from "../components/dashboards/submissions/overview/SubOverview";

const routes = [

  {
    path: "/submission/:hackathonSlug?/:uuid?",
    name: "baseScreen",
    component: baseScreen
  },
  {
    path: "/login",
    alias: "/",
    name: "Login",
    component: UserLogin,
  },
  {
    path: "/user",
    name: "UserOverview",
    component: UserOverview,
  },
  {
    path: "/hackathons",
    name: "Hackathons",
    component: HackathonOverview,
  },
  {
    path: "/keys",
    name: "SelectHackathon",
    component: SelectHackathon,
  },
  {
    path: "/keys/overview",
    name: "KeyOverview",
    component: KeyOverview,
  },
  {
    path: "/schools",
    name: "Organisation",
    component: OrganisationOverview,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: DashboardComponent,
  },
  {
    path: "/submissions/",
    name: "Submissions",
    component: SelectHackathonSubmission,
  },  {
    path: "/submissions/overview",
    name: "KeyOverviewSubmission",
    component: KeyOverviewSubmission,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes
});

export default router;
