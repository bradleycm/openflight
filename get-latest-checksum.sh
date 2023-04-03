#!/bin/bash

# Check if a tag was provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <tag>"
    exit 1
fi

TAG=$1
USER="bradleycm"
REPO="openflight"
URL="https://github.com/$USER/$REPO/archive/refs/tags/$TAG.zip"
OUTPUT="$HOME/Downloads/openflight-$TAG.zip"

# Download the release archive
echo "Downloading release $TAG..."
curl -L -o "$OUTPUT" "$URL"

# Calculate the SHA-256 hash
echo "Calculating SHA-256 hash..."
shasum -a 256 "$OUTPUT"
