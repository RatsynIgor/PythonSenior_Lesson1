print("Hello  world")
#Class теж саме щоб список зі змінних --> class + name subject: змінні
# def __init__(self): self.color = "red"
a = "Text" #intenger
b = 1 #string
c = 1.3 #float
d = True #boolean
class Marker:
    def __init__(self, color): #color змінна яка буде присвоюватися до поля обєкта
        self.height = "Metr"
        self.price = 1.22
        self.weight = 12
        self.isPresent = True

myMarker = Marker("red") #через змінну ми можемо виводити властивості змінної
print(myMarker.weight) #self описание предмета # Запускае ініціалізацію цих полів
# Якщо вводимо характеристуку pricе то виведе 1.22
# якщо введемо в строку 15 "red" і 16 "color" нам виведе колір червоний
