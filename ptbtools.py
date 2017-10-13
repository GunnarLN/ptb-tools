import re
import os

#This fxn takes a regex string and spits out 1. the file name, 2. the start and end points of the tree, 3. the start and endpoints of the string matched, and 4. the match itself.
#This is formatted in the following way:
# FILENAME startTree:endTree startString:endString string
def printTreeLoc(file, string):
    pattern = r'\(TOP(?:(?!\(TOP)[\s\S])+?('+string+')[\s\S]+?(?=\n\n)'
    regex = re.compile(pattern)
    f = open(file, 'r')
    for match in regex.finditer(f.read()):
        print("{} {}:{} {}:{} {}".format(file, match.start(), match.end(), match.start(1), match.end(1), match.group(1)))
    f.close()
    
#Third param is the file being written to.
def writeTreeLoc(file, string, wfile):
    pattern = r'\(TOP(?:(?!\(TOP)[\s\S])+?('+string+')[\s\S]+?(?=\n\n)'
    regex = re.compile(pattern)
    f = open(file, 'r')
    f2 = open(wfile, 'a')
    for match in regex.finditer(f.read()):
        f2.write("{} {}:{} {}:{} {}\n".format(file, match.start(), match.end(), match.start(1), match.end(1), match.group(1)))
    f.close()
    f2.close()

#These two fxns take a line in the format above and print/write the tree.
def printTree(tline):
    plist = tline.split(" ")
    treeLoc = plist[1].split(":")
    treeLoc = [int(i) for i in treeLoc]
    f = open(plist[0], 'r')
    print(f.read()[treeLoc[0]:treeLoc[1]])
    f.close

def writeTree(tline, wfile):
    plist = tline.split(" ")
    treeLoc = plist[1].split(":")
    treeLoc = [int(i) for i in treeLoc]
    f = open(plist[0], 'r')
    f2 = open(wfile, 'a')
    f2.write(f.read()[treeLoc[0]:treeLoc[1]]+"\n\n")
    f.close    
    f2.close

#This guy will operate over a number of folders/files. Very useful for heavily segmented corpora.
#folder is the folder you're searching through, fextension is the file extension, fxn is whatever search function above being used and the args (minus the file arg).            
def multiFileHelper(folder, fextension, fxn, *fargs):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".parse"):
                fxn(os.path.join(root, file), *fargs)