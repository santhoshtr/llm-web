import logging
import transformers
from typing import List
import logging.config
from .base import BaseGenerator

logging.config.fileConfig("logging.conf")

class BloomGenerator(BaseGenerator):
    def generate(self, prompt):
        start_tokens = self.tokenizer.convert_ids_to_tokens(self.tokenizer.encode(prompt))
        results = self.generator.generate_batch(
            [start_tokens],
            max_length=len(prompt)+100,
            sampling_topk=10
        )
        return self.tokenizer.decode(results[0].sequences_ids[0])
