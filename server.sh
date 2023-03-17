#!/bin/bash

# Download models
mkdir -p models

echo "Downloading models..."


modelbase=https://people.wikimedia.org/~santhosh/bloom/bloom-560m
wget -N --no-verbose --show-progress --progress=bar:force:noscroll $modelbase/config.json -P models/bloom-560m
wget -N --no-verbose --show-progress --progress=bar:force:noscroll $modelbase/model.bin -P models/bloom-560m
wget -N --no-verbose --show-progress --progress=bar:force:noscroll $modelbase/vocabulary.txt -P models/bloom-560m

echo "Models downloaded. Starting server..."

gunicorn
