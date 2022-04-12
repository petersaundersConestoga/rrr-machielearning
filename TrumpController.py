from transformers import AutoModelForCausalLM 
from transformers import AutoTokenizer
from transformers import pipeline 

modelpath = "model/trump"

# get the tokenizer and model to start
def tweet(input = ""):
    tokenizer = AutoTokenizer.from_pretrained(modelpath)
    model = AutoModelForCausalLM.from_pretrained(modelpath)
    generator = pipeline(task="text-generation", model=model, tokenizer=tokenizer)

    generated = generator(input)
    return generated
