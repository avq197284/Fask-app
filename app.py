from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, Mundo!'

@app.route('/about')
def about_func():
    return 'Acerca de esta página'

@app.route('/contact')
def contact_func():
    return 'Contáctanos en flask@example.com'

if __name__ =='__main__':
    app.run(debug=True)


