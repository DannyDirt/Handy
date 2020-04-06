import os
import glob
import os.path



foldername = #os.path.join('/Users/danielruso/PycharmProjects/NEW/100')

found_files = glob.glob(os.path.join(foldername,'*.jpg'), recursive=True)

for root, _, files in os.walk(foldername):
    for f in files:
        fullpath = os.path.join(root, f)
        if f.endswith(' 2.jpg'):
            os.remove(fullpath)
        elif f.endswith(' 3.jpg'):
            os.remove(fullpath)
        elif f.endswith(' 4.jpg'):
            os.remove(fullpath)

print("works?")

