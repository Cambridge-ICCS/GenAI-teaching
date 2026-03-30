# Examples

## Dependencies

Install with:

```bash
pip install -r requirements.txt
```
## Instructions 

In order to run, `hugging-face.py` API keys need to be set up on huggingface:

Then set it in your environment.
```bash
export HF_API_KEY=...
```
This runs a Gemma-2b (google) model locally. 


### Cambridge endpoint example `test_openai.py`

This calls the Cambridge LLM proxy (`https://llm.hpc.cam.ac.uk`), which is OpenAI-compatible. Speak to Cambridge Platforms for an API key on LiteLLM.

Again this needs to be set in your environment: 
```bash
export CAM_API_KEY=...
```
