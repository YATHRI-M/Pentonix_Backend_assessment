from flask import Flask, request, jsonify

api = Flask(__name__)# Creating Flask web application named as api

# Creating In-memory database for departments table
departments = {
    10: 'Admin',
    20: 'Accounts',
    30: 'Sales',
    40: 'Marketing',
    50: 'Purchasing'}
# Creating In-memory database for employees table
employees = {
    1: {'ENAME': 'Amal', 'DNO': 10, 'SALARY': 30000},
    2: {'ENAME': 'Shyamal', 'DNO': 30, 'SALARY': 50000},
    3: {'ENAME': 'Kamal', 'DNO': 40, 'SALARY': 10000},
    4: {'ENAME': 'Nirmal', 'DNO': 50, 'SALARY': 60000},
    5: {'ENAME': 'Bimal', 'DNO': 20, 'SALARY': 40000},
    6: {'ENAME': 'Parimal', 'DNO': 10, 'SALARY': 20000} }

@api.route('/api/employee')#Defining the route to end-point employee for 1st api and when the user request with this end point then get_employee_by_eno() will be triggred
def get_employee_by_eno():
    """Using try and exception block verifying the user request, if the user request is valid the the try block will display the output in JSON form
     and if the user try to make bad request it will be handled in exception block  """
    try:
        eno = int(request.args.get('ENO')) # extracting the ENO from the url
        employee = employees.get(eno)# Fetching the details of the employee whose ENO is requested and strong in an variable
        if employee:
            return jsonify(employee)
        else:
            return jsonify({'error': 'Employee record not found'}), 404 #if user make good request and the requested record in not present in the database it returns 404 error
    except ValueError:
        return jsonify({'error': 'Invalid ENO'}), 400

@api.route('/api/employees')#Defining the route end point for 2nd api
def get_employees_by_dname():
    try:
        dname = request.args.get('DNAME')
        matching_employees = [employee for employee in employees.values() if departments.get(employee['DNO']) == dname]
        if matching_employees:
            return jsonify(matching_employees)
        else:
            return jsonify({'error': 'Employees not found for DNAME'}), 404
    except ValueError:
        return jsonify({'error': 'Invalid DNAME'}, 400)

if __name__ == '__main__':
    api.run(port=9000)#Addresing the Flask server to run only in port 9000
