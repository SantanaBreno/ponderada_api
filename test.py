import pytest 
from app import Animal, Recinto

@pytest.fixture
def animal_feliz():
    animal = Animal('Spike', 'Cachorro')
    animal.alimentar()
    animal.alimentar()
    animal.alimentar()
    return animal

@pytest.fixture
def animal_triste():
    animal = Animal('Figo', 'Gato')
    return animal

def test_animal_feliz(animal_feliz):
    assert animal_feliz.felicidade == 30
    assert animal_feliz.nome == 'Spike'
    assert animal_feliz.especie == 'Cachorro'

def test_esta_feliz(animal_feliz, animal_triste):
    assert animal_feliz.esta_feliz() == False  # Ainda não está feliz
    assert animal_triste.esta_feliz() == False  # Não está feliz

@pytest.fixture
def recinto():
    return Recinto('Recinto 1')

def test_recinto(recinto):
    assert recinto.nome == 'Recinto 1'
    assert recinto.animais == []

def test_adicionar_animal(recinto, animal_feliz):
    recinto.adicionar_animal(animal_feliz)
    assert recinto.animais == [animal_feliz]

def test_alimentar_animais(recinto, animal_feliz):
    recinto.adicionar_animal(animal_feliz)
    recinto.alimentar_animais()
    assert recinto.animais[0].felicidade == 40

def test_adicionar_animal_diferente_especie(recinto, animal_feliz, animal_triste):
    recinto.adicionar_animal(animal_feliz)
    recinto.adicionar_animal(animal_triste) 
    assert len(recinto.animais) == 1  
