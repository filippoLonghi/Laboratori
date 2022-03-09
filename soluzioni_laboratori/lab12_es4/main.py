#Laboratorio 12 esercizio 4. Contatti di sospetti
def dict_creation(file):
    registro={}
    for line in file:
        line=line.rstrip("\n").rsplit(",",3)
        registro[line[0]]=[line[1],int(line[2]),int(line[3])]
    return registro

def ricerca_contatti(file, registro):
    for line in file:
        line=line.rstrip("\n")
        if line in registro:
            print("** Contatti del cliente: %s: **" %line)
            flag=0
            for key in registro:
                if key!=line and (registro[line][1]>=registro[key][1] and registro[line][1]<=registro[key][2] or registro[line][2]>=registro[key][1] and registro[line][2]<=registro[key][2]):
                    print("\tContatto con %s, telefono %s" %(key,registro[key][0]))
                    flag=1
            if not flag:
                print("\tIl cliente %s non ha avuto contatti" %line)
        else:
            print("** Contatti del cliente: %s: **\n\tCliente %s non presente in archivio" %(line,line))
    return


try:
    try:
        file=open("presenze.txt","r")
        registro=dict_creation(file)
    finally:
        file.close()
except IOError:
    print("Errore apertura file ""presenze.txt""")

try:
    try:
        file=open("sospetti.txt","r")
        ricerca_contatti(file, registro)
    finally:
        file.close()
except IOError:
    print("Errore apertura file ""sospetti.txt""")
