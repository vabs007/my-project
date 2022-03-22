from flask import Flask, jsonify, request

app = Flask(__name__)
Employee = [
    {
        'name': 'emp 1',
        'emplists': [
            {
                'name': 'Rajesh',
                'input': 'Sanitized'
            }
        ]
    },
    {
        'name': 'emp 2',
        'emplists': [
            {
                'name': 'Mahesh',
                'input': 'Sanitized'
            }
        ]
    }
]



@app.route('/employee', methods=['POST'])
def create_employee():
    request_data = request.get_json()
    new_employee = {
        'name': request_data['name'],
        'emplists': []
    }
    Employee.append(new_employee)
    return jsonify(new_employee)


@app.route('/employee/<string:name>')
def get_employee_name(name):
    for employee in Employee:
        if(employee['name'] == name):
            return jsonify(employee)
    return jsonify({'message': 'unsanitized'})


@app.route('/employee')
def get_all_employee_name():
    return jsonify({'Employee': Employee})


@app.route('/employee/<string:name>/emplist', methods=['POST'])
def create_employee_emplist(name):
    request_data = request.get_json()
    for employee in Employee:
        if(employee['name'] == name):
            new_emplist = {
                'name': request_data['name'],
                'input': request_data['input']
            }
            employee['emplists'].append(new_emplist)
            return jsonify(new_emplist)
    return jsonify({'message':'unsanitized'})


@app.route('/employee/<string:name>/emplist')
def get_employee_emplist(name):
    for employee in Employee:
        if(employee['name'] == name):
            return jsonify(employee['emplists'])
    return jsonify({'message': 'unsanitized'})



app.run(port=8000)
