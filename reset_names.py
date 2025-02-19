import os

path = "."

i = 1
for filename in os.listdir(path):
    if filename.endswith(".pdf"):
        os.rename(os.path.join(path, filename), os.path.join(path, str(i).zfill(3) + ".pdf"))
        i += 1