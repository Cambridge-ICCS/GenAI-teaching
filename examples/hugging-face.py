import os
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM

login(token=os.environ["HF_API_KEY"], add_to_git_credential=True)

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")

model = AutoModelForCausalLM.from_pretrained("google/gemma-2b")

input_text = "I went to the"
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids, max_new_tokens=10, do_sample=True, top_p=0.9)
print(tokenizer.decode(outputs[0]))
