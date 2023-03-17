import yaml

class GeneratorConfig:
    def __init__(self):
        self.models = None
        self.config = None
        self.init()

    def init(self):
        with open("./models.yaml") as f:
            self.models = yaml.load(f, Loader=yaml.SafeLoader)
