#!/bin/bash

FIRMWALL_DIR="$PWD"
ZEPHYR_DIR="/home/aruna/Documents/Zephyr"
TFM_DIR=zephyr/samples/tfm_integration
BOARD=mps2_an521_ns

echo This script build the tf-m reference applications on zephyre os and coby the build binary and the sources to firmwall binary folder
echo This script requires working ZEPHYR building environement

cd "$ZEPHYR_DIR"


echo "$PWD"
echo copying TF-M implementations
cp -r  $TFM_DIR $FIRMWALL_DIR

source .venv/bin/activate
# Get subfolders as an array using glob pattern
shopt -s nullglob  # Enable nullglob to handle no match case
subfolders=("$TFM_DIR"/*/)
# Print the subfolders
echo "Subfolders:"
for subfolder in "${subfolders[@]}"; do
    echo "Building $subfolder"
	west build -p auto -b $BOARD $subfolder
	mkdir -p $FIRMWALL_DIR/tfm_integration/$(basename "$subfolder")/bin/
	cp -r build/zephyr/zephyr* $FIRMWALL_DIR/tfm_integration/$(basename "$subfolder")/bin/
	echo "binaries copied"
done



