---
Reference files:
  - [claude_developer_platform_urls.txt](../claude_developer_platform_urls.txt)
  - [claude_code_en_docs.txt](../claude_code_en_docs.txt)
---

# Claude Developer Platform
https://platform.claude.com/docs/en/intro

TODO: check if it's right the split in subsections

## Getting Started
* [overview](home.md)
* [Intro to Claude](docs.intro.md)
* [Quickstart](docs.get-started.md)

## About Claude
* Models
  * [Overview](about-claude._models_overview.md)
  * [Choosing a model](about-claude._models_choosing-a-model.md)
  * [What's new in Claude 4.5](about-claude._models_whats-new-claude-4-5.md)
  * [Migrating to Claude 4](about-claude._models_migrating-to-claude-4.md)
* [Model deprecations](about-claude._model-deprecations.md)
* [Pricing](about-claude._pricing.md)
* Use Case Guides
  * [Overview](about-claude._use-case-guides_overview.md)
  * [Content moderation](about-claude._use-case-guides_content-moderation.md)
  * [Customer support chat](about-claude._use-case-guides_customer-support-chat.md)
  * [Legal summarization](about-claude._use-case-guides_legal-summarization.md)
  * [Ticket routing](about-claude._use-case-guides_ticket-routing.md)
* [Glossary](about-claude._glossary.md)

## Build with Claude
* [Overview](build-with-claude._overview.md)
* Core Features
  * [Text generation](docs.build-with-claude.text-generation.md)
  * [Vision](build-with-claude._vision.md)
  * [Structured outputs](build-with-claude._structured-outputs.md)
  * [Extended thinking](build-with-claude._extended-thinking.md)
  * [Citations](build-with-claude._citations.md)
* Files & Documents
  * [Files](build-with-claude._files.md)
  * [PDF support](build-with-claude._pdf-support.md)
* Messaging & Streaming
  * [Working with messages](build-with-claude._working-with-messages.md)
  * [Streaming](build-with-claude._streaming.md)
* Performance & Optimization
  * [Prompt caching](build-with-claude._prompt-caching.md)
  * [Token counting](build-with-claude._token-counting.md)
  * [Batch processing](build-with-claude._batch-processing.md)
  * [Context windows](build-with-claude._context-windows.md)
  * [Context editing](build-with-claude._context-editing.md)
* Prompt Engineering
  * [Overview](build-with-claude._prompt-engineering_overview.md)
  * [Be clear and direct](build-with-claude._prompt-engineering_be-clear-and-direct.md)
  * [Use XML tags](build-with-claude._prompt-engineering_use-xml-tags.md)
  * [Chain of thought](build-with-claude._prompt-engineering_chain-of-thought.md)
  * [Chain prompts](build-with-claude._prompt-engineering_chain-prompts.md)
  * [Prefill Claude's response](build-with-claude._prompt-engineering_prefill-claudes-response.md)
  * [Multishot prompting](build-with-claude._prompt-engineering_multishot-prompting.md)
  * [System prompts](build-with-claude._prompt-engineering_system-prompts.md)
  * [Prompt templates and variables](build-with-claude._prompt-engineering_prompt-templates-and-variables.md)
  * [Long context tips](build-with-claude._prompt-engineering_long-context-tips.md)
  * [Extended thinking tips](build-with-claude._prompt-engineering_extended-thinking-tips.md)
  * [Claude 4 best practices](build-with-claude._prompt-engineering_claude-4-best-practices.md)
  * [Prompt generator](build-with-claude._prompt-engineering_prompt-generator.md)
  * [Prompt improver](build-with-claude._prompt-engineering_prompt-improver.md)
* Additional Features
  * [Skills guide](build-with-claude._skills-guide.md)
  * [Multilingual support](build-with-claude._multilingual-support.md)
  * [Embeddings](build-with-claude._embeddings.md)
  * [Search results](build-with-claude._search-results.md)
* Platform Integrations
  * [Claude on Amazon Bedrock](build-with-claude._claude-on-amazon-bedrock.md)
  * [Claude on Vertex AI](build-with-claude._claude-on-vertex-ai.md)
* APIs
  * [Administration API](build-with-claude._administration-api.md)
  * [Usage Cost API](build-with-claude._usage-cost-api.md)
  * [Claude Code Analytics API](build-with-claude._claude-code-analytics-api.md)

## Agents and Tools
* Tool Use
  * [Overview](agents-and-tools._tool-use_overview.md)
  * [Implement tool use](agents-and-tools._tool-use_implement-tool-use.md)
  * Built-in Tools
    * [Computer use tool](agents-and-tools._tool-use_computer-use-tool.md)
    * [Bash tool](agents-and-tools._tool-use_bash-tool.md)
    * [Text editor tool](agents-and-tools._tool-use_text-editor-tool.md)
    * [Code execution tool](agents-and-tools._tool-use_code-execution-tool.md)
    * [Memory tool](agents-and-tools._tool-use_memory-tool.md)
    * [Web search tool](agents-and-tools._tool-use_web-search-tool.md)
    * [Web fetch tool](agents-and-tools._tool-use_web-fetch-tool.md)
  * Advanced
    * [Fine-grained tool streaming](agents-and-tools._tool-use_fine-grained-tool-streaming.md)
    * [Token efficient tool use](agents-and-tools._tool-use_token-efficient-tool-use.md)
* Agent Skills
  * [Overview](agents-and-tools._agent-skills_overview.md)
  * [Quickstart](agents-and-tools._agent-skills_quickstart.md)
  * [Best practices](agents-and-tools._agent-skills_best-practices.md)
* MCP Integration
  * [MCP Connector](agents-and-tools._mcp-connector.md)
  * [Remote MCP servers](agents-and-tools._remote-mcp-servers.md)
* [Claude for Sheets](agents-and-tools._claude-for-sheets.md)

## Agent SDK
* [Overview](agent-sdk._overview.md)
* Language Support
  * [Python](agent-sdk._python.md)
  * [TypeScript](agent-sdk._typescript.md)
* Core Concepts
  * [Custom tools](agent-sdk._custom-tools.md)
  * [Skills](agent-sdk._skills.md)
  * [Slash commands](agent-sdk._slash-commands.md)
  * [Subagents](agent-sdk._subagents.md)
  * [Sessions](agent-sdk._sessions.md)
  * [Plugins](agent-sdk._plugins.md)
* Integration
  * [MCP](agent-sdk._mcp.md)
  * [Permissions](agent-sdk._permissions.md)
* Advanced
  * [Cost tracking](agent-sdk._cost-tracking.md)
  * [Todo tracking](agent-sdk._todo-tracking.md)
  * [Modifying system prompts](agent-sdk._modifying-system-prompts.md)
  * [Streaming vs single mode](agent-sdk._streaming-vs-single-mode.md)
  * [Hosting](agent-sdk._hosting.md)

## Test & Evaluate
* [Define success](test-and-evaluate._define-success.md)
* [Develop tests](test-and-evaluate._develop-tests.md)
* [Eval tool](test-and-evaluate._eval-tool.md)
* Strengthen Guardrails
  * [Increase consistency (JSON mode)](test-and-evaluate._strengthen-guardrails_increase-consistency.md)
  * [Reduce hallucinations](test-and-evaluate._strengthen-guardrails_reduce-hallucinations.md)
  * [Keep Claude in character](test-and-evaluate._strengthen-guardrails_keep-claude-in-character.md)
  * [Mitigate jailbreaks](test-and-evaluate._strengthen-guardrails_mitigate-jailbreaks.md)
  * [Reduce prompt leak](test-and-evaluate._strengthen-guardrails_reduce-prompt-leak.md)
  * [Handle streaming refusals](test-and-evaluate._strengthen-guardrails_handle-streaming-refusals.md)
  * [Reduce latency](test-and-evaluate._strengthen-guardrails_reduce-latency.md)

## API Reference
* [Overview](api.overview.md)
* [Client SDKs](api.client-sdks.md)
* [OpenAI SDK](api.openai-sdk.md)
* [Beta headers](api.beta-headers.md)
* [Versioning](api.versioning.md)
* [Errors](api.errors.md)
* [Rate limits](api.rate-limits.md)
* [Service tiers](api.service-tiers.md)
* [IP addresses](api.ip-addresses.md)
* [Supported regions](api.supported-regions.md)
* Messages
  * [Messages](api.messages.md)
  * [Count tokens](api.messages-count-tokens.md)
* Models
  * [Models](api.models.md)
  * [List models](api.models-list.md)
* Files
  * [Create file](api.files-create.md)
  * [List files](api.files-list.md)
  * [Get file metadata](api.files-metadata.md)
  * [Get file content](api.files-content.md)
  * [Delete file](api.files-delete.md)
* Message Batches
  * [Creating message batches](api.creating-message-batches.md)
  * [Listing message batches](api.listing-message-batches.md)
  * [Retrieving message batches](api.retrieving-message-batches.md)
  * [Retrieving message batch results](api.retrieving-message-batch-results.md)
  * [Canceling message batches](api.canceling-message-batches.md)
  * [Deleting message batches](api.deleting-message-batches.md)
* Admin API
  * Organization
    * [Get me](api.admin-api_organization_get-me.md)
  * Users
    * [List users](api.admin-api_users_list-users.md)
    * [Get user](api.admin-api_users_get-user.md)
    * [Update user](api.admin-api_users_update-user.md)
    * [Remove user](api.admin-api_users_remove-user.md)
  * Workspaces
    * [List workspaces](api.admin-api_workspaces_list-workspaces.md)
    * [Get workspace](api.admin-api_workspaces_get-workspace.md)
    * [Create workspace](api.admin-api_workspaces_create-workspace.md)
    * [Update workspace](api.admin-api_workspaces_update-workspace.md)
    * [Archive workspace](api.admin-api_workspaces_archive-workspace.md)
  * Workspace Members
    * [List workspace members](api.admin-api_workspace_members_list-workspace-members.md)
    * [Get workspace member](api.admin-api_workspace_members_get-workspace-member.md)
    * [Create workspace member](api.admin-api_workspace_members_create-workspace-member.md)
    * [Update workspace member](api.admin-api_workspace_members_update-workspace-member.md)
    * [Delete workspace member](api.admin-api_workspace_members_delete-workspace-member.md)
  * Invites
    * [List invites](api.admin-api_invites_list-invites.md)
    * [Get invite](api.admin-api_invites_get-invite.md)
    * [Create invite](api.admin-api_invites_create-invite.md)
    * [Delete invite](api.admin-api_invites_delete-invite.md)
  * API Keys
    * [List API keys](api.admin-api_apikeys_list-api-keys.md)
    * [Get API key](api.admin-api_apikeys_get-api-key.md)
    * [Update API key](api.admin-api_apikeys_update-api-key.md)
  * Usage & Cost
    * [Get cost report](api.admin-api_usage-cost_get-cost-report.md)
    * [Get messages usage report](api.admin-api_usage-cost_get-messages-usage-report.md)
  * Claude Code
    * [Get Claude Code usage report](api.admin-api_claude-code_get-claude-code-usage-report.md)
* Skills API
  * [List skills](api.skills_list-skills.md)
  * [Get skill](api.skills_get-skill.md)
  * [Create skill](api.skills_create-skill.md)
  * [Delete skill](api.skills_delete-skill.md)
  * [List skill versions](api.skills_list-skill-versions.md)
  * [Get skill version](api.skills_get-skill-version.md)
  * [Create skill version](api.skills_create-skill-version.md)
  * [Delete skill version](api.skills_delete-skill-version.md)
* Prompt Tools
  * [Generate prompt](api.prompt-tools-generate.md)
  * [Improve prompt](api.prompt-tools-improve.md)
  * [Templatize prompt](api.prompt-tools-templatize.md)
* Migration
  * [Migrating from Text Completions to Messages](api.migrating-from-text-completions-to-messages.md)

## Resources
* [Overview](resources.overview.md)
* Prompt Library
  * [Library](resources.prompt-library.library.md)
  * [Cosmic Keystrokes](resources.prompt-library.cosmic-keystrokes.md)
  * [Adaptive Editor](prompt-library._adaptive-editor.md)
  * [Airport Code Analyst](prompt-library._airport-code-analyst.md)
  * [Alien Anthropologist](prompt-library._alien-anthropologist.md)
  * [Alliteration Alchemist](prompt-library._alliteration-alchemist.md)
  * [Babel's Broadcasts](prompt-library._babels-broadcasts.md)
  * [Brand Builder](prompt-library._brand-builder.md)
  * [Career Coach](prompt-library._career-coach.md)
  * [Cite Your Sources](prompt-library._cite-your-sources.md)
  * [Code Clarifier](prompt-library._code-clarifier.md)
  * [Code Consultant](prompt-library._code-consultant.md)
  * [Corporate Clairvoyant](prompt-library._corporate-clairvoyant.md)
  * [CSV Converter](prompt-library._csv-converter.md)
  * [Culinary Creator](prompt-library._culinary-creator.md)
  * [Data Organizer](prompt-library._data-organizer.md)
  * [Direction Decoder](prompt-library._direction-decoder.md)
  * [Dream Interpreter](prompt-library._dream-interpreter.md)
  * [Efficiency Estimator](prompt-library._efficiency-estimator.md)
  * [Email Extractor](prompt-library._email-extractor.md)
  * [Emoji Encoder](prompt-library._emoji-encoder.md)
  * [Ethical Dilemma Navigator](prompt-library._ethical-dilemma-navigator.md)
  * [Excel Formula Expert](prompt-library._excel-formula-expert.md)
  * [Function Fabricator](prompt-library._function-fabricator.md)
  * [Futuristic Fashion Advisor](prompt-library._futuristic-fashion-advisor.md)
  * [Git Gud](prompt-library._git-gud.md)
  * [Google Apps Scripter](prompt-library._google-apps-scripter.md)
  * [Grading Guru](prompt-library._grading-guru.md)
  * [Grammar Genie](prompt-library._grammar-genie.md)
  * [HAL the Humorous Helper](prompt-library._hal-the-humorous-helper.md)
  * [Idiom Illuminator](prompt-library._idiom-illuminator.md)
  * [Interview Question Crafter](prompt-library._interview-question-crafter.md)
  * [LaTeX Legend](prompt-library._latex-legend.md)
  * [Lesson Planner](prompt-library._lesson-planner.md)
  * [Master Moderator](prompt-library._master-moderator.md)
  * [Meeting Scribe](prompt-library._meeting-scribe.md)
  * [Memo Maestro](prompt-library._memo-maestro.md)
  * [Mindfulness Mentor](prompt-library._mindfulness-mentor.md)
  * [Mood Colorizer](prompt-library._mood-colorizer.md)
  * [Motivational Muse](prompt-library._motivational-muse.md)
  * [Neologism Creator](prompt-library._neologism-creator.md)
  * [Perspectives Ponderer](prompt-library._perspectives-ponderer.md)
  * [Philosophical Musings](prompt-library._philosophical-musings.md)
  * [PII Purifier](prompt-library._pii-purifier.md)
  * [Polyglot Superpowers](prompt-library._polyglot-superpowers.md)
  * [Portmanteau Poet](prompt-library._portmanteau-poet.md)
  * [Product Naming Pro](prompt-library._product-naming-pro.md)
  * [Prose Polisher](prompt-library._prose-polisher.md)
  * [Pun Dit](prompt-library._pun-dit.md)
  * [Python Bug Buster](prompt-library._python-bug-buster.md)
  * [Review Classifier](prompt-library._review-classifier.md)
  * [Riddle Me This](prompt-library._riddle-me-this.md)
  * [Sci-Fi Scenario Simulator](prompt-library._sci-fi-scenario-simulator.md)
  * [Second Grade Simplifier](prompt-library._second-grade-simplifier.md)
  * [Simile Savant](prompt-library._simile-savant.md)
  * [Socratic Sage](prompt-library._socratic-sage.md)
  * [Spreadsheet Sorcerer](prompt-library._spreadsheet-sorcerer.md)
  * [SQL Sorcerer](prompt-library._sql-sorcerer.md)
  * [Storytelling Sidekick](prompt-library._storytelling-sidekick.md)
  * [Time Travel Consultant](prompt-library._time-travel-consultant.md)
  * [Tongue Twister](prompt-library._tongue-twister.md)
  * [Trivia Generator](prompt-library._trivia-generator.md)
  * [Tweet Tone Detector](prompt-library._tweet-tone-detector.md)
  * [VR Fitness Innovator](prompt-library._vr-fitness-innovator.md)
  * [Website Wizard](prompt-library._website-wizard.md)

## Release Notes
* [Release notes](release-notes.md)
* [System prompts](release-notes.system-prompts.md)

---

# Claude Code
https://code.claude.com/docs

TODO: check if it's right the split in subsections

## Getting Started
* [Overview](claude.code.overview.md)
* [Quickstart](claude.code.quickstart.md)
* [Common workflows](claude.code.common-workflows.md)

## Configuration
* [Settings](claude.code.settings.md)
* [Model config](claude.code.model-config.md)
* [Terminal config](claude.code.terminal-config.md)
* [Network config](claude.code.network-config.md)
* [Output styles](claude.code.output-styles.md)
* [Statusline](claude.code.statusline.md)
* [Memory](claude.code.memory.md)

## Build with Claude Code
* [MCP](claude.code.mcp.md)
* [Skills](claude.code.skills.md)
* [Slash commands](claude.code.slash-commands.md)
* [Sub-agents](claude.code.sub-agents.md)
* [Hooks](claude.code.hooks.md)
* [Hooks guide](claude.code.hooks-guide.md)
* [Plugins](claude.code.plugins.md)
* [Plugins reference](claude.code.plugins-reference.md)
* [Plugin marketplaces](claude.code.plugin-marketplaces.md)

## Platforms & Integrations
* [VS Code](claude.code.vs-code.md)
* [JetBrains](claude.code.jetbrains.md)
* [Interactive mode](claude.code.interactive-mode.md)
* [Headless mode](claude.code.headless.md)
* [Devcontainer](claude.code.devcontainer.md)
* [Claude Code on the web](claude.code.claude-code-on-the-web.md)

## Deployment
* [Third-party integrations overview](claude.code.third-party-integrations.md)
* Cloud Platforms
  * [Amazon Bedrock](claude.code.amazon-bedrock.md)
  * [Azure AI Foundry](claude.code.azure-ai-foundry.md)
  * [Google Vertex AI](claude.code.google-vertex-ai.md)
* CI/CD
  * [GitHub Actions](claude.code.github-actions.md)
  * [GitLab CI/CD](claude.code.gitlab-ci-cd.md)
* [LLM Gateway](claude.code.llm-gateway.md)

## Administration
* [Advanced installation (Setup)](claude.code.setup.md)
* [IAM](claude.code.iam.md)
* [Security](claude.code.security.md)
* [Sandboxing](claude.code.sandboxing.md)
* [Monitoring usage](claude.code.monitoring-usage.md)
* [Costs](claude.code.costs.md)
* [Analytics](claude.code.analytics.md)
* [Data usage](claude.code.data-usage.md)
* [Checkpointing](claude.code.checkpointing.md)

## SDK
* [Migration guide](claude.code.sdk_migration-guide.md)

## Reference
* [CLI reference](claude.code.cli-reference.md)

## Resources
* [Troubleshooting](claude.code.troubleshooting.md)
* [Legal and compliance](claude.code.legal-and-compliance.md)

---

## External Resources
* [MCP (Model Context Protocol)](https://github.com/dancer1325/mcp-modelcontextprotocol)