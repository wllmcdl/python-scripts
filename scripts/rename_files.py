import os, re

os.chdir('/Users/william/Downloads/flask')

regex = r'Tutorial - (.+?)-[a-zA-z0-9]+?(.mkv|.mp4)'

fnames = os.listdir(".")

for fname in fnames:
    group = re.search(regex, fname)
    if group is None: continue
    new_name = (group.group(1) + group.group(2))
    os.rename(fname, fname.replace(fname, new_name))