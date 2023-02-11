import { createWebHistory, createRouter } from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue";
import SongPage from "@/components/SongPage.vue";

const routes = [
  {
    path: "/",
    name: "HelloWorld",
    component: HelloWorld,
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