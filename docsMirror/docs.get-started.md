https://docs.claude.com/en/docs/get-started

# Get started with Claude

* goal
  * make your first API call -- to -- Claude
  * build a simple web search assistant

---

## Prerequisites

- [Anthropic Console account](https://platform.claude.com/)
- [API key](https://platform.claude.com/settings/keys)

## Call the API

### cURL
* steps
  * `export ANTHROPIC_API_KEY='your-api-key-here'`
  * curl / create a simple web search assistant

### Python
* steps
  * `export ANTHROPIC_API_KEY='your-api-key-here'`
  * `pip install anthropic`
  * `python3 getStarted.py`

### TypeScript
* steps
  * `export ANTHROPIC_API_KEY='your-api-key-here'`
  * `npm install @anthropic-ai/sdk`
  * `npx tsx quickstart.ts`

### Java
* steps
  * `export ANTHROPIC_API_KEY='your-api-key-here'`
  * install Java SDK
    * | **Gradle:**
          ```groovy
          implementation("com.anthropic:anthropic-java:1.0.0")
          ```
    * | **Maven:**
          ```xml
          <dependency>
            <groupId>com.anthropic</groupId>
            <artifactId>anthropic-java</artifactId>
            <version>1.0.0</version>
          </dependency>
          ```
  * 

    ```bash
    javac App.java
    java App
    ```
