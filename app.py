from flask import Flask, request

# app factory
def create_app():
    #create app
    app = Flask(__name__)

    #config
    
    return app

#create an app instance
app = create_app()

@app.route("/")
def index():
    print(request.query_string) 
    name = request.args.get("name")
    shoe = request.args.get("shoe")
    return f"Hello {name} my shoe is: {shoe}"

#get /pets
@app.route("/pets")
def get_pets():
    return "My pets list"

#POST /pets
@app.route("/pets", methods=['POST'])
def create_pets():
    return "Recieved POST create a pet"


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


