class Dad:
    basketball = 1

class Son(Dad):
    basketball = 9
    dance = 1
    def isdance(self):
        return f" Yes i Dance {self.dance} no of times"

class Grandson(Son):
    dance= 6
    def isdance(self):
        return f" Yes i Dance very Awesomely {self.dance} no of times"


dada = Dad()
beta = Son()
pota = Grandson()

print(pota.basketball)
print(pota.isdance())