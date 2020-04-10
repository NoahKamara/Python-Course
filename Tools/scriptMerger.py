from os import listdir

directory = 'Script/'

filenames = listdir(directory)
completeDocument = ""
for filename in filenames:
    filename = directory+filename
    if filename.startswith('00'):
        continue

    with open(filename, 'r') as f:
        completeDocument += f.read()
        completeDocument += "\n\n---\n\n"

with open('Script/00 Complete.md', 'w') as f:
    f.write(completeDocument)
