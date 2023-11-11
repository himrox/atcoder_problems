import os
import shutil

print("input folder name")
name = input()
path = "Tessoku/" + name

os.mkdir(path)
shutil.copy("template.py", path + "/main.py")
