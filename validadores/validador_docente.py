def validar_docente(horario, docente, franja):
    for a in horario.asignaciones:
        if a.docente.id == docente.id and a.franja.id == franja.id:
            return False
    return True