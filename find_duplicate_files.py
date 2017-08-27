"""
This goes through a directory and finds all the duplicate files. It needs to do this by content in the file and not by file name.

"""

import os
import md5

startingDirectory = r'/Users/stupidrobot/Box Sync/'

stack = [startingDirectory]

filesSeen = {} # I want the contents of the file as the key and the name of the fileName and time as a tuple for the value.

duplicates = []

extensionToIgnore = ['exp','pdb']
# first list all files in the directory.
# for every new directory found append that to the stack and for any new file read the contents and compare to what you already have.
count = 0
while len(stack) > 0:
    currentPath = stack.pop()
    if os.path.isdir(currentPath):
        for path in os.listdir(currentPath):
            stack.append(os.path.join(currentPath, path))

    else:
# this is a file lets open it and read contents. Compute, search for, and store a hash instead. First check that the extension is belongs to a file I care to check
        extension = currentPath.split('.')
        if len(extension) > 1:
            extension = extension[-1]
            if extension in extensionToIgnore:
                continue

        with open(currentPath) as file:
            contents = file.read()
        newHash = md5.new(contents).digest()
        
#record the last time this was edited.
        lastEdited = os.path.getmtime(currentPath)

# have we seen this file before?
        if newHash in filesSeen:
            previousVersion, previousTime = filesSeen.get(newHash)

            if previousTime > lastEdited:
# previous version is the duplicate
                duplicates.append((previousVersion, currentPath))
            else:
# the file I just found is the duplicate.
                duplicates.append((currentPath, previousVersion))
        else:
            filesSeen.update({newHash: (currentPath, lastEdited)})
    if count/10. == round(count/10):
        print "the size of the stack is %i"%len(stack)
    count += 1

print "I found %i duplicates"%(len(duplicates))   


