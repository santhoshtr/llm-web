from ctranslate2 import Generator
import logging
import transformers
from typing import List
import logging.config

logging.config.fileConfig("logging.conf")

class BaseGenerator:
    def __init__(self, config):
        self.config = config
        self.generator = None
        self.tokenizer = None
        self.init()

    def getGenerator(self) -> Generator:
        return Generator(
            self.config.get("model"),  # Model
            device="auto",
            compute_type="auto",
        )

    def getTokenizer(self):
        raise Exception("Not implemented")

    def init(self):
        self.generator = self.getGenerator()
        self.tokenizer = self.getTokenizer()
        logging.info(f"{self.__class__.__name__} initialized")


    def generate(self, prompt):
        raise Exception("Not implemented")
