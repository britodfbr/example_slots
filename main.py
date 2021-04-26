from example_slots.formas import Circulo


if __name__ == '__main__':
    c = Circulo()
    c.raio = 3
    print(c.get_area())
    print(c.get_perimetro())
    
    c.a = 3