# pip install fonttools
from fontTools.ttLib.ttCollection import TTCollection
import os
import sys

filename = sys.argv[1]
ttc = TTCollection(filename)
basename = os.path.basename(filename)
basename_wo_ext = os.path.splitext(basename)[0]
for i, font in enumerate(ttc):
    font.save(f"{basename_wo_ext}-{i}.ttf")

