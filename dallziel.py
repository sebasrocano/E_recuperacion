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
        
# Funcion de infección por años
import statistics
def avgyear(city, my_csv, year_c="1910"):
    """
    función para extraer el valor promedio de infectados
    """  
    cityyear = {}
    for line in my_csv:
        mycity = line['loc']
        year = line['year']
        pop = float(line['pop'])
        if line ['cases'] != "NA":
            case = float(line['cases'])
            cityyear[mycity] = cityyear.get (mycity, {})
            cityyear[mycity][year] = cityyear[mycity].get(year, [0,0,0,[]])
            cityyear[mycity][year][0] = cityyear[mycity][year][0] + pop
            cityyear[mycity][year][1] = cityyear[mycity][year][1] + case
            cityyear[mycity][year][2] = cityyear[mycity][year][2] + 1
            cityyear[mycity][year][3].append(case)           
    
    for keys in cityyear.keys():
        if keys == city:
            for key in cityyear[city].keys():
                if key == year_c:
                    avg_year = 100000*cityyear[city][year][1] / cityyear[city][year][0]
                    d_year = statistics.stdev(cityyear[city][year][3])
                    
                    return print ("Ciudad:",keys, 
                                  "\nAño",":",key,  
                                  "\nPromedio:",avg_year, 
                                  "\nDesviación Estandar:",d_year,  
                                  "\n# Registro:",cityyear[city][year][2])
                
# Funcion de infección por semanas
def avgbiweeks(city, my_csv, biweek_c="20"):
    """
    función para extraer el valor promedio de infectados
    """  
    citybiweek = {}
    for line in my_csv:
        mycity = line['loc']
        biweek = line['biweek']
        pop = float(line['pop'])
        if line ['cases'] != "NA":
            case = float(line['cases'])
            citybiweek[mycity] = citybiweek.get (mycity, {})
            citybiweek[mycity][biweek] = citybiweek[mycity].get(biweek, [0,0,0,[]])
            citybiweek[mycity][biweek][0] = citybiweek[mycity][biweek][0] + pop
            citybiweek[mycity][biweek][1] = citybiweek[mycity][biweek][1] + case
            citybiweek[mycity][biweek][2] = citybiweek[mycity][biweek][2] + 1
            citybiweek[mycity][biweek][3].append(case)
    
    for keys in citybiweek.keys():
        if keys == city:
            for key in citybiweek[city].keys():
                if key == biweek_c:
                    avg_biweek = 100000*citybiweek[city][biweek][1] / citybiweek[city][biweek][0]
                    d_biweek = statistics.stdev(citybiweek[city][biweek][3])
                    
                    return print ("Ciudad:",keys, 
                                  "\nSemana",":",key,  
                                  "\nPromedio:",avg_biweek, 
                                  "\nDesviación Estandar:",d_biweek,  
                                  "\n# Registro:",citybiweek[city][biweek][2])
    
