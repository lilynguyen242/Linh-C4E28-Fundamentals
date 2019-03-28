import excercise1
from matplotlib import pyplot
database = excercise1.connect()
customers = database['customers']
ref = customers.find()
events = 0
ads = 0
wom = 0
for i in ref:
    if i['ref'] == "events":
        events += 1
    elif i['ref'] == "ads":
        ads += 1
    elif i['ref'] == "wom":
        wom += 1
total = events + ads + wom

ref_data = [events, ads, wom]
ref_name = ["event", "advertisements", "word of mouth"]
pyplot.pie(ref_data, labels=ref_name, autopct="%.1f%%", shadow=True, explode=[0, 0.05, 0.05])
pyplot.title("References")
pyplot.axis("equal")
pyplot.show()