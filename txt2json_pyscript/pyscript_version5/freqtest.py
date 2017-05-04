# For string checking
import re
# For converting into JSON format
import json
import xml.etree.ElementTree

e = xml.etree.ElementTree.parse('kanjidic2.xml').getroot()
for ch in e.iter('character'):
    if ch.find("./misc/freq") is not None:
        test = ch.find("./misc/freq").text
        print type(test)

print "Done!"
