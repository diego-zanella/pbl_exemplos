from flask import Blueprint

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

@admin.route("/")
def admin_index():
    return "Esse é seu modulo de admin"
