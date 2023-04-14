def run():
    return 'hola mi campeon'


names = ['Juan','Nadia','Candela','Valentina']
age = [26,25,4,3]

new_dict = {k : v for k, v in zip(names, age)}


if __name__ == '__main__':
    print(run())
    print(new_dict)



