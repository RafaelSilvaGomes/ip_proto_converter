from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def ip_para_binario(ip):
    try:
        octetos = ip.split('.')
        
        if len(octetos) != 4:
            return "Erro: O IP deve ter 4 partes separadas por ponto.", False
            
        octetos_binarios = []
        for octeto in octetos:
            num = int(octeto)
            if num < 0 or num > 255:
                return f"Erro: O valor '{num}' é inválido (use 0 a 255).", False
            
            binario = f"{num:08b}"
            octetos_binarios.append(binario)
            
        return ".".join(octetos_binarios), True
        
    except ValueError:
        return "Erro: Digite apenas números e pontos.", False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/converter', methods=['POST'])
def converter():
    dados = request.get_json()
    ip_digitado = dados.get('ip', '')
    
    resultado, sucesso = ip_para_binario(ip_digitado)
    
    if sucesso:
        return jsonify({"sucesso": True, "resultado": resultado})
    else:
        return jsonify({"sucesso": False, "erro": resultado})

if __name__ == '__main__':
    app.run(debug=True)