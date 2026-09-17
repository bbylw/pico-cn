import { defineCollection } from "astro:content";
import { z } from "astro/zod";
import { glob } from "astro/loaders";

const docs = defineCollection({
  loader: glob({ base: "./src/content/docs", pattern: "**/*.mdx" }),
  schema: z.object({
    title: z.string(),
    chapter: z.string(),
    lead: z.string().default(""),
    badge: z.enum(["new"]).optional(),
    toc: z
      .array(z.object({ id: z.string(), text: z.string(), depth: z.number().int().default(2) }))
      .default([]),
  }),
});

export const collections = { docs };
