import subprocess

subprocess.run("magick convert *.gif -set filename:base \"%[basename]\" \"%[filename:base].jpg\"")