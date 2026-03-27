# Demo MCP server

## Installation

To use our new MCP servers with `opencode` we first need to register them. This can be done with the `mcp add` command

```
opencode mcp add
```

This will launch an interactive CLI which will help you configure the MCP server.

```
$ opencode mcp add
┌  Add MCP server
│
◆  Location
│  ● Current project (path/to/GenAI-teaching/opencode.json)
│  ○ Global
└
```

You can add it for the current project only, or add it to your global config. For now, let's just use it for this project i.e.,
press `[Enter]`.

> [!NOTE]
> On your system the current project path to `GenAI-teaching/opencode.json` will be different.

```
┌  Add MCP server
│
◇  Location
│  Current project
│
◆  Enter MCP server name
│  _
└
```

We can choose any name, this is how it will be displayed in `opencode`. Let's use `numbers`.

> [!NOTE]
> The name you give here is important as it will provide context to the LLM as to what your tool can be used for. So give it a
> meaningful name. In addition, each tool will get a name as follows `[servername]_[toolname]`. For example, in `mcp-numbers.py`
> the tool is called `add`. So if we call the server `numbers` the MCP tool will get the name `numbers_add` in `opencode`.

```
┌  Add MCP server
│
◇  Location
│  Current project
│
◇  Enter MCP server name
│  numbers
│
◆  Select MCP server type
│  ● Local (Run a local command)
│  ○ Remote
└
```

For this example, both of our MCP servers are running on our local machine, so press `[Enter]` to pick `Local`.

```
┌  Add MCP server
│
◇  Location
│  Current project
│
◇  Enter MCP server name
│  numbers
│
◇  Select MCP server type
│  Local
│
◆  Enter command to run
│  e.g., opencode x @modelcontextprotocol/server-filesystem
└
```

Here we will enter the command that is used to launch our server. Because we are using the python library `fastMCP`, we need to
use a python command to run it. I prefer to use `uv` for this kind of thing, but you can just as equally use a virtual
environment. Feel free to use either method described below.

### `uv` (simpler/recommended)

If you have `uv` already installed, you can simply pass the following command into `opencode`'s MCP CLI configuration tool

```
uv run --directory absolute/path/to/GenAI-teaching/mcp mcp-add.py
```

> [!NOTE]
> I recommend giving the full absolute path of the server `mcp-add.py` to prevent errors when launching from other directories.

So it will looks something like this:

```
┌  Add MCP server
│
◇  Location
│  Current project
│
◇  Enter MCP server name
│  numbers
│
◇  Select MCP server type
│  Local
│
◇  Enter command to run
│  uv run --directory absolute/path/to/GenAI-teaching/mcp mcp-add.py
│
◆  MCP server "numbers" added to path/to/GenAI-teaching/opencode.json
│
└  MCP server added successfully
```

### Python virtual environment

First create a python virtual environment (if you haven't already).

```
python3 -m venv .genai
```

Activate the environment

```
source .genai/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Now we can pass the following command into `opencode`'s MCP CLI configuration tool

```
path/to/.genai/bin/python path/to/mcp-numbers.py
```

> [!NOTE]
> I recommend giving the full absolute path to your virtual environment (`.genai`) and the mcp server (`mcp-numbers.py`) to
> prevent errors when launching from other directories.

So it will looks something like this:

```
┌  Add MCP server
│
◇  Location
│  Current project
│
◇  Enter MCP server name
│  numbers
│
◇  Select MCP server type
│  Local
│
◇  Enter command to run
│  path/to/.genai/bin/python path/to/mcp-numbers.py
│
◆  MCP server "numbers" added to path/to/GenAI-teaching/opencode.json
│
└  MCP server added successfully
```

## Validation

You should see `MCP server added successfully`. To verify it is working we will run opencode and check which MCP servers are
running.
