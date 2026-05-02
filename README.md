# Sistema de Generación de Horarios Académicos
 
## Descripción del Proyecto
 
Este proyecto es un sistema web desarrollado en Python con Flask que permite generar horarios académicos de forma automática utilizando un algoritmo de asignación con validaciones de conflictos.
 
El sistema busca resolver el problema de planificación de horarios (timetable problem), asignando cursos, docentes, salones y franjas horarias evitando choques de disponibilidad.
 

 
## Tecnologías Utilizadas
 
- Python 3
- Flask
- HTML + CSS
- Estructura modular (MVC básico)

 
## Estructura del Proyecto
 
```
proyecto_horarios/
│
├── app.py
├── main.py
├── algoritmo/
├── datos/
├── modelos/
├── validadores/
├── static/
└── templates/
```

 
## Requisitos
 
Antes de ejecutar el proyecto, asegúrate de tener instalado:
 
- Python 3.10 o superior
- pip
- Entorno virtual (opcional pero recomendado)
Instalar Flask:
 
```bash
pip install flask
```
  
## Instalación y Ejecución
 
**1. Clonar el repositorio**
 
```bash
git clone https://github.com/stiusaba/proyecto-horarios.git
cd proyecto-horarios
```
 
**2. Crear entorno virtual (opcional)**
 
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
 
**3. Instalar dependencias**
 
```bash
pip install flask
```
 
**4. Ejecutar el sistema**
 
```bash
python app.py
```
 
**5. Abrir en el navegador**
 
```
http://127.0.0.1:5000/
```
 
## Funcionalidades
 
- Generación automática de horarios
- Asignación de cursos, docentes y salones
- Validación de conflictos
- Interfaz web básica
- Manejo de escenarios con distintos tamaños de entrada

 
## Limitaciones
 
- No incluye optimización avanzada de horarios
- El rendimiento puede disminuir con grandes volúmenes de datos
