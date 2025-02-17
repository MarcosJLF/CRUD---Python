from model import session, Carro

def read():
    carros = session.query(Carro).all()
    carros_dict = {}
    for carro in carros:
        carros_dict[carro.id] = {
            'modelo': carro.modelo,
            'marca': carro.marca,
            'ano': carro.ano,
            'cor': carro.cor,
            'km': carro.km,
            'preco': carro.preco
        }
    return carros_dict
