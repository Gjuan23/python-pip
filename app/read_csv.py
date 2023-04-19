import csv


'''
import csv
with open('archivo.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for fila in csvreader:
        print(fila)
'''

def read_csv(path):     # ingreso el enrutador del archivo como parametro, que es PATH en este caso.
    with open('./data.csv','r') as csvfile:     # ingreso la ruta del archivo .csv
        reader = csv.reader(csvfile, delimiter= ',')        #csv.reader / sirve para leer formato csv que itera sobre las lineas del archivo.
        header = next(reader)       # aca iteramos la primer fila de la lista.
        data = []
        for row in reader:
            iterable = zip(header, row)  # con zip() unimos el header(encabezado) y reader(cuerpo del archivo).
            # print(list(iterable))     lo convertimos a lista.
            country_dict = {key:value for key,value in iterable}    # Agrego iterable a un nuevo diccionario y luego agrego a data que esta vacia.
            data.append(country_dict)
            #print('***' * 5)        # agregamos un separador por cada lista de datos.
            #print(row)
        return data
if __name__ == '__main__':
        data = read_csv('./app/data.csv')      # aca ingreso la funcion con su argumento que es la direccion del archivo .csv
        print(data[0])
