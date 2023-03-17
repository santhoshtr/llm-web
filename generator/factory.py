import logging

import logging.config
from generator import BaseGenerator, BloomGenerator, GeneratorConfig

logging.config.fileConfig("logging.conf")

generator_cache={}

def GeneratorFactory(generator_config: GeneratorConfig, model: str) -> BaseGenerator:
    generators = {
        "bloom-560m": BloomGenerator,
        "bloomz-1b7": BloomGenerator,
    }
    if model not in generator_cache:
        generator_cache[model] = generators.get(model)(generator_config.models.get(model));
    return generator_cache[model]


if __name__ == "__main__":
    config = GeneratorConfig()
    print(
        GeneratorFactory(config, "bloom-560m").generate(
           "Hello, My name is "
    )  )

