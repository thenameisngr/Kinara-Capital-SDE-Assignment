# app.py

from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

students = []

# Load student details from a CSV file
def load_students():
    file_path = 'C:\\Users\\NGR\\Desktop\\Kinara Assignment\\assignment\\students.csv'
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

# Load Student Details API
@app.route('/api/students', methods=['GET'])
def get_students():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('pageSize', 10))
    start_index = (page - 1) * page_size
    end_index = page * page_size
    paginated_students = students[start_index:end_index]

    return jsonify({
        'page': page,
        'pageSize': page_size,
        'total': len(students),
        'data': paginated_students
    })

# Server-side Filtering API
@app.route('/api/students/filter', methods=['GET'])
def filter_students():
    name = request.args.get('name')
    marks = request.args.get('marks')
    filtered_students = students

    if name:
        filtered_students = [student for student in filtered_students if name.lower() in student['name'].lower()]

    if marks:
        filtered_students = [student for student in filtered_students if int(student['marks']) >= int(marks)]

    return jsonify(filtered_students)

if __name__ == '__main__':
    load_students()
    app.run(debug=True)
