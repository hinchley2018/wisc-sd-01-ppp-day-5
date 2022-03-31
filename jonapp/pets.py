from flask import Flask, request, jsonify, Blueprint, render_template
#in-memory pets 
pets = []

#node refrseher
'''
app.use("/pets" ,petsController)
const router = require("express").Router()

// GET /pets/
router.get("/",(req,res) => {})
'''

pets_bp = Blueprint(
    'pets',
    __name__,
    url_prefix="/pets"
)

@pets_bp.route("/")
def view_pets():
    return render_template(
        "pets.html",
        pets=pets
    )

#get /pets/list
@pets_bp.route("/list")
def get_pets():
    #good tutorial on returning json https://koenwoortman.com/python-flask-return-json-response
    return jsonify(pets)

@pets_bp.route("/create-pets")
def view_create_pets():
    return render_template(
        "create-pets.html",
    )

#POST /pets
#NOTE: in the slides it has methods=('POST') this is incorrect syntax python expects a list
@pets_bp.route("", methods=['POST'])
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
