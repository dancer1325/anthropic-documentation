import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY
});

const response = await client.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    betas: ["structured-outputs-2025-11-13"],
    messages: [
        {
            role: "user",
            content: "What's the weather like in San Francisco?"
        }
    ],
    tools: [{
        name: "get_weather",
        description: "Get the current weather in a given location",
        strict: true,  // Enable strict mode
        input_schema: {
            type: "object",
            properties: {
                location: {
                    type: "string",
                    description: "The city and state, e.g. San Francisco, CA"
                },
                unit: {
                    type: "string",
                    enum: ["celsius", "fahrenheit"]
                }
            },
            required: ["location"],
            additionalProperties: false
        }
    }]
});
console.log(response.content);