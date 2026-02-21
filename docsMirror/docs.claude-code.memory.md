https://docs.anthropic.com/en/docs/claude-code/memory

# Manage Claude's memory

* goal
  * about Claude Code's memory
    * how to manage ACROSS sessions / DIFFERENT memory locations 
    * best practices

* Claude Code
  * | ACROSS sessions, can remember your preferences
    * _Examples:_ style guidelines & common commands

## built-in memory type

| Memory Type                | Location                                                                                                                                                | Purpose                                             | Use Case Examples                                                    | Shared With                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------- |
| **Enterprise policy**      | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`<br />Linux: `/etc/claude-code/CLAUDE.md`<br />Windows: `C:\ProgramData\ClaudeCode\CLAUDE.md` | Organization-wide instructions / managed -- by -- IT/DevOps | Company coding standards,<br/> security policies,<br/> compliance requirements | ALL users \| organization       |
| **Project memory**         | 💡`./CLAUDE.md` 💡                                                                                                                                          | \| project, team-shared instructions            | Project architecture,<br/> coding standards,<br/> common workflows             | 👀Team members -- via -- source control👀 |
| **User memory**            | `~/.claude/CLAUDE.md`                                                                                                                                   | \| ALL projects, personal preferences                | Code styling preferences, <br/> personal tooling shortcuts                 | ONLY you \| ALL projects         |
| **Project memory (local)** | `./CLAUDE.local.md`                                                                                                                                     | Personal project-specific preferences               | ⚠️ deprecated -- by -- CLAUDE.md imports⚠️ <br/> your sandbox URLs,<br/> preferred test data     | ONLY you \| CURRENT project      |

* allows
  * | launch Claude Code,
    * ALL memory files are AUTOMATICALLY loaded | Claude Code's context /
      * files higher | hierarchy, 
        * take precedence == loaded first

## CLAUDE.md imports

* goal
  * | "CLAUDE.md" OR "~/.claude/CLAUDE.md"
    * import additional files & recursively imported (<= 5 recursive) -- via -- `@path/to/import` syntax

* _Examples:_ imports 3 files (@README, @package.json & @docs/git-instructions.md)

  ```.markdown, title=Claude.md
  See @README for project overview and @package.json for available npm commands for this project.

  # Additional Instructions
  - git workflow @docs/git-instructions.md
  ``` 

* ALLOWED `@path/to/import` syntax
  * relative paths
  * absolute paths

* ❌NOT valid,❌ 
  * if it's wrapped | markdown's 
    * <span> @.... </span>
    * `@...`

* `/memory`
  * 👀check the memory files / are loaded👀 

## How Claude looks up memories

* Claude Code reads 
  * memories ("CLAUDE.md" or "CLAUDE.local.md") 👀recursively👀 
    * /
      * start | cwd
      * recurses up to (WITHOUT including) the root directory */*
    * pros
      * | large repositories
    * ' subtrees, loaded
      * ❌NOT | launch❌
      * | Claude reads them 

## Quickly add memories -- via -- `#` 

* `# someInputToAdd` / 
  * 👀you are prompted to select the memory | store this in👀

      ```
      # Always use descriptive variable names
      ```

## edit memories -- via -- `/memory`

* [`/memory` slash command](docs.claude-code.slash-commands.md)
  * allows
    * 👀| session, open any memory file | your system editor -- to -- edit it👀

## Set up project memory

* `/init`
  * 👀bootstrap a CLAUDE.md | your codebase👀

* recommendations
  * add 
    * frequently used commands
      * Reason:🧠avoid repeated searches🧠
      * _Example:_ build, test, lint 
    * document code style preferences & naming conventions
    * your project's architectural patterns 

## Organization-level memory management

* how to set up memory type's enterprise policy?
  1. create it -- based on -- your OS
     * macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`
     * Linux/WSL: `/etc/claude-code/CLAUDE.md`
     * Windows: `C:\ProgramData\ClaudeCode\CLAUDE.md`
  2. deploy -- via -- your configuration management system (MDM, Group Policy, Ansible, etc.) / distributed | ALL developer machines

## Memory best practices

* **Be specific**
  * "2-space indentation" vs "Format code properly"
    * better
* **Use structure to organize**
  * format EACH individual memory -- as a -- bullet point 
  * group related memories | descriptive markdown headings
* **Review periodically**:
  * Reason:🧠your project evolves🧠
