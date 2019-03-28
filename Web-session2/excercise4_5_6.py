import excercise1
database = excercise1.connect()
rivers = database['river']
rivers_africa = rivers.find({'continent': 'Africa'})
for i in rivers_africa:
    print(i['name'])

rivers_america = rivers.find({'continent': 'S. America'})
for a in rivers_america:
    if int(a['length']) < 1000:
        print(a['name'])
