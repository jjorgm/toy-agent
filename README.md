# AI Coding Agent

A lightweight, autonomous coding agent built in Python that leverages LLMs to inspect files, execute code, and iteratively fix bugs or implement features within a repository.

## Features

- **Autonomous Tool Use:** Equipped with tools to read, write, and execute code within the project directory.
- **Iterative Problem Solving:** Uses LLM reasoning loops to diagnose issues, test solutions, and verify fixes.
- **Model Agnostic:** Connects via OpenRouter to support various LLM providers and models.

## How It Works

1. Takes a high-level coding task or bug report from the user.
2. Explores the codebase using file system tools.
3. Formulates a plan, applies modifications, and runs tests or scripts to verify changes.
4. Reports final results back to the user.

> **Note:** This is an experimental educational project. Exercise caution when granting LLMs file system access and execution privileges.
