import re

def jsonmaker(fopen, fwrite, count):
    for line in fopen:
        wordict = {}
        linearr = line.split(" ")
        string = str(count) + ": { 'kanji': "
        string += linearr[0] + ", "
        for word in linearr:
            if re.search('^P', word):
                pcodes = word.split("-")
                string += "'skip':" + str(word) + ", 'p1':" + pcodes[0][1] + ", 'p2':" + pcodes[1] + ", 'p3':" + pcodes[2] + "}, "
        fwrite.write(string)
        count += 1
    return count

f1 = open('group1.txt', 'r')
f2 = open('group2.txt', 'r')
f3 = open('group3.txt', 'r')
f4 = open('group4.txt', 'r')
f5 = open('1234.json', 'w')
count = 1
f5.write('"[{')
count = jsonmaker(f1, f5, count)
count = jsonmaker(f2, f5, count)
count = jsonmaker(f3, f5, count)
count = jsonmaker(f4, f5, count)
f5.write('}]"')
print "Done!" + str(count)
