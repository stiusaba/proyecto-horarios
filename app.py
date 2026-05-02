from flask import Flask, render_template, request
from modelos.horario import Horario
from algoritmo.generador import generar_horario
from datos.datos_prueba import cursos, docentes, salones, franjas

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/generar", methods=["GET", "POST"])
def generar():
    from modelos.docente import Docente
    from modelos.curso import Curso
    from modelos.salon import Salon
    from modelos.franja import Franja
    from modelos.horario import Horario
    from algoritmo.generador import generar_horario

    if request.method == "POST":
        try:
            num_docentes = int(request.form["docentes"])
            num_cursos = int(request.form["cursos"])
            num_salones = int(request.form["salones"])

            docentes = [Docente(i, f"Docente {i}") for i in range(1, num_docentes + 1)]
            cursos = [Curso(i, f"Curso {i}", 20 + (i % 10)) for i in range(1, num_cursos + 1)]
            salones = [Salon(i, 30) for i in range(1, num_salones + 1)]

            franjas = [
                Franja(1, "Lunes", "8-10"),
                Franja(2, "Lunes", "10-12"),
                Franja(3, "Martes", "8-10"),
                Franja(4, "Martes", "10-12"),
            ]

            horario = Horario()
            exito = generar_horario(cursos, docentes, salones, franjas, horario)

            if exito:
                resultado = []
                for a in horario.asignaciones:
                    resultado.append({
                        "curso": a.curso.nombre,
                        "docente": a.docente.nombre,
                        "salon": a.salon.id,
                        "franja": f"{a.franja.dia} {a.franja.hora}"
                    })
                return render_template("index.html", horario=resultado)
            else:
                return render_template("index.html", error="No se pudo generar el horario")

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)