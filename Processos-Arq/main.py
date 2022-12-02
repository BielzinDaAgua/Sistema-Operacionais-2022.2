import os
import sys

#Coletando o primeiro número do arquivo 1 como parâmetro:
param1 = sys.argv[1]
arquivo1 = open(param1)
numi = arquivo1.read()
numInicial = int(numi)

#Coletando o segundo número do arquivo 2 como parâmetro:
param2 = sys.argv[2]
arquivo2 = open(param2)
numf = arquivo2.read()
ret = os.fork()
numFinal = int(numf)



if ret == 0:
  #Processo Filho
  with open("pares.txt", "w") as f:
    for x in range(numInicial, numFinal+1):
      if x %2 == 0:
        y = str(x)
        f.write(y)
        f.write("\n")
    f.close()
    print("Finalizando a Execução do Filho")
    os.execv("/bin/cp", ["-f", "pares.txt", "/tmp"] )
else:
  #Processo Pai
  os.wait()
  print("Iniciando Execução Pai")
  os.execv("/bin/cat", ["/tmp/", "pares.txt"] )
  
