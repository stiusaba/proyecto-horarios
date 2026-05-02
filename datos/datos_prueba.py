from modelos.docente import Docente
from modelos.curso import Curso
from modelos.salon import Salon
from modelos.franja import Franja

# 10 docentes
docentes = [Docente(i, f"Docente {i}") for i in range(1, 11)]

# 20 cursos (con diferentes tamaños)
cursos = [Curso(i, f"Curso {i}", 15 + (i % 20)) for i in range(1, 31)]

# 5 salones con diferentes capacidades
salones = [
    Salon(1, 20),
    Salon(2, 25),
    Salon(3, 30),
    Salon(4, 35),
    Salon(5, 40)
]

# 10 franjas (más combinaciones)
franjas = []
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

id_franja = 1
for dia in dias:
    for hora in ["8-10", "10-12"]:
        franjas.append(Franja(id_franja, dia, hora))
        id_franja += 1