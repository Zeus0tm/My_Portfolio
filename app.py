"""BALA portfolio — native HTML, CSS, and Python/Flask. No JavaScript required."""
from flask import Flask, abort, redirect, render_template, request
app = Flask(__name__)
PAGES = {"about", "skills", "projects", "journey", "contact"}
CATEGORIES = {"All", "Street", "Landscape", "Nature", "Sport"}
@app.get("/")
def home():
    return render_template("index.html")
@app.get("/index")
def index_alias():
    return redirect("/", code=301)
@app.get("/photography")
def photography():
    category = request.args.get("category", "All")
    if category not in CATEGORIES:
        abort(400)
    return render_template("photography.html", category=category)
@app.get("/project/<int:index>")
def project(index):
    if not 0 <= index < 3:
        abort(404)
    return render_template(f"project-{index}.html")
@app.get("/photo/<int:index>")
def photo(index):
    if not 0 <= index < 4:
        abort(404)
    return render_template(f"photo-{index}.html")
@app.get("/resume")
def resume():
    return render_template("resume.html")
@app.get("/<page>")
def content(page):
    if page not in PAGES:
        abort(404)
    return render_template(f"{page}.html")
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
