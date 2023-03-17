import ctranslate2
import transformers

generator = ctranslate2.Generator("models/bloom-560m")
tokenizer = transformers.AutoTokenizer.from_pretrained("bigscience/bloom-560m")

def generate(prompt):
  start_tokens = tokenizer.convert_ids_to_tokens(tokenizer.encode(prompt))
  results = generator.generate_batch([start_tokens], max_length=30, sampling_topk=10)
  return tokenizer.decode(results[0].sequences_ids[0])
prompt="Einstein was born in "
print(generate(prompt))