import codecs

f1 = codecs.open('radkfile2', encoding='euc_jp')
f2 = codecs.open('radkfile2_converted.txt', 'w', encoding='utf8')

for line in f1:
    if line.startswith('#'):
        continue
    else:
        f2.write(line)

f1.close()
f2.close()

print "Done!"
