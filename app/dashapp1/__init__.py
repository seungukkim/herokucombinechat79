from flask import Blueprint, render_template

bp = Blueprint('dashapp1', 
               __name__, 
               template_folder = 'templates')