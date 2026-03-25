# GenAI-teaching

Slides are rendered [here](https://cambridge-iccs.github.io/GenAI-teaching).

## Build dependencies

- [Quarto](https://quarto.org/docs/get-started/)
- Python with `jupyter` (`pip install jupyter`)

The required Quarto extensions can be installed with:

```bash
quarto add --no-prompt quarto-ext/attribution
quarto add --no-prompt jmbuhr/quarto-qrcode
```

Then render with:

```bash
QUARTO_PYTHON=venv/bin/python quarto render genai-teaching.qmd
```
