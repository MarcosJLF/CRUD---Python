from flask import Flask, request, jsonify
from c import add_carro
from delete import delete

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def carro():
    
    data = request.get_json()

    if not data or not data.get('modelo') or not data.get('marca') or not data.get('ano') or not data.get('cor') or not data.get('km') or not data.get('preco'):
        return jsonify({'message': 'Todos os campos devem ser preenchidos'}), 400
    
    try:
        carro = {
            'modelo': data['modelo'],
            'marca': data['marca'],
            'ano': data['ano'],
            'cor': data['cor'],
            'km': data['km'],
            'preco': data['preco']
        }

        dic = {}
        dic = add_carro(**carro)

        return jsonify({"Status": "Modelo adicionado", "Modelo": dic}), 201
        # if result:
        #     return jsonify({'message': 'Carro adicionado com sucesso'}), 201
        # else:
        #     return jsonify({'message': 'Erro ao adicionar carro'}), 500
        
    except Exception as e:
        return jsonify({'message': f'Erro ao adicionar carro: {str(e)}'}), 500
    
@app.route('/api/<int:id>', methods=['DELETE'])

def delete_carro(id):
    try:
        result = delete(id)
        if result == None:
            return jsonify({'message': 'Carro não encontrado'}), 404
        else:
            return jsonify({'message': 'Carro deletado com sucesso'}), 200
    except Exception as e:
        return jsonify({'message': f'Erro ao deletar carro: {str(e)}'}), 500
    
if __name__ == '__main__':
    app.run(debug=True)




