from flask import Flask, request
import json
from DbRepo import DbRepo
from db_config import local_session
from Customers import Customers

repo = DbRepo(local_session)
app = Flask(__name__)

def convert_to_json(_list):
    json_list = []
    for i in _list:
        _dict = i.__dict__
        _dict.pop('_sa_instance_state', None)
        json_list.append(_dict)
    return json_list

def add_customer(_input):
    repo.add(Customers( id=_input['id'],
                        first_name=_input['first_name'],
                        last_name=_input['last_name'],
                        address=_input['address']))
    return '{"status": "great success!"}'

def update_customer(_input, id):
    customers_json = convert_to_json(repo.get_all(Customers))
    for c in customers_json:
        if c["id"] == id:
            c["id"] = _input["id"] if "id" in _input.keys() else None
            c["first_name"] = _input["first_name"] if "first_name" in _input.keys() else None
            c["last_name"] = _input["last_name"] if "last_name" in _input.keys() else None
            c["address"] = _input["address"] if "address" in _input.keys() else None
            repo.update_by_id(Customers, Customers.id, id, c)
    return '{"status": "success"}'

# localhost:5000/
# static page
# dynamic page
@app.route("/")
def home():
    print('hi')
    return '''
        <html>
            <h3>*************************************************</h3>
            <h1>REST API MUST HOMEWORK<h1>
            <h3>*************************************************</h3>
            <h1>RONEN FROMCHUK</h1>
            <h3>**********************************</h3>
            <h1>CUSTOMERS</h1>
            <h3>**********************</h3>
        </html>
    '''


# url/<resource> <--- GET POST
@app.route('/customers', methods=['GET', 'POST'])
def get_or_post_customer():
    global new_customer
    if request.method == 'GET': return json.dumps(convert_to_json(repo.get_all(Customers)))
    if request.method == 'POST':
        new_customer = request.get_json()
    return add_customer(new_customer)

@app.route('/customers/<int:id>', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def get_customer_by_id(id):
    if request.method == 'GET':
        for c in convert_to_json(repo.get_all(Customers)):
            if c["id"] == id:
                return json.dumps(c)
        return '{}'
    if request.method == 'PUT':
        updated_new_customer = request.get_json()
        return add_customer(updated_new_customer)
    if request.method == 'PATCH':
        updated_customer = request.get_json()
        if repo.get_by_id(Customers, id) != None: return update_customer(updated_customer, id)
        return '{"status": "not found"}'
    if request.method == 'DELETE':
        deleted_customer = request.get_json()
        customers_json = convert_to_json(repo.get_all(Customers))
        for c in customers_json:
            if c["id"] == id:
                repo.delete_by_id(Customers, Customers.id, id)
        return f'{json.dumps(deleted_customer)} deleted'
    return '{"status": "not found"}'

app.run()