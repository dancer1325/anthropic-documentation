https://docs.anthropic.com/en/docs/claude-code/third-party-integrations

# Enterprise deployment overview

* goal
  * how Claude Code can integrate -- with -- MULTIPLE 
    * third-party services
    * third-party infrastructure

* deployment option
  * == 👀how to provide Claude Code -- through -- third party👀

## Provider comparison

| Feature             | Anthropic                                                            | Amazon Bedrock                                                                                   | Google Vertex AI                                                                              | Azure AI Foundry                                                                                              |
|---------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Regions             | Supported [countries](https://www.anthropic.com/supported-countries) | Multiple AWS [regions](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) | Multiple GCP [regions](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations) | Multiple Azure [regions](https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/) |
| Prompt caching      | Enabled by default                                                   | Enabled by default                                                                               | Enabled by default                                                                            | Enabled by default                                                                                            |
| Authentication      | API key                                                              | AWS credentials (IAM)                                                                            | GCP credentials (OAuth/Service Account)                                                       | API key or Microsoft Entra ID                                                                                 |
| Cost tracking       | Dashboard                                                            | AWS Cost Explorer                                                                                | GCP Billing                                                                                   | Azure Cost Management                                                                                         |
| Enterprise features | Teams, usage monitoring                                              | IAM policies, CloudTrail                                                                         | IAM roles, Cloud Audit Logs                                                                   | RBAC policies, Azure Monitor                                                                                  |

## Corporate infrastructure

* [Enterprise Network](claude.code.network-config.md)
* [LLM Gateway](claude.code.llm-gateway.md)

## Configuration overview

* allow you to
  * combine DIFFERENT providers & infrastructure
    * [**Corporate proxy**](claude.code.network-config.md)
    * **LLM Gateway**
      * configured -- via --
        * `ANTHROPIC_BASE_URL`
        * `ANTHROPIC_BEDROCK_BASE_URL`
        * `ANTHROPIC_VERTEX_BASE_URL`

### Using Bedrock + corporate proxy

* == route Bedrock traffic -- through a -- corporate HTTP/HTTPS proxy

  ```bash
  # Enable Bedrock
  export CLAUDE_CODE_USE_BEDROCK=1
  export AWS_REGION=us-east-1
  
  # Configure corporate proxy
  export HTTPS_PROXY='https://proxy.example.com:8080'
  ```

### Using Bedrock + LLM Gateway

* == gateway service / provides Bedrock-compatible endpoints

  ```bash
  # Enable Bedrock
  export CLAUDE_CODE_USE_BEDROCK=1
  
  # Configure LLM gateway
  export ANTHROPIC_BEDROCK_BASE_URL='https://your-llm-gateway.com/bedrock'
  export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1  # If gateway handles AWS auth
  ```

### Using Vertex AI + corporate proxy

* == route Vertex AI traffic -- through a -- corporate HTTP/HTTPS proxy

  ```bash
  # Enable Vertex
  export CLAUDE_CODE_USE_VERTEX=1
  export CLOUD_ML_REGION=us-east5
  export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id
  
  # Configure corporate proxy
  export HTTPS_PROXY='https://proxy.example.com:8080'
  ```

### Using Vertex AI + LLM Gateway

* Google Vertex AI models + LLM gateway

  ```bash
  # Enable Vertex
  export CLAUDE_CODE_USE_VERTEX=1
  
  # Configure LLM gateway
  export ANTHROPIC_VERTEX_BASE_URL='https://your-llm-gateway.com/vertex'
  export CLAUDE_CODE_SKIP_VERTEX_AUTH=1  # If gateway handles GCP auth
  ```

### Authentication configuration

* TODO:Claude Code uses the `ANTHROPIC_AUTH_TOKEN` for the `Authorization` header when needed
* `SKIP_AUTH` flags (`CLAUDE_CODE_SKIP_BEDROCK_AUTH`, `CLAUDE_CODE_SKIP_VERTEX_AUTH`) 
are used in LLM gateway scenarios where the gateway handles provider authentication.

## How to choose the right deployment configuration?

### Direct provider access

* the simplest setup
* Have existing AWS or GCP infrastructure
* Need provider-native monitoring and compliance

### Corporate proxy

* Have existing corporate proxy requirements
* Need traffic monitoring and compliance
* route all traffic -- through -- specific network paths

### LLM Gateway

* Need usage tracking across teams
* dynamically switch BETWEEN models
* custom rate limiting OR budgets
* centralized authentication management

## Debugging

* use [`claude /status`](claude.code.slash-commands.md)
* set `export ANTHROPIC_LOG=debug`
  * Reason:🧠log requests🧠

## Best practices for organizations

### 1. Invest | documentation & memory

* documentation
  * Reason:🧠enable Claude Code can understands your codebase🧠
  * deploy "CLAUDE.md" files | MULTIPLE levels
    * **Organization-wide**
      * _Example:_ | (macOS), `/Library/Application Support/ClaudeCode/CLAUDE.md`
    * **Repository-level**
      * 's content: 
        * project architecture,
        * build commands,
        * contribution guidelines
      * track into source control
* [memory](claude.code.memory.md)

### 2. Simplify deployment

* TODO: If you have a custom development environment, 
we find that creating a "one click" way to install Claude Code is key to growing adoption across an organization.

### 3. Start with guided usage

Encourage new users to try Claude Code for codebase Q\&A, or on smaller bug fixes or feature requests
Ask Claude Code to make a plan
* Check Claude's suggestions and give feedback if it's off-track
* Over time, as users understand this new paradigm better, then they'll be more effective at letting Claude Code run more agentically.

### 4. Configure security policies

Security teams can configure managed permissions for what Claude Code is and is not allowed to do, which cannot be overwritten by local configuration
* [Learn more](/en/docs/claude-code/security).

### 5. Leverage MCP for integrations

MCP is a great way to give Claude Code more information, such as connecting to ticket management systems or error logs
* We recommend that one central team configures MCP servers and checks a `.mcp.json` configuration into the codebase so that all users benefit
* [Learn more](/en/docs/claude-code/mcp).

At Anthropic, we trust Claude Code to power development across every Anthropic codebase
* We hope you enjoy using Claude Code as much as we do!

## Next steps

* [Set up Amazon Bedrock](/en/docs/claude-code/amazon-bedrock) for AWS-native deployment
* [Configure Google Vertex AI](/en/docs/claude-code/google-vertex-ai) for GCP deployment
* [Implement Corporate Proxy](/en/docs/claude-code/corporate-proxy) for network requirements
* [Deploy LLM Gateway](/en/docs/claude-code/llm-gateway) for enterprise management
* [Settings](/en/docs/claude-code/settings) for configuration options and environment variables
