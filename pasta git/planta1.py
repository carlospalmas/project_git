from abc import ABC, abstractmethod

class Planta(ABC):
    def __init__(self, nome_comum, nome_cientifico, umidade, luz):
        self.nome_comum = nome_comum
        self.nome_cientifico = nome_cientifico
        self.__umidade = None
        self.__luz = None
        self.set_umidade(umidade)
        self.set_luz(luz)

    def get_umidade(self):
        return self.__umidade

    def set_umidade(self, umidade):
        if 0 <= umidade <= 100:
            self.__umidade = umidade
        else:
            print("Erro: Umidade deve estar entre 0 e 100.")

    def get_luz(self):
        return self.__luz

    def set_luz(self, luz):
        if 0 <= luz <= 100:
            self.__luz = luz
        else:
            print("Erro: Luz deve estar entre 0 e 100.")

    @abstractmethod
    def verificar_cuidados(self):
        pass

    def exibir_info(self):
        print(f"Nome Comum: {self.nome_comum}")
        print(f"Nome Científico: {self.nome_cientifico}")
        print(f"Umidade: {self.get_umidade()}%")
        print(f"Luz: {self.get_luz()}%")

class Cacto(Planta):
    def verificar_cuidados(self):
        if self.get_umidade() >= 35:
            print("⚠️ Atenção: O cacto precisa de menos água!")
        if self.get_luz() < 65:
            print("⚠️ Atenção: O cacto precisa de mais luz!")

class Flor(Planta):
    def verificar_cuidados(self):
        if not (40 <= self.get_umidade() <= 70):
            print("⚠️ Atenção: A flor precisa de umidade entre 40 e 70!")
        if not (50 <= self.get_luz() <= 80):
            print("⚠️ Atenção: A flor precisa de luz entre 50 e 80!")

class PlantaAquatica(Planta):
    def verificar_cuidados(self):
        if self.get_umidade() < 90:
            print("⚠️ Atenção: A planta aquática precisa de mais umidade!")
        if self.get_luz() >= 50:
            print("⚠️ Atenção: A planta aquática nAo precvida de tanta luz!")

def monitorar_estufa(lista_plantas):
    for planta in lista_plantas:
        planta.exibir_info()
        planta.verificar_cuidados()
        planta.set_umidade(2)
        print("-" * 30)

estufa = [
    Cacto("Cacto", "Cactaceae", 35, 65),
    Flor("Rosa", "Rosa sp.", 50, 75),
    PlantaAquatica("Vitória-régia", "Victoria amazonica", 85, 55),
]

monitorar_estufa(estufa)

# teste de atualização