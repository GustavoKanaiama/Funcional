def fact(x):
    x = int(x)
    return 1 if(x == 0) else (x*fact(x-1))

def fib(n):
    n = int(n)
    if (n == 2):
        return 1
    
    return 0 if (n == 0 or n == 1) else (fib(n-1) + fib(n-2))


with open('./output.dat', 'w') as f_out:
    
    db = open('./input.dat', 'r').read()

    f_out.write(''.join(list(map(lambda x : f"Linha {str(x[0])}: Fib({str(x[1])})={str(x[2])} Fact({str(x[3])})={str(x[4])}\n", list(map(lambda x : [list(map(lambda x : x.split(',') if (',') in x else x.split(), db.split('\n'))).index(x), x[0].strip(), fib(x[0]), x[1].strip(), fact(x[1])], list(map(lambda x : x.split(',') if (',') in x else x.split(), db.split('\n')))))))))


    """
    #Ler o arquivo de entrada(input)
    f_in = open('./input.dat', 'r')
    db = f_in.read()
    
    #Criei uma lista de listas
    lista_de_listas = map(lambda x : x.split(',') if (',') in x else x.split(), db.split('\n'))

    #listando a lista_de_lista para poder usar o método .index()
    lista_de_listas = list(lista_de_listas)

    
    #Aplicando fib() e fact() em cada um dos elementos formatado: "nlinha, xfib, fib(), yfact ,fact()" utilizando o metodo strip para evitar espaços
    res = map(lambda x : [lista_de_listas.index(x), x[0].strip(), fib(x[0]), x[1].strip(), fact(x[1])], lista_de_listas)
    
    
    #Transcrever de novo para o formato de string
    str_form = map(lambda x : f"Linha {str(x[0])}: Fib({str(x[1])})={str(x[2])} Fact({str(x[3])})={str(x[4])}\n", list(res))
    
    #Dar criar uma string com join() iterando todos elementos das listas
    str_final = ''.join(list(str_form))


    f_out.write(str_final)
    """
    
    
    