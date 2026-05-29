#!/usr/bin/env node

import inquirer from "inquirer";
import chalk from "chalk";
import fs from "fs-extra";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// raiz do pacote
const rootDir = path.resolve(__dirname, "..");

// pasta source das skills
const skillsDir = path.join(rootDir, "skills");

// agentes
const agents = {
  "1. Claude Code": ".claude/skills",
  "2. OpenClaude": ".openclaude/skills",
  "3. Codex": ".codex/skills",
  "4. Cursor": ".cursor/skills",
  "5. Windsurf": ".windsurf/skills",
  "6. Continue": ".continue/skills",
  "7. Aider": ".aider/skills",
  "8. OpenHands": ".openhands/skills",
};

async function installSkills(targetPath) {
  const absoluteTarget = path.resolve(process.cwd(), targetPath);

  console.log(chalk.yellow(`Creating ${absoluteTarget}`));

  await fs.ensureDir(absoluteTarget);

  const skillFolders = await fs.readdir(skillsDir);

  for (const folder of skillFolders) {
    const source = path.join(skillsDir, folder);
    const destination = path.join(absoluteTarget, folder);

    const stat = await fs.stat(source);

    if (stat.isDirectory()) {
      console.log(chalk.cyan(`Installing skill: ${folder}`));

      await fs.copy(source, destination, {
        overwrite: true,
      });
    }
  }

  console.log(
    chalk.green(`NSC skills installed successfully in:`)
  );

  console.log(chalk.green(absoluteTarget));
}

async function installAll() {
  for (const target of Object.values(agents)) {
    await installSkills(target);
  }
}

async function run() {
  console.log(
    chalk.cyan(`
NSC — NonSlopContext
Governance for Autonomous Coding Agents
`)
  );

  const { agent } = await inquirer.prompt([
    {
      type: "list",
      name: "agent",
      message: "Select installation target",
      choices: [
        ...Object.keys(agents),
        "9. Install All",
      ],
    },
  ]);

  try {
    if (agent === "9. Install All") {
      await installAll();

      console.log(
        chalk.green("\nInstalled NSC on all supported agents.")
      );

      return;
    }

    const target = agents[agent];

    if (!target) {
      console.log(chalk.red("Invalid option."));
      process.exit(1);
    }

    await installSkills(target);
  } catch (error) {
    console.error(
      chalk.red(`Installation failed:`),
      error.message
    );

    process.exit(1);
  }
}

run();
