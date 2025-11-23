https://docs.claude.com/en/docs/about-claude/models/choosing-a-model.md

# Choosing the right model

* goal
  * how to choose the right Claude model

## Establish key criteria

* | choose a Claude model,
  * factors / take in account
    - **Capabilities:**
      - == model's features OR capabilities / meet your needs
    - **Speed:**
    - **Cost:**
      - == your budget

## Choose the best model to start with

* approaches | choose the best Claude model

### Option 1: Start with a fast, cost-effective model

* == use Claude Haiku 4.5

* steps
  1. Test your use case thoroughly
  2. Evaluate if performance meets your requirements
  3. ONLY if necessary for specific capability gaps -> ugrade 

* use cases
  - Initial prototyping and development
  - Applications with tight latency requirements
  - Cost-sensitive implementations
  - High-volume, straightforward tasks

### Option 2: Start with the most capable model

* == use Claude Sonnet 4.5 

* steps 
  1. Optimize your prompts
  2. Evaluate if performance meets your requirements
  3. Consider increasing efficiency by downgrading intelligence over time with greater workflow optimization

* use cases
  - Complex reasoning tasks
  - Scientific or mathematical applications
  - Tasks requiring nuanced understanding
  - Applications where accuracy outweighs cost considerations
  - Advanced coding

## Model selection matrix

TODO:

| When you need... | We recommend starting with... | Example use cases |
|------------------|-------------------|-------------------|
| Best model for complex agents and coding, highest intelligence across most tasks, superior tool orchestration for long-running autonomous tasks | Claude Sonnet 4.5 | Autonomous coding agents, cybersecurity automation, complex financial analysis, multi-hour research tasks, multi agent frameworks |
| Exceptional intelligence and reasoning for specialized complex tasks | Claude Opus 4.1 | Highly complex codebase refactoring, nuanced creative writing, specialized scientific analysis |
| Near-frontier performance with lightning-fast speed and extended thinking - our fastest and most intelligent Haiku model at the most economical price point | Claude Haiku 4.5 | Real-time applications, high-volume intelligent processing, cost-sensitive deployments needing strong reasoning, sub-agent tasks |

## Decide whether to upgrade OR change models

1. [Create benchmark tests](/docs/en/test-and-evaluate/develop-tests) specific to your use case - having a good evaluation set is the most important step in the process
2. Test with your actual prompts and data
3. Compare performance across models for:
   - Accuracy of responses
   - Response quality
   - Handling of edge cases
4. Weigh performance and cost tradeoffs

## Next steps

<CardGroup cols={3}>
  <Card title="Model comparison chart" icon="settings" href="/docs/en/about-claude/models/overview">
    See detailed specifications and pricing for the latest Claude models
  </Card>
  <Card title="What's new in Claude 4.5" icon="sparkle" href="/docs/en/about-claude/models/whats-new-claude-4-5">
    Explore the latest improvements in Claude 4.5 models
  </Card>
  <Card title="Start building" icon="code" href="/docs/en/get-started">
    Get started with your first API call
  </Card>
</CardGroup>