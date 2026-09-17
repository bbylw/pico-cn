// @ts-check
import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";

export default defineConfig({
  site: "https://picocss.ndjp.net",
  integrations: [mdx()],
  markdown: {
    shikiConfig: {
      themes: { light: "vitesse-light", dark: "vitesse-dark" },
      defaultColor: false,
    },
  },
  vite: {
    ssr: {
      noExternal: ["@picocss/pico"],
    },
  },
});
