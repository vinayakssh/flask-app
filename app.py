from flask import Flask, render_template_string

app = Flask(__name__)

students = []

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Student Tracker</title>
  <style>
    body { font-family: Arial; max-width: 500px; margin: 50px auto; }
    input { padding: 8px; margin: 5px; }
    button { padding: 8px 16px; background: #4CAF50; color: white; border: none; cursor: pointer; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
    th { background: #f2f2f2; }
  </style>
</head>
<body>
  <h2>Student Grade Tracker</h2>
  <form method="POST" action="/add">
    <input name="name" placeholder="Student name" required />
    <input name="grade" placeholder="Grade (e.g. A)" required />
    <button type="submit">Add Student</button>
  </form>
  <table>
    <tr><th>Name</th><th>Grade</th></tr>
    {% for s in students %}
    <tr><td>{{ s.name }}</td><td>{{ s.grade }}</td></tr>
    {% endfor %}
  </table>
  <p style="color:gray; font-size:12px;">Running on Kubernetes - v1</p>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML, students=students)

@app.route('/add', methods=['POST'])
def add():
    from flask import request, redirect
    students.append({'name': request.form['name'], 'grade': request.form['grade']})
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
