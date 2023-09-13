from flask import Flask, jsonify, request

 

app = Flask(__name__)

 

# Sample data (you can replace this with your data)

data = [

    {"id": 1, "name": "Item 1"},

    {"id": 2, "name": "Item 2"},

    {"id": 3, "name": "Item 3"}

]

 

# Route to get all items

@app.route('/items', methods=['GET'])

def get_items():

    return jsonify({"items": data})

 

# Route to get a specific item by ID

@app.route('/items/<int:item_id>', methods=['GET'])

def get_item(item_id):

    item = next((item for item in data if item['id'] == item_id), None)

    if item:

        return jsonify({"item": item})

    else:

        return jsonify({"message": "Item not found"}), 404

 

if __name__ == '__main__':

app.run(debug=True)
