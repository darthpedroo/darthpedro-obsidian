#!/bin/bash
./copy-md.sh
python3 images.py
./copy-md.sh
python3 images.py

hugo server
