from collections import OrderedDict
from flask import Flask, jsonify, render_template, request, abort
import yaml
import time
import os
import logging
import logging.config
from generator import GeneratorFactory, GeneratorConfig

logging.config.fileConfig("logging.conf")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

APP_NAME = "BLOOM"

app = Flask(__name__)
config = GeneratorConfig()

@app.route("/", defaults={"path": ""})
def index(path):
    return render_template("index.html" )


@app.before_request
def before_request():
    request.start_time = time.time()


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
    return response

@app.route("/healthz")
def health():
    generator = GeneratorFactory(config['bloom-560m'])
    text = generator.generate(["Hi, How are you?"])
    return "" if len(text) and len(text[0]) else False


@app.route("/api/generate/<model>", methods=["POST"])
def generate_handler(model):
    prompt = request.json.get("prompt")
    if len(prompt) > 10000:
        abort(
            413,
            description="Request too large to handle. Maximum 10000 characters are supported.",
        )
    prompt = prompt.strip()
    start = time.time()
    generator = GeneratorFactory(config, model)

    if not generator:
        abort(400, description="Could not find generator for the model.")

    generated_text = generator.generate(prompt)
    end = time.time()
    generationtime = end - start
    return jsonify(
        generatedtext=generated_text,
        generationtime=generationtime,
        model=model,
    )
