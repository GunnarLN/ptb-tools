A few useful (but limited) functions for working with the Penn Treebank.

printTreeLoc(file, string) - prints the location of a tree with the matching regex string to the console.
writeTreeLoc(file, string, wfile) - writes the location to whatever file specified in wfile.
printTree(tree-loc-line) - prints the tree specified in tree-loc-line to the console.
writeTree(tree-loc-line, wfile) writes the tree specified in tree-loc-line to the file in wfile.
multiFileHelper(folder-location, file-extension, function, fxn-arguments) - runs function (printTreeLoc, writeTreeLoc) over all files with file-extension in folder-location. (very useful for running a search in e.g. ontonotes)