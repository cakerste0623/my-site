import { createWebHistory, createRouter } from "vue-router";
import HomePage from "@/components/HomePage.vue";
import SongPage from "@/components/SongPage.vue";
import ResumePage from "@/components/ResumePage.vue";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/song",
    name: "SongPage",
    component: SongPage,
  },
  {
    path: "/resume",
    name: "ResumePage",
    component: ResumePage
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;