https://code.claude.com/docs/en/amazon-bedrock.md

# Claude Code | Amazon Bedrock

* goal
  * how to configure Claude Code -- through -- Amazon Bedrock (setup, IAM configuration, and troubleshooting)

## Prerequisites

* AWS account / 
  * has Bedrock access enabled
* | Bedrock,
  * access -- to -- desired Claude models 
* AWS CLI 
  * installed & configured
    * ⚠️if it's the ONLY mechanism / get credentials -> MANDATORY⚠️ 
* IAM permissions

## Setup

### 1. Submit use case details

* ⚠️First-time users of Anthropic models⚠️
  * == 1! time / account

1. | [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/)
   1. Select **Chat/Text playground**
   2. choose any Anthropic model -> you will be prompted -- to -- fill out the use case form

### 2. Configure AWS credentials

#### 2.1 AWS CLI configuration

* `aws configure`

#### 2.2 Environment variables (access key)

```bash  theme={null}
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
export AWS_SESSION_TOKEN=your-session-token
```

#### 2.3 Environment variables (SSO profile)

```bash  theme={null}
aws sso login --profile=<your-profile-name>

export AWS_PROFILE=your-profile-name
```

#### 2.4 Bedrock API keys

```bash  theme={null}
export AWS_BEARER_TOKEN_BEDROCK=your-bedrock-api-key
```

* benefits
  * simpler authentication
    * Reason:🧠NO need FULL AWS credentials🧠
* [MORE](https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/)

#### Advanced credential configuration

* AUTOMATIC credential refresh
  * ALLOWED |
    * AWS SSO
    * corporate identity providers

* add these settings | your [Claude Code settings](claude.code.settings.md)

* if Claude Code detects that your AWS credentials are expired (locally -- based on -- their timestamp OR Bedrock returns a credential error) -> BEFORE retrying the request, obtain NEW credentials -- AUTOMATICALLY running -- your configured `awsAuthRefresh` &/OR `awsCredentialExport` commands  

* _Example configuration:_

  ```json  theme={null}
  {
    "awsAuthRefresh": "aws sso login --profile myprofile",
    "env": {
      "AWS_PROFILE": "myprofile"
    }
  }
  ```

### 3. Configure Claude Code

* environment variables / enable Bedrock

  ```bash  theme={null}
  # Enable Bedrock integration
  export CLAUDE_CODE_USE_BEDROCK=1
  
  export AWS_REGION=us-east-1  # or your preferred region
  # required -- Reason:🧠Claude Code does NOT read from the ".aws"🧠 --
  
  # Optional: Override the region for the small/fast model (Haiku)
  export ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION=us-west-2
  ```

* | **VS Code Extension users**
  * [configure environment variables | VS Code extension settings](claude.code.vs-code.md#using-third-party-providers)
    * ⚠️!= export them in your shell⚠️

* `/login` & `/logout` commands
  * ⚠️are disabled⚠️
    * Reason:🧠authentication is handled -- through -- AWS credentials🧠

* You can use settings files for environment variables like `AWS_PROFILE` that you don't want to leak to other processes
* See [Settings](/en/settings) for more information.

### 4. Model configuration

Claude Code uses these default models for Bedrock:

| Model type       | Default value                                      |
| :--------------- | :------------------------------------------------- |
| Primary model    | `global.anthropic.claude-sonnet-4-5-20250929-v1:0` |
| Small/fast model | `us.anthropic.claude-haiku-4-5-20251001-v1:0`      |

<Note>
  For Bedrock users, Claude Code will not automatically upgrade from Haiku 3.5 to Haiku 4.5. To manually switch to a newer Haiku model, set the `ANTHROPIC_DEFAULT_HAIKU_MODEL` environment variable to the full model name (e.g., `us.anthropic.claude-haiku-4-5-20251001-v1:0`).
</Note>

To customize models, use one of these methods:

```bash  theme={null}
# Using inference profile ID
export ANTHROPIC_MODEL='global.anthropic.claude-sonnet-4-5-20250929-v1:0'
export ANTHROPIC_SMALL_FAST_MODEL='us.anthropic.claude-haiku-4-5-20251001-v1:0'

# Using application inference profile ARN
export ANTHROPIC_MODEL='arn:aws:bedrock:us-east-2:your-account-id:application-inference-profile/your-model-id'

# Optional: Disable prompt caching if needed
export DISABLE_PROMPT_CACHING=1
```

<Note>
  [Prompt caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching) may not be available in all regions
</Note>

### 5. Output token configuration

When using Claude Code with Amazon Bedrock, we recommend the following token settings:

```bash  theme={null}
# Recommended output token settings for Bedrock
export CLAUDE_CODE_MAX_OUTPUT_TOKENS=4096
export MAX_THINKING_TOKENS=1024
```

**Why these values:**

* **`CLAUDE_CODE_MAX_OUTPUT_TOKENS=4096`**: Bedrock's burndown throttling logic sets a minimum of 4096 tokens as the max\_token penalty. Setting this lower won't reduce costs but may cut off long tool uses, causing the Claude Code agent loop to fail persistently. Claude Code typically uses less than 4096 output tokens without extended thinking, but may need this headroom for tasks involving significant file creation or Write tool usage.

* **`MAX_THINKING_TOKENS=1024`**: This provides space for extended thinking without cutting off tool use responses, while still maintaining focused reasoning chains. This balance helps prevent trajectory changes that aren't always helpful for coding tasks specifically.

## IAM configuration

Create an IAM policy with the required permissions for Claude Code:

```json  theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowModelAndInferenceProfileAccess",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListInferenceProfiles"
      ],
      "Resource": [
        "arn:aws:bedrock:*:*:inference-profile/*",
        "arn:aws:bedrock:*:*:application-inference-profile/*",
        "arn:aws:bedrock:*:*:foundation-model/*"
      ]
    },
    {
      "Sid": "AllowMarketplaceSubscription",
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:ViewSubscriptions",
        "aws-marketplace:Subscribe"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:CalledViaLast": "bedrock.amazonaws.com"
        }
      }
    }
  ]
}
```

For more restrictive permissions, you can limit the Resource to specific inference profile ARNs.

For details, see [Bedrock IAM documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html).

<Note>
  We recommend creating a dedicated AWS account for Claude Code to simplify cost tracking and access control.
</Note>

## Troubleshooting
* Problem1: region issues
  * Solution1: switch to a region / supports the model
    * `aws bedrock list-inference-profiles --region your-region`
      * check model availability 
    * `export AWS_REGION=us-east-1`
      * switch to a supported region
  * Solution2: use [inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html) / cross-region access

* Problem2: "on-demand throughput isn’t supported"
  * Solution: specify the model -- as an -- [inference profile ID](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)

* Claude Code
  * uses
    * Bedrock [Invoke API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) 
  * NOT support
    * Bedrock Converse API

## Additional resources

* [Bedrock documentation](https://docs.aws.amazon.com/bedrock/)
* [Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
* [Bedrock inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)
* [Claude Code on Amazon Bedrock: Quick Setup Guide](https://community.aws/content/2tXkZKrZzlrlu0KfH8gST5Dkppq/claude-code-on-amazon-bedrock-quick-setup-guide)- [Claude Code Monitoring Implementation (Bedrock)](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock/blob/main/assets/docs/MONITORING.md)
