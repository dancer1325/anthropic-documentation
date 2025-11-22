https://code.claude.com/docs/en/network-config.md

# Enterprise network configuration

* goal
  * how to configure Claude Code | enterprise environments / have
    * proxy servers,
    * custom Certificate Authorities (CA),
    * mutual Transport Layer Security (mTLS) authentication

* 👀ways to configure environment variables👀
  * `export ENVIRONMENT_VARIABLE_KEY=ENVIRONMENT_VARIABLE_VALUE`
    * == traditional one
  * [settings.json](claude.code.settings.md#settings-files)
    * ⚠️Claude recommended one⚠️

## Proxy configuration

* == HTTP/HTTPS proxy -- for -- routing traffic

### -- via -- Environment variables

* Claude Code
  * respects standard proxy environment variables

    ```bash  theme={null}
    # HTTPS proxy (recommended)
    export HTTPS_PROXY=https://proxy.example.com:8080
    
    # HTTP proxy (if HTTPS not available)
    export HTTP_PROXY=http://proxy.example.com:8080
    
    # Bypass proxy for specific requests - space-separated format
    export NO_PROXY="localhost 192.168.1.1 example.com .example.com"
    # Bypass proxy for specific requests - comma-separated format
    export NO_PROXY="localhost,192.168.1.1,example.com,.example.com"
    # Bypass proxy for all requests
    export NO_PROXY="*"
    ```
  * ❌does NOT support SOCKS proxies❌

### Basic authentication

* use case
  * proxy / requires basic authentication
* steps
  * include credentials | proxy URL

    ```bash  theme={null}
    export HTTPS_PROXY=http://username:password@proxy.example.com:8080
    ```
    * recommendations
      * | scripts, 
        * ❌NOT hardcode passwords❌
      * use 
        * environment variables, OR
        * secure credential storage

* recommendations
  * 👀if proxies require advanced authentication (NTLM, Kerberos, etc.) -> use an LLM Gateway service / supports your authentication method👀

## Custom CA certificates

* uses
  * enterprise environment uses custom CAs -- for -- HTTPS connections (either proxy OR direct API)

```bash  theme={null}
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
```

## mTLS authentication

For enterprise environments requiring client certificate authentication:

```bash  theme={null}
# Client certificate for authentication
export CLAUDE_CODE_CLIENT_CERT=/path/to/client-cert.pem

# Client private key
export CLAUDE_CODE_CLIENT_KEY=/path/to/client-key.pem

# Optional: Passphrase for encrypted private key
export CLAUDE_CODE_CLIENT_KEY_PASSPHRASE="your-passphrase"
```

## Network access requirements

Claude Code requires access to the following URLs:

* `api.anthropic.com` - Claude API endpoints
* `claude.ai` - WebFetch safeguards
* `statsig.anthropic.com` - Telemetry and metrics
* `sentry.io` - Error reporting

Ensure these URLs are allowlisted in your proxy configuration and firewall rules. This is especially important when using Claude Code in containerized or restricted network environments.

## Additional resources

* [Claude Code settings](/en/settings)
* [Environment variables reference](claude.code.settings.md)
* [Troubleshooting guide](/en/troubleshooting)
