from flask import Flask, request, jsonify
from jonapp import create_app

#instaniate app
app = create_app()


#these routes below were just other examples, you'd ideally move them to their own blueprints in your app

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


