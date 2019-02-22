from flask import Flask, jsonify, request
from flask_cors import CORS
import csv,json

# configuration
DEBUG = True
CUSTOMERS = None
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


@app.route('/chart', methods=['GET'])
def show_chart():
    d = {"sell": [
           {
               "Rate": 0.001425,
               "Quantity": 537.27713514
           },
           {
               "Rate": 0.00142853,
               "Quantity": 6.59174681
           }
]   }
    df = pd.DataFrame(d['sell'])
    print (df)
    df.plot(x='Quantity', y='Rate')
    # response_object = {'status': 'success'}
    # response_object['customers'] = CUSTOMERS
    # return jsonify(response_object)


@app.route('/customers', methods=['GET', 'POST'])
def all_customers():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        CUSTOMERS.append({
            'id': post_data.get('id'),
            'segment': post_data.get('segment'),
            'gender': post_data.get('gender'),
            'years_customer': post_data.get('years_customer'),
            'no_of_complaints': post_data.get('no_of_complaints'),
            'contract_value': post_data.get('contract_value')
        })
        # CUSTOMERS.sort(key=lambda x: float(x['id']), reverse=False);
        response_object['message'] = 'Customer added!'
    else:
        response_object['customers'] = CUSTOMERS
    return jsonify(response_object)


@app.route('/customers/<customer_id>', methods=['PUT', 'DELETE'])
def single_customer(customer_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_customer(customer_id)
        CUSTOMERS.append({
            'id': post_data.get('id'),
            'segment': post_data.get('segment'),
            'gender': post_data.get('gender'),
            'years_customer': post_data.get('years_customer'),
            'no_of_complaints': post_data.get('no_of_complaints'),
            'contract_value': post_data.get('contract_value')
        })
        response_object['message'] = 'Customer updated!'
    if request.method == 'DELETE':
        remove_customer(customer_id)
        response_object['message'] = 'Customer removed!'
    return jsonify(response_object)


def remove_customer(customer_id):
    for customer in CUSTOMERS:
        if customer['id'] == customer_id:
            CUSTOMERS.remove(customer)
            return True
    return False


if __name__ == '__main__':
    filename = 'churn_case_data.csv'
    csvfile = open ('../' + filename, 'r')
    reader = csv.DictReader(csvfile, delimiter=';')
    result = []
    for row in reader:
        result.append(row)
    result = json.dumps(result)
    CUSTOMERS = json.loads(result)
    app.run()
