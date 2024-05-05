from flask import Flask

app = Flask(__name__)

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.felicidade = 0

    def alimentar(self):
        self.felicidade += 10
    
    def esta_feliz(self):
        return self.felicidade > 50
    
class Recinto:
    def __init__(self, nome):
        self.nome = nome
        self.animais = []

    def adicionar_animal(self, animal):
        if not self.animais:
            self.animais.append(animal)
        elif animal.especie == self.animais[0].especie:
            self.animais.append(animal)
        else:
            print(f"Não é possível adicionar o animal {animal.nome} ao recinto {self.nome}.")
            print(f"A espécie do animal ({animal.especie}) é diferente da espécie dos animais presentes ({self.animais[0].especie}).")

    
    def alimentar_animais(self):
        for animal in self.animais:
            animal.alimentar()
    
    def animais_felizes(self):
        return [animal for animal in self.animais if animal.esta_feliz()]
    

if __name__ == '__main__':
    app.run()