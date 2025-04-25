#!/bin/bash
rsync -av --delete /home/porky/notes/public /home/porky/darthpedro/obsidian-darthpedro/content
python3 images.py
rsync -av --delete /home/porky/notes/public /home/porky/darthpedro/obsidian-darthpedro/content
python3 images.py

hugo server
