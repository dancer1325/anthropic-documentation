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

* TODO: Claude Code reads memories recursively: starting in the cwd, Claude Code recurses up to (but not including) the root directory */* and reads any CLAUDE.md or CLAUDE.local.md files it finds. This is especially convenient when working in large repositories where you run Claude Code in *foo/bar/*, and have memories in both *foo/CLAUDE.md* and *foo/bar/CLAUDE.md*.

Claude will also discover CLAUDE.md nested in subtrees under your current working directory. Instead of loading them at launch, they are only included when Claude reads files in those subtrees.

## Quickly add memories with the `#` shortcut

The fastest way to add a memory is to start your input with the `#` character:

```
# Always use descriptive variable names
```

You'll be prompted to select which memory file to store this in.

## Directly edit memories with `/memory`

Use the `/memory` slash command during a session to open any memory file in your system editor for more extensive additions or organization.

## Set up project memory

Suppose you want to set up a CLAUDE.md file to store important project information, conventions, and frequently used commands.

Bootstrap a CLAUDE.md for your codebase with the following command:

```
> /init 
```

<Tip>
  Tips:

  * Include frequently used commands (build, test, lint) to avoid repeated searches
  * Document code style preferences and naming conventions
  * Add important architectural patterns specific to your project
  * CLAUDE.md memories can be used for both instructions shared with your team and for your individual preferences.
</Tip>

## Organization-level memory management

Enterprise organizations can deploy centrally managed CLAUDE.md files that apply to all users.

To set up organization-level memory management:

1. Create the enterprise memory file in the appropriate location for your operating system:

* macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`
* Linux/WSL: `/etc/claude-code/CLAUDE.md`
* Windows: `C:\ProgramData\ClaudeCode\CLAUDE.md`

2. Deploy via your configuration management system (MDM, Group Policy, Ansible, etc.) to ensure consistent distribution across all developer machines.

## Memory best practices

* **Be specific**: "Use 2-space indentation" is better than "Format code properly".
* **Use structure to organize**: Format each individual memory as a bullet point and group related memories under descriptive markdown headings.
* **Review periodically**: Update memories as your project evolves to ensure Claude is always using the most up to date information and context.
