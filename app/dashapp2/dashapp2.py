from flask import Blueprint, render_template

bp = Blueprint('dashapp2', 
               __name__, 
               template_folder = 'templates', 
               url_prefix="/dashapp2")

@bp.route('/', methods=['GET'])
def main():
    return render_template('dashapp2.jinja2', title="Dashapp Page")