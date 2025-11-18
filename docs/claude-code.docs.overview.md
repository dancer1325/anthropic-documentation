https://code.claude.com/docs/en/overview

# Claude Code overview

* goal
  * learn Claude Code

* Claude Code
  * == Anthropic's agentic coding tool / 
    * lives | your terminal
    * helps you turn ideas -- into -- code faster

## Get started in 30 seconds

* Prerequisites
  * [Claude.ai](https://claude.ai), OR
    * recommended
  * [Claude Console account](https://console.anthropic.com/)

### ways to install
#### | macOS/Linux
    ```bash  theme={null}
    curl -fsSL https://claude.ai/install.sh | bash
    ```
#### Homebrew
* `brew install --cask claude-code`

#### Windows
```powershell  theme={null}
irm https://claude.ai/install.ps1 | iex
```

#### NPM
* requirements
  * [Node.js 18+](https://nodejs.org/en/download/)
* `npm install -g @anthropic-ai/claude-code`

### how to use?

```bash  theme={null}
cd your-project
claude

# & log in
```

## What Claude Code does for you

* TODO:
* **Build features from descriptions**: Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
* **Debug and fix issues**: Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
* **Navigate any codebase**: Ask anything about your team's codebase, and get a thoughtful answer back. Claude Code maintains awareness of your entire project structure, can find up-to-date information from the web, and with [MCP](/en/mcp) can pull from external datasources like Google Drive, Figma, and Slack.
* **Automate tedious tasks**: Fix fiddly lint issues, resolve merge conflicts, and write release notes. Do all this in a single command from your developer machines, or automatically in CI.

## Why developers love Claude Code

* **Works in your terminal**: Not another chat window. Not another IDE. Claude Code meets you where you already work, with the tools you already love.
* **Takes action**: Claude Code can directly edit files, run commands, and create commits. Need more? [MCP](/en/mcp) lets Claude read your design docs in Google Drive, update your tickets in Jira, or use *your* custom developer tooling.
* **Unix philosophy**: Claude Code is composable and scriptable. `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"` *works*. Your CI can run `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`.
* **Enterprise-ready**: Use the Claude API, or host on AWS or GCP. Enterprise-grade [security](/en/security), [privacy](/en/data-usage), and [compliance](https://trust.anthropic.com/) is built-in.
