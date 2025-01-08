from flask import Flask, render_template

'''Instancia de la clase Flask'''
app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "Hola Mundo!!"

@app.route("/elegante")
def hola_mundo_elegante():
    return """
        <html>
            <body>
                <h1>Saludos!!</h1>
                <p>Hola Mundo!!</p>
            </body>
        </html>
    """

@app.route("/primera")
def template_primera():
    return render_template("primera_pagina.html")

@app.route("/segunda")
def template_segunda():
    return render_template("segunda_pagina.html")

@app.route("/variables")
def hola_nombre():
    return render_template("variables.html", nombre="Iván", curso="Python")

@app.route("/pedro")
def pedro():
    return render_template("variables.html", nombre="Pedro", curso="Java")

@app.route("/expresiones")
def expresiones():
    nombre = "Iván"
    apellido="Espinoza"
    color="Azul"
    base =5
    altura=10
    return render_template(template_name_or_list="expresiones.html", nombre=nombre, apellido=apellido, color=color, base=base, altura=altura)

def expresiones2():
    kwargs = {
        "nombre":"Roberto",
        "apellido":"Alegria",
        "color" : "Rojo",
        "base" : 2,
        "altura":5
    }
    return render_template(template_name_or_list="expresiones.html",**kwargs)


if __name__ == "__main__":
    app.run(debug=True)
