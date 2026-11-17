from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self,marca,modelo,ano,valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


    @abstractmethod
    def exibir_informacao(self):
        pass

    def informacoes_basicas(self):
        return (f"-------------------------\n"
        f'Veiculo: {type(self).__name__}\n'
        f'Marca: {self.marca}\n'
        f'Modelo: {self.modelo}\n'
        f'Ano: {self.ano}\n'
        f'Valor: {self.valor}')

    @abstractmethod
    def exibir_ipva(self):
        pass

    

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano,valor,portas):
        super().__init__(marca, modelo, ano,valor)
        self.portas = portas
        self.valor = valor

    def exibir_informacao(self):
        print(self.informacoes_basicas())
        print(f'Portas: {self.portas}')
        print(f'Ipva R$ {self.exibir_ipva()}')
    
    def exibir_ipva(self):
            return self.valor * 0.04

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano,valor,cilindradas):
        super().__init__(marca, modelo, ano,valor)
        self.cilindradas = cilindradas
        self.valor = valor

    def exibir_informacao(self):
        print(self.informacoes_basicas())
        print(f'Cilindradas: {self.cilindradas}')
        print(f'Ipva R$ {self.exibir_ipva()}')

    def exibir_ipva(self):
        return self.valor * 0.02

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano,valor,carga):
        super().__init__(marca, modelo, ano,valor)
        self.carga = carga
        self.valor = valor

    def exibir_informacao(self):
        print(self.informacoes_basicas())
        print(f'Capacidade Carga: {self.carga}')
        print(f'Ipva R$ {self.exibir_ipva()}')

    def exibir_ipva(self):
            return self.valor * 0.015

def informacoes(veiculos:list):
    try:
        for veiculo in veiculos:
            veiculo.exibir_informacao()
    except:
        print("Ocorreu um erro")
        
        

        
