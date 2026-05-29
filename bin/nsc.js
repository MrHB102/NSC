#!/usr/bin/env node

import inquirer from "inquirer";
import chalk from "chalk";

console.log(
  chalk.cyan(`
NSC — NonSlopContext
Governance for Autonomous Coding Agents
`)
);

const run = async () => {
  const { agent } = await inquirer.prompt([
    {
      type: "list",
      name: "agent",
      message: "Select installation target",
      choices: [
        "1. Claude Code",
        "2. OpenClaude",
        "3. Codex",
        "4. Cursor",
        "5. Windsurf",
        "6. Continue",
        "7. Aider",
        "8. OpenHands",
        "9. Install All"
      ]
    }
  ]);

  console.log(chalk.green(`Installing NSC for ${agent}`));
};

run();
