import ctranslate2
import transformers

model = "models/bloom-560m"
#model = "models/bloomz-1b7"
tokenizer =  "bigscience/bloom-560m"
#tokenizer =  "bigscience/bloomz-1b7"

generator = ctranslate2.Generator(model)
tokenizer = transformers.AutoTokenizer.from_pretrained(tokenizer)

def generate(prompt):
  start_tokens = tokenizer.convert_ids_to_tokens(tokenizer.encode(prompt))
  results = generator.generate_batch(
    [start_tokens],
    max_length=len(prompt)+100,
    sampling_topk=10,
    sampling_temperature=0
  )

  return tokenizer.decode(results[0].sequences_ids[0])

prompt="Sky is blue because "
print(generate(prompt))