import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()    # plt.subplots crea dos objetos, figura fig y ejes ax.
    ax.bar(labels,values)       # grafica de barras.
    plt.savefig(f'./imgs/{name}bar.png')      # show para mostrar el grafico.
    plt.close()

def generate_pie_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)    # grafica de torta.
    ax.axis('equal')
    plt.savefig(f'./imgs/{name}pie.png')
    plt.close()

if __name__ == '__main__':
    labels = ['A', 'B', 'B']    # le paso el valor de labels para que pueda retornar.
    values = [10, 40, 800]      # ""
    # generate_bar_chart(labels,values)
    generate_pie_chart(labels,values)




