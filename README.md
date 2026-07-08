<img src="slides/images/UCAM_ICCS_Logo.png"  width="600">

# GenAI-teaching

![GitHub](https://img.shields.io/github/license/Cambridge-ICCS/GenAI-teaching)
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This repository contains documentation, resources, and code for the `GenAI-teaching` session designed and delivered by Tom
Meltzer (@TomMelt) and Matt Archer (@ma595) of [ICCS](https://cambridge-iccs.github.io/) and Cordero Core (@cdcore09) of
[SSEC](https://github.com/uw-ssec). All materials, including slides, are available such that individuals can cover the course in
their own time.

The course slides can be found here [GenAI-teaching](https://cambridge-iccs.github.io/GenAI-teaching).

## Contents

- [Learning Objectives](#learning-objectives)
- [Teaching material](#teaching-material)
- [Preparation and prerequisites](#preparation-and-prerequisites)
- [Installation and setup](#installation-and-setup)
- [License information](#license)
- [Contribution Guidelines and Support](#contribution-guidelines-and-support)

## Learning Objectives

The key learning objective from this workshop is to equip RSEs with a practical understanding of Generative AI, from the
underlying principles to the tools and workflows used today.

More specifically, by the end of the session participants will be able to:

### Conceptual understanding (first half)

* Understand current state-of-play of LLMs and Agents by learning the history of this field
* Understand what transformers are and how transformer models work at inference time
* Understand different agentic workflows
* Recognise the key safety, ethical, and environmental concerns surrounding GenAI

### Practical skills (second half)

* Configure [`opencode`](https://opencode.ai/) to work with self-hosted LLMs
* Build a custom MCP tool
* Create, register, and use an agent `SKILL.md`
* Distinguish between when to use MCP, Skills or CLI
* Create and configure a sub-agent for a specific task

## Teaching Material

### Slides
The slides for this workshop can be viewed here: [GenAI-teaching](https://cambridge-iccs.github.io/GenAI-teaching)

The slides are generated using [Quarto](https://quarto.org/docs/get-started/) from the `genai-teaching.qmd` source file.

## Preparation and prerequisites

### Prerequisites

- No technical knowledge of ML or AI/LLMs is assumed
- No programming knowledge is required
- Familiarity with terminal/bash will be helpful
- a laptop
- a `litellm` key (which will be issued by us on the day)

### Preparation

This course should work just fine on Windows, Linux or Mac.

You will need a terminal, but this normally comes with your default software. You can use:

* Linux - Default terminal for your distro e.g., Gnome Terminal on Debian
* Mac OS - iTerm
* Windows - Powershell

If you require assistance or further information with any of these please reach out to us before the session.

## Installation and setup

We will cover installation instructions during the presentation.

### Obtaining the materials

Clone the repository locally:

```bash
git clone https://github.com/Cambridge-ICCS/GenAI-teaching.git
```

## License

The code materials in this project are licensed under the [MIT License](LICENSE).

The teaching materials are licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

## Contribution Guidelines and Support

If you spot an issue with the materials please let us know by [opening an issue](https://github.com/Cambridge-ICCS/GenAI-teaching/issues) here on GitHub clearly describing the problem.

If you are able to fix an issue that you spot, or an [existing open issue](https://github.com/Cambridge-ICCS/GenAI-teaching/issues) please get in touch by commenting on the issue thread.

Contributions from the community are welcome. To contribute back to the repository please first [fork it](https://github.com/Cambridge-ICCS/GenAI-teaching/fork), make the necessary changes to fix the problem, and then open a pull
request back to this repository clearly describing the changes you have made. We will then perform a review and merge once
ready.

If you would like support using these materials, adapting them to your needs, or delivering them please get in touch either via
GitHub or via one of the communication channels listed [here](https://github.com/Cambridge-ICCS).
