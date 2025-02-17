from model import Carro, session

def  add_carro(modelo, marca, ano, cor, km, preco):
    carro = Carro(modelo=modelo, marca=marca, ano=ano, cor=cor, km=km, preco=preco)
    session.add(carro)
    session.commit()
    print("Carro adicionado com sucesso")

    return {"modelo": modelo, "marca": marca, "ano": ano, "cor": cor, "km": km, "preco": preco}


#add_carro('Fusca', 'Volkswagen', 1970, 'Azul', 100000, 10000)