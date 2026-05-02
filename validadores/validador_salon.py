def validar_salon(horario, salon, franja):
    for a in horario.asignaciones:
        if a.salon.id == salon.id and a.franja.id == franja.id:
            return False
    return True