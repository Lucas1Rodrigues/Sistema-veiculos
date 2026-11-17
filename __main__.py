from veiculos import Carro,Moto,informacoes
def main():
    veiculos = []
    carro = Carro('Fiat','Uno mille',2012,23000,2)
    moto = Moto('kawasaki','ninja',2019,125000,1250)
    veiculos.append(carro)
    veiculos.append(moto)

    informacoes(veiculos)



if __name__ == "__main__":
    main()