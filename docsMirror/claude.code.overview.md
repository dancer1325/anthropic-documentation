https://code.claude.com/docs/en/overview

# Claude Code overview

* goal
  * learn Claude Code

* Claude Code
  * == 💡Anthropic's agentic coding tool💡 / 
    * lives | your terminal
    * helps you turn ideas -- into -- code faster

## Get started in 30 seconds

* ⚠️Prerequisites⚠️
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

## What Claude Code does for you?

* **Build features from descriptions (plain natural language)**
* **Debug and fix issues**
* **Navigate any codebase**
* **Pull -- from -- external datasources**
  * -- via -- [MCP](claude.code.mcp.md)
  * _Examples:_ Google Drive, Figma, and Slack
* **Automate tedious tasks**
  * _Examples:_ lint issues, resolve merge conflicts, write release notes, ...

## Why developers love Claude Code

* **Works | your terminal**
  * == ❌NOT require ANOTHER IDE❌
* **Takes action**
  * -- via -- [MCP](claude.code.mcp.md)
  * _Example:_ edit files, run commands, create commits, ...
* **Unix philosophy**
  * == 
    * composable
      * == valid in `|` (== pipes)
      * _Example:_ `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"`
    * scriptable
      * == valid | command line
      * _Example:_ `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`
* **Enterprise-ready**
  * Enterprise-grade 
    * [security](claude.code.security.md),
    * [privacy](claude.code.data-usage.md),
    * [compliance](https://trust.anthropic.com/)
