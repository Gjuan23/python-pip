import matplotlib.pyplot as plt

def generate_pie_chart():
    #le damos los valores de columna y fila
    labels = ['A','B','C']
    values = [200,34,120]
    # llamo la figura y coordenada
    fig, ax = plt.subplots()
    # genero el piechart con los valores y labels
    ax.pie(values,labels=labels)
    #plt.show() con esta funcion el programa se detiene para mostrar la img del grafico.
    # se guarda la img en archivo png y queda guardada en la carpeta
    plt.savefig('pie.png')
    # al guardarse la img, no se abre para no detener el programa
    plt.close()
