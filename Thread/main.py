from threading import Thread, get_ident

class Somador(Thread):

    def __init__(self, inicio, fim):
        Thread.__init__(self)
        self.inicio = inicio
        self.fim = fim
        self.somatorio = 0

    def run(self):
        for i in range(self.inicio, self.fim + 1):
            self.somatorio += i
            print('Thread-', get_ident())
        

s1 = Somador(0, 25)
s1.start()
s1.join()
print(s1.somatorio)
s2= Somador(11,20)
s2.start()
print(s2.somatorio)
print('Gabriel Oliveira Chaves')