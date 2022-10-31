class objeto: #Objeto para instanciar los objetos que se introduciran en la mochila.
    def __init__(self, peso, valor,nombre):  # Constructor
        self.peso = float(peso)
        self.valor = float(valor)
        self.nombre = nombre
        self.ratio = self.valor/self.peso

def o_sort(obj):#Funcion para usarla como "key" al momento de ordenar con respecto al valor de los objetos.
    return  obj.valor

def p_sort(obj):#Funcion para usarla como "key" al momento de ordenar con respecto al peso de los objetos.
    return  obj.peso

def r_sort(obj):#Funcion para usarla como "key" al momento de ordenar con respecto al ratio(v/p) de los objetos.
    return obj.ratio

def mochilazo(lista,W):#Funcion de la mochila, recibe una lista con los posibles y el peso maximo de mochila.
    #La complejidad de este algoritmo es Big O(n)
    valor_max = 0 
    objetosSeleccionados = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]#lista que guardara los objetos seleccionados.
    pesoActual = 0
    iterator = 0

    for i in lista: #Este for itera en los objetos de la lista de objetos posibles.
            if i.peso <= W: #Este if guarda marca como seleccionado al objeto actual si es que cabe en la mochila.
                valor_max += i.valor
                W -= i.peso
                objetosSeleccionados[iterator] = 1
                iterator += 1
            else: #Si no cabe completo, guarda una fraccion del objeto actual y rompe el ciclo.
                objetosSeleccionados[iterator] = (W - pesoActual) / i.peso
                valor_max += i.valor * objetosSeleccionados[iterator]
                break
    return objetosSeleccionados,valor_max#Retornamos la lista de objetos seleccionados y el valor maximo.             
    
    

def main():#Funcion principal.

    objetosSeleccionados=[] #Declaramos las variables para guardar los resultados del algoritmo.
    valor_max = 0
    objetosSeleccionados1=[]
    valor_max1 = 0
    objetosSeleccionados2=[]
    valor_max2 = 0
    computadora = objeto(6,1500,"Computadora") #Declaramos los objetos posibles para meter a la mochila.
    libro = objeto(3,50,"Libro")
    perro = objeto(10,60,"firulais")
    peluche = objeto(4,200,"osito de felpa")
    celular = objeto(4,900,"Celular")
    xbox = objeto(6,3000,"xbox")
    caguama = objeto(1,99,"caguama")
    navaja = objeto(2,200,"navaja")
    objetos = [computadora,libro,perro,peluche,celular,xbox,caguama,navaja] #Guardamos los objetos en una lista de objetos.
    
    #Ordena los objetos de mayor a menor respecto al valor
    s_objetos = sorted(objetos, key=o_sort,reverse=True)
    objetosSeleccionados,valor_max = mochilazo(s_objetos,20)

    #Ordena los objetos de menor a mayor respecto al peso
    s_objetos_peso = sorted(objetos, key=p_sort)
    objetosSeleccionados1,valor_max1 = mochilazo(s_objetos_peso,20)

    #Ordena los objetos de mayor a menor por el valor/peso 
    s_objetos_ratio = sorted(objetos, key=r_sort,reverse=True)
    objetosSeleccionados2,valor_max2 = mochilazo(s_objetos_ratio,20)

    
    
    #Imprime los nombres, porciones de los objetos y el valor total agregado a la mochila respecto al objeto más valioso
    print("|----------Enfoque con respecto al objeto mas valioso------------|")
    for i in s_objetos:
        print(i.nombre,", ",end="")
    print("\nObjetos Agregados: ",objetosSeleccionados)
    print("Valor total: ",valor_max)
    print("\n\n")

    #Imprime los nombres, porciones de los objetos y el valor maximo que fue agregado a la mochila respecto al menor peso
    print("|----------Enfoque con respecto al menor peso------------|")
    for i in s_objetos_peso:
        print(i.nombre,", ",end="")
    print("\nObjetos Agregados: ",objetosSeleccionados1)
    print("Valor total: ",valor_max1)
    print("\n\n")

    #Imprime los nombres, porciones de los objetos y el valor maximo que fue agregado a la mochila respecto al valor/peso
    print("|----------Enfoque con respecto al valor / peso------------|")
    for i in s_objetos_ratio:
        print(i.nombre,", ",end="")
    print("\nObjetos Agregados: ",objetosSeleccionados2)
    print("Valor total: ",valor_max2)
    

if __name__ == "__main__":
    main()
