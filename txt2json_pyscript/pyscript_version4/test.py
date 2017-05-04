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
    if ch.find("./query_code/q_code[@qc_type='skip']")is not None:
        code = ch.find("./query_code/q_code[@qc_type='skip']").text
        codearr = code.split("-")
        if codearr[0] == '1':
            count += 1
            wordict = {}
            wordict['kanji_id'] = str(count)
            wordict['kanji'] = ch.find("./literal").text.encode("utf-8")
            wordict['skipcode'] = "P" + code
            wordict['p1'] = str(codearr[0])
            wordict['p2'] = str(codearr[1])
            wordict['p3'] = str(codearr[2])
            charlist.append(wordict)

for ch in e.iter('character'):
    if ch.find("./query_code/q_code[@qc_type='skip']")is not None:
        code = ch.find("./query_code/q_code[@qc_type='skip']").text
        codearr = code.split("-")
        if codearr[0] == '2':
            count += 1
            wordict = {}
            wordict['kanji_id'] = str(count)
            wordict['kanji'] = ch.find("./literal").text.encode("utf-8")
            wordict['skipcode'] = "P" + code
            wordict['p1'] = str(codearr[0])
            wordict['p2'] = str(codearr[1])
            wordict['p3'] = str(codearr[2])
            charlist.append(wordict)

for ch in e.iter('character'):
    if ch.find("./query_code/q_code[@qc_type='skip']")is not None:
        code = ch.find("./query_code/q_code[@qc_type='skip']").text
        codearr = code.split("-")
        if codearr[0] == '3':
            count += 1
            wordict = {}
            wordict['kanji_id'] = str(count)
            wordict['kanji'] = ch.find("./literal").text.encode("utf-8")
            wordict['skipcode'] = "P" + code
            wordict['p1'] = str(codearr[0])
            wordict['p2'] = str(codearr[1])
            wordict['p3'] = str(codearr[2])
            charlist.append(wordict)

for ch in e.iter('character'):
    if ch.find("./query_code/q_code[@qc_type='skip']")is not None:
        code = ch.find("./query_code/q_code[@qc_type='skip']").text
        codearr = code.split("-")
        if codearr[0] == '4':
            count += 1
            wordict = {}
            wordict['kanji_id'] = str(count)
            wordict['kanji'] = ch.find("./literal").text.encode("utf-8")
            wordict['skipcode'] = "P" + code
            wordict['p1'] = str(codearr[0])
            wordict['p2'] = str(codearr[1])
            wordict['p3'] = str(codearr[2])
            charlist.append(wordict)


fopen.write(json.dumps(charlist))

print "Done! Total entries: " + str(count)
