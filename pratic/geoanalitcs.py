class vetor():
    def __init__(self) -> None:
        self.x
        self.y
        self.z

    


def ponto_medio(vet1,vet2):
    vet3 = vetor
    vet3 = (vet1.x + vet2.x)/2
    vet3 = (vet1.y + vet2.y)/2
    vet3 = (vet1.z + vet2.z)/2

    print(vet3)

vet = vetor
vet2 = vetor


print("vetor 1")
vet.x  = input("digite a coordenada x do vetor\n")
vet.y  = input("digite a coordenada y do vetor\n")
vet.z  = input("digite a coordenada z do vetor\n")

print("vetor 2")
vet2.x  = input("digite a coordenada x do vetor\n")
vet2.y  = input("digite a coordenada y do vetor\n")
vet2.z  = input("digite a coordenada z do vetor\n")



option = input("!!!!!!")

if option == 1:
    ponto_medio(vet,vet2)



print(vetor.x,vetor.y,vetor.z)




