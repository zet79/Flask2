from flask import Flask, render_template

app= Flask(__name__)
class Pelicula:
        def __init__(self,nombre,anho,protagonista):
            self.nombre=nombre
            self.anho=anho
            self.protagonista=protagonista

@app.route("/estructura")
def estructura_datos():
    peliculas = [
        "El lobo de Wall Street",
        "Harry Potter"
        "Volver al Futuro"
    ]

    lobo = {
        "Nombre": "El lobo de Wall Street",
        "Año" :  2013,
        "Protagonista" : "Leonardo Di Caprio"
    }

    volver = Pelicula("Volver al futuro", 1985,"Michael J. Fox")

    return render_template("estructuras.html",movies=peliculas,destacada=lobo,favorita=volver)

if __name__ == "__main__":
    app.run(debug=True)