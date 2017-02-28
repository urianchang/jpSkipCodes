import json

f = open('test.json', 'w')
test = []
for num in range(0, 2):
    data = {}
    data['model'] = 'jpskip.character'
    data['pk'] = str(1)
    data['fields'] = {'kanji': 'test', 'p1': str(2)}
    test.append(data)
    # f.write(json.dumps(data))
f.write(json.dumps(test))
