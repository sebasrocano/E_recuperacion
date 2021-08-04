# Funcion de infección por ciudades
import pandas as pd
import numpy as np

def avgcity(city, my_csv):
    """
    función para extraer el valor promedio de infectados
    """  
    citypop = {}
    for line in my_csv:
        mycity = line['loc']
        pop = float(line['pop'])
        if line ['cases'] != "NA":
            case = float(line['cases'])
            citypop[mycity] = citypop.get(mycity, [0,0,0])
            citypop[mycity][0] = citypop[mycity][0] + pop
            citypop[mycity][1] = citypop[mycity][1] + case
            citypop[mycity][2] = citypop[mycity][2] + 1
    for key in citypop:
        if key == city:
            avg_case = 100000*citypop[key][1]/citypop[key][0]
            return print (key, avg_case)
        
