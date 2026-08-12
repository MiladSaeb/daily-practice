import csv
sensordata = [

    {
        "tid": "20:00",
        "temperatur": 20 ,
        "luftfuktighet": "24 %"
    },

    {
        "tid": "21:00",
        "temperatur": 30 ,
        "luftfuktighet": "44 %"
    },

    {
        "tid": "23:00",
        "temperatur": 50 ,
        "luftfuktighet": "50 %"
    },

    {
        "tid": "12:00",
        "temperatur": 2 ,
        "luftfuktighet": "2 %"
    },

    {
        "tid": "2:00",
        "temperatur": 24,
        "luftfuktighet": "27 %"
    },
]

print(sensordata)

summa = 0
medel = 0
for avlastning in sensordata:
    summa = summa + avlastning["temperatur"] 
    
print(summa)

medel = summa / (len(sensordata))
print(medel)

high = sensordata[0]["temperatur"]
low = sensordata[0]["temperatur"]
for x in sensordata:
    if x["temperatur"] > high:
        high = x["temperatur"]
    if x["temperatur"] < low:
        low = x["temperatur"]

print(high)
print(low)

with open('university_records.csv', 'w', newline='') as csvfile:
    fieldnames = ['tid', 'temperatur', 'luftfuktighet']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sensordata)