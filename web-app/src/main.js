import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "./main.css";

if (import.meta.hot) {
    import.meta.hot.on("vite:beforeUpdate", () => console.clear());
}

import { createApp } from "vue";
import App from "./App.vue";

createApp(App).mount("#app");
