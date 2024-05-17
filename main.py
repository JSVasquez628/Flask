from flask import Flask, request, make_response, redirect, render_template #importar el framework

app = Flask(__name__)
items = ['Colombia','Peru','Argentina','Brasil']

@app.route('/index') #Definir ruta
def index (): # va a funcionar como una vista para resivir los request
    user_ip = request.remote_addr
    response = make_response(redirect('/mostrarip'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/mostrarip')
def Mostrar_informacion():
    mostrarinf = request.cookies.get('user_ip')
    contexto = {'su_ip':mostrarinf, 'items':items}
    return render_template('respuesta.html', **contexto)


app.run(host='0.0.0.0', port=81, debug=True)