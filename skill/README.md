# Skills

## Installation

To "install" skills in opencode, they need to be placed in a specific location.

A list of recognized locations can be found in their [documentation](https://opencode.ai/docs/skills#place-files).

- Project config: `.opencode/skills/<name>/SKILL.md`
- Global config: `~/.config/opencode/skills/<name>/SKILL.md`
- Project Claude-compatible: `.claude/skills/<name>/SKILL.md`
- Global Claude-compatible: `~/.claude/skills/<name>/SKILL.md`
- Project agent-compatible: `.agents/skills/<name>/SKILL.md`
- Global agent-compatible: `~/.agents/skills/<name>/SKILL.md`

For this workshop it doesn't really matter, but as we are using `opencode` only, we shall go with
`.opencode/skills/<name>/SKILL.md` which is the local folder (project config).

So `cd` to the root of the `GenAI-teaching` repo and run the following command:

```bash
mkdir -p .opencode/skills/netcdf
ln -sf $(pwd)/skill/netcdf/SKILL.md .opencode/skills/netcdf/
```

This should now make the netcdf `SKILL.md` available to `opencode`.

To check, run the `/skills` command and you should see it listed.
