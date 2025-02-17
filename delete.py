from model import session, Carro
from model import Carro, session

def delete(id):
    carro = session.query(Carro).filter(Carro.id == id).first()
    print(carro)
    if carro is None:
        raise ValueError(f"Carro with id {id} not found")
    session.delete(carro)
    session.commit()

    return {"id": id}