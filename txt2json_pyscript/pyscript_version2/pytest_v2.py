# For string checking
import re
# For converting into JSON format
import json

# Helper function that creates dictionary for each line in file
def dictmaker(fopen):
    # Declare these 2 variables as globals, so we don't have to return them at end of function
    global count
    global charlist
    # Goes through file line-by-line (e.g. newline character)
    for line in fopen:
        count += 1
        wordict = {}
        # Split the line into words
        linearr = line.split(" ")
        # Add the following fields to JSON so that JSON works as Django fixture
        wordict['model'] = 'jpskip.character'
        wordict['pk'] = str(count)
        for word in linearr:
            if re.search('^P', word):
                # Split skip codes by hyphens in case of double digits
                pcodes = word.split("-")
                # Data fields for Character model in Django
                wordict['fields'] = {'kanji': linearr[0], 'skipcode': str(word), 'p1': str(pcodes[0][1]), 'p2': str(pcodes[1]), 'p3': str(pcodes[2])}
        charlist.append(wordict)

f1 = open('group1.txt', 'r')
f2 = open('group2.txt', 'r')
f3 = open('group3.txt', 'r')
f4 = open('group4.txt', 'r')
f5 = open('db.json', 'a')

count = 0
charlist = []

dictmaker(f1)
dictmaker(f2)
dictmaker(f3)
dictmaker(f4)

#Convert list into JSON format and write to file.
f5.write(json.dumps(charlist))

print "Done! Total entries: " + str(count)
