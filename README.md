# GenAI-teaching

Slides are rendered [here](https://cambridge-iccs.github.io/GenAI-teaching).

## Build dependencies

- [Quarto](https://quarto.org/docs/get-started/)

The required Quarto extensions can be installed with:

```bash
quarto add --no-prompt quarto-ext/attribution
quarto add --no-prompt jmbuhr/quarto-qrcode
quarto add --no-prompt quarto-ext/pointer
```

Then render with:

```bash
quarto render genai-teaching.qmd
```
