import { createWebHistory, createRouter } from "vue-router";
import HomePage from "@/components/HomePage.vue";
import SongPage from "@/components/SongPage.vue";

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
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;