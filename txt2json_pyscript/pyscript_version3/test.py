# For string checking
import re
# For converting into JSON format
import json
import xml.etree.ElementTree

fopen = open('db.json', 'a')

count = 0
charlist = []

e = xml.etree.ElementTree.parse('kanjidic2.xml').getroot()
for ch in e.iter('character'):
    #fopen.write(ch.find("./literal").text.encode("utf-8"))
    if ch.find("./query_code/q_code[@qc_type='skip']")is not None:
        count += 1
        wordict = {}
        wordict['model'] = 'jpskip.character'
        wordict['pk'] = str(count)
        code = ch.find("./query_code/q_code[@qc_type='skip']").text
        codearr = code.split("-")
        wordict['fields'] = {'kanji': ch.find("./literal").text.encode("utf-8"), 'skipcode': "P" + code, 'p1': str(codearr[0]), 'p2': str(codearr[1]), 'p3': str(codearr[2])}
        charlist.append(wordict)

fopen.write(json.dumps(charlist))

print "Done! Total entries: " + str(count)
