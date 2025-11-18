https://docs.anthropic.com/en/docs/claude-code/setup

# Set up Claude Code

* goal
  * | your development machine, about Claude Code,
    * how to 
      * install,
      * authenticate,
      * use 

## System requirements

* **Operating Systems**: macOS 10.15+, Ubuntu 20.04+/Debian 10+, or Windows 10+ (with WSL 1, WSL 2, or Git for Windows)
* **Hardware**: 4GB+ RAM
* **Software**: [Node.js 18+](https://nodejs.org/en/download)
* **Network**: Internet connection
  * Reason:🧠authenticate & AI processing🧠
* **Shell**
  * recommendation
    * Bash,
    * Zsh
    * Fish
* **Location**: [Anthropic supported countries](https://www.anthropic.com/supported-countries)

## Standard installation

```sh
npm install -g @anthropic-ai/claude-code

# check your installation type
claude doctor
```
* recommendations
  * ❌NOT use `sudo npm install -g`❌
    * Reason:🧠it can lead to permission issues & security risks🧠
  * see [troubleshooting](docs.claude-code.troubleshooting.md)

## how to use | your project?

* | your project

    ```bash
    claude
    ```
  * prompt to authenticate
    * -- via -- 
      1. **Anthropic Console**
         1. default option
         2. connect -- through the -- Anthropic Console & complete the OAuth process
         3. requirements
            * | [console.anthropic.com](https://console.anthropic.com), active billing
      2. **Claude App (with Pro or Max plan)**
         1. requirements
            * subscribe | Claude's [Pro or Max plan](https://www.anthropic.com/pricing) / include
              * Claude Code + web interface
         2. steps
            1. log in -- via -- your Claude.ai account
            2. | launch, choose the option / matches your subscription type
      3. **Enterprise platforms**
         1. allows
            * enterprise deployments -- with -- your existing cloud infrastructure
         2. configure Claude Code / use [Amazon Bedrock or Google Vertex AI](docs.claude-code.third-party-integrations.md) 
    * [securely stores your credentials](docs.claude-code.iam.md)

## | Windows, how to setup?

* TODO:
**Option 1: Claude Code within WSL**

* Both WSL 1 and WSL 2 are supported

**Option 2: Claude Code on native Windows with Git Bash**

* Requires [Git for Windows](https://git-scm.com/downloads/win)
* For portable Git installations, specify the path to your `bash.exe`:
  ```powershell
  $env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
  ```

## ALTERNATIVE installation methods

* if you find issues -> see [troubleshooting guide](docs.claude-code.troubleshooting.md)

### Native binary installation (Beta)

* TODO: If you have an existing installation of Claude Code, use `claude install` to start the native binary installation.

For a fresh install, run the following command:

**macOS, Linux, WSL:**

```bash
# Install stable version (default)
curl -fsSL https://claude.ai/install.sh | bash

# Install latest version
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Install specific version number
curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
```

**Windows PowerShell:**

```powershell
# Install stable version (default)
irm https://claude.ai/install.ps1 | iex

# Install latest version
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest

# Install specific version number
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 1.0.58

```

The native Claude Code installer is supported on macOS, Linux, and Windows.

<Tip>
  Make sure that you remove any outdated aliases or symlinks.
  Once your installation is complete, run `claude doctor` to verify the installation.
</Tip>

## | Local installation

* requirements
  * ALREADY installed

* recommendations
  * `claude migrate-installer` + select "Claude Code Local Installer"
    * 👀migrate project memory -- to -- user memory👀
    * Reason:🧠avoids autoupdater npm permission issues🧠

## how to run | AWS or GCP?

* Claude Code
  * by default, uses Anthropic's API
  * if you want to run it | AWS or GCP -> see [third-party integrations](docs.claude-code.third-party-integrations.md)

## how to update Claude Code?

### Auto updates

Claude Code automatically keeps itself up to date to ensure you have the latest features and security fixes.

* **Update checks**: Performed on startup and periodically while running
* **Update process**: Downloads and installs automatically in the background
* **Notifications**: You'll see a notification when updates are installed
* **Applying updates**: Updates take effect the next time you start Claude Code

**Disable auto-updates:**

```bash
# Via configuration
claude config set autoUpdates false --global

# Or via environment variable
export DISABLE_AUTOUPDATER=1
```

### Update manually

```bash
claude update
```
