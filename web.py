from flask import Flask, request, redirect, render_template_string
from app import add_note, list_notes

app = Flask(__name__)

PAGE = """
<h1>Notes</h1>
<form method="post" action="/add">
  <input name="text" placeholder="Write a note" required>
  <button type="submit">Add</button>
</form>
<ul>
{% for note_id, text in notes %}
  <li>{{ note_id }}: {{ text }}</li>
{% else %}
  <li>No notes yet.</li>
{% endfor %}
</ul>
"""

@app.route("/")
def index():
    return render_template_string(PAGE, notes=list_notes())

@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text", "").strip()
    if text:
        add_note(text)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
