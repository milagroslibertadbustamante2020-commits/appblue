from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__, template_folder='templates')

ENTRADAS = {
    1: "Mi primera entrada en Flask",
    2: "Blueprints para ordenar el proyecto",
    3: "Plantillas con Jinja2 y extends",
}

@blog_bp.route('/entrada/<int:id>')
def entrada(id):
    titulo = ENTRADAS.get(id, "Entrada no encontrada")
    return render_template('entrada.html', id=id, titulo=titulo)
