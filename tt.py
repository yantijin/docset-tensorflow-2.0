import os
n = 0
for root, dirs, files in os.walk('./out'):
    for name in files:
        if(name.endswith(".md")):
            n += 1
            print(n)
            os.remove(os.path.join(root, name))
