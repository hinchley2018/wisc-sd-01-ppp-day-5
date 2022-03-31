from flask import Flask, request, jsonify
from jonapp import create_app

#instaniate app
app = create_app()

#in-memory pets 
pets = []

@app.route("/")
def index():
    print(request.query_string) 
    name = request.args.get("name")
    shoe = request.args.get("shoe")
    return f"Hello {name} my shoe is: {shoe}"

#get /pets
@app.route("/pets")
def get_pets():
    #good tutorial on returning json https://koenwoortman.com/python-flask-return-json-response
    return jsonify(pets)

#POST /pets
@app.route("/pets", methods=['POST'])
def create_pets():
    #good tutorial for handling POST requests with JSON payloads https://pythonise.com/series/learning-flask/working-with-json-in-flask
    #handle bad requests
    if not request.is_json:
        return "Request was not JSON",400
    # grab off the request body as json aka a dict in python
    reqBody = request.get_json()
    print("Recieved POST /pets ",reqBody)
    pets.append(reqBody)
    print("updated pets: ",pets)
    return f"created a pet at index {len(pets) -1}"


#explanation back to js routes
'''
app.get('/pets', (req, res) => {
    res.send(req.body)
})
'''

# GET /fruits/<name> 
# if parameter is not there it won't match -> 404
@app.route('/fruits/<name>')
def get_fruit_by_name(name):
    return f"{name}"

# GET /users/<userId>
# if parameter is not an int -> 404
@app.route('/users/<int:userId>')
def get_users_by_id(userId):
    return f"{userId}"


