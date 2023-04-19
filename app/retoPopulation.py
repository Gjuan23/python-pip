import csv

def read_csv():
    with open('./data.csv','r') as file:
        """llamamos la funcion reader del paquete csv para leer el archivo csv"""
        reader = csv.reader(file,delimiter=',')
        """agregamos next a la variable header para poder iterar la primer fila del archivo, que son los titulos de los datos"""
        header = next(reader)
        data = []
        """con un for iteramos cada linea del archivo"""
        for row in reader:
            iterable = zip(header,row)
            """Aca, ya uní mediante zip(), las columnas con filas en iterable"""
            country_dict = {k : v for (k,v) in iterable}
            """Ya hecho el dictComprehension ahora lo agrego a una lista"""
            data.append(country_dict)
        return data
        """Retorno la lista en variable 'data' fuera del bucle for para que devuelva la lista"""



if __name__ == '__main__':
    se = read_csv()
    print(se[8])




