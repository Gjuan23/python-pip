import os
os.system('clear')

#import utils
import read_csv #Necesito este módulo para leer el csv
import charts   #Necesito este módulo que ya tiene funcion con gráfica
import retoPopulation_2 as utilsV2

"""data = [
    {
        'Country':'Colombia',
        'Population': 300
    },{
        'Country':'Bolivia',
        'Population':'300'
    }
]"""

def run():
    data = read_csv.read_csv('./app/data.csv')  # IMPORTAMOS LA FUNCION DEL PAQUETE read_csv
    country = input('Type Country => ')     # YA IMPORTADA LA DATA, INGRESAR PAIS QUE BUSCAMOS
    #print(country)
    result = utilsV2.population_by_country(data,country)     # IMPORTAMOS FUNCION (FILTER) QUE FILTRA Y AGREGAMOS LOS ARGUMENTOS
    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utilsV2.get_population(country)
        charts.generate_bar_chart(country, labels, values)
        charts.generate_pie_chart(country, labels, values)


if __name__ == '__main__':
    run()

    """keys, values = utils.get_population()
    print(keys, values)
    country = input('Type Country =>  ')
    result = utils.population_by_country(data,country)
    print(result)"""

# la funcion run() se está controlando desde example.py
# para correr run() desde su archivo de origen adivinanza.py utilizamos este metodo.




