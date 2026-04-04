import fs from "fs";
import path from "path";
import typescript from "@rollup/plugin-typescript";
import json from "@rollup/plugin-json";
import { nodeResolve } from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";
import { terser } from "@rollup/plugin-terser";

function generateIconList() {
  return {
    name: "generate-mushic-icon-list",
    buildStart() {
      const iconDir = path.resolve("icons/mushic");
      const files = fs.readdirSync(iconDir)
        .filter((f) => f.endsWith(".svg"));

      const out = {};
      for (const file of files) {
        const name = file.replace(".svg", "");
        out[name] = file;
      }

      fs.writeFileSync(
        path.resolve("src/utils/mushic-icons.json"),
        JSON.stringify(out, null, 2)
      );

      console.log(`Generated mushic-icons.json with ${files.length} icons`);
    }
  };
}

export default {
  input: "src/mushic-icons.ts",
  output: {
    file: "dist/mushic-icons.js",
    format: "es",
  },
  plugins: [
    generateIconList(),
    typescript(),
    json(),
    nodeResolve(),
    commonjs(),
    terser(),
  ],
};
