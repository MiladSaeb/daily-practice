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
        {
        "tid": "3:00",
        "temperatur": 23 ,
        "luftfuktighet": "24 %"
    },

    {
        "tid": "18:00",
        "temperatur": 550 ,
        "luftfuktighet": "44 %"
    },

    {
        "tid": "1:00",
        "temperatur": 10 ,
        "luftfuktighet": "50 %"
    },

    {
        "tid": "16:00",
        "temperatur": 26 ,
        "luftfuktighet": "2 %"
    },

    {
        "tid": "23:00",
        "temperatur": 29,
        "luftfuktighet": "27 %"
    },
]
def berakna_medel(data, min_temp = -40, max_temp = 60):
     
    summa = 0
    antal_giltiga = 0
    for avlasning in data:
        if avlasning["temperatur"] > max_temp:
            print("To high temp ")
        elif avlasning["temperatur"] < min_temp:
            print("To low temp")
        else:
            antal_giltiga = antal_giltiga + 1
            summa = summa + avlasning["temperatur"]
    medel = summa / antal_giltiga
    return medel

print(berakna_medel(sensordata))