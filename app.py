
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multiplicacao')
def multiplicacao():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))
    
    conta = n1 * n2 

    return {

            'numero1': n1,
            'numero2': n2,
            'multiplicar os 2 numeros': conta
         }


@app.route('/soma')
def soma():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))
    
    conta = n1 + n2 

    return {

            'numero1': n1,
            'numero2': n2,
            'soma os 2 numeros': conta
         }


@app.route('/subtracao')
def subtracao():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))
    
    conta = n1 - n2 

    return {

            'numero1': n1,
            'numero2': n2,
            'subtrair os 2 numeros': conta
         }


@app.route('/divisao')
def divisao():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))
    
    conta = n1 / n2 

    return {

            'numero1': n1,
            'numero2': n2,
            'dividir os 2 numeros': conta
         }


if __name__ =='__main__':
    app.run(debug=True)






