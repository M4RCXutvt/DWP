try:
    path= 'C:\\Filespy\\archivo.txt'
    new_file= open(path, 'r')
    data = new_file.readlines()
    print(data)
    one_line = new_file.readlines()
    one_line = new_file.readlines()
    print(one_line)
    print(one_line)

    #new_file = open('C:\\Filespy\\archivo.txt', 'w')
    #new_file.write("Hello World\n")
    #new_file.write("Hola mundo\n")
    #new_file.write("Hola UTVTA\n")
    #new_file.close()
except Exception as e:
    print(e)