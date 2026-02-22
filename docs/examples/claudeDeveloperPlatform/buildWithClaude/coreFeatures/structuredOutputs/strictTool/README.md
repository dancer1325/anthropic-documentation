**Response format:** Tool use blocks with validated inputs in `response.content[x].input`

```json
{
  "type": "tool_use",
  "name": "get_weather",
  "input": {
    "location": "San Francisco, CA"
  }
}
```

* `input`
  * strictly follows the `input_schema`
* `name`
  * ALWAYS valid (from provided tools or server tools)