from flask import Flask,jsonify,request
app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'name': u'Rahul',
        'number': u'8473926791', 
        'done': False
    },
    {
        'id': 2,
        'name': u'Rohan',
        'number': u'3498723986', 
        'done': False
    }
]
@app.route("/")
def hello_world():
    return "Hello i am Astitva"
@app.route ("/getdata")
def getdata():
    return jsonify({"data":tasks})
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'number': request.json.get('number', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
if(__name__ == "__main__"):
    app.run(debug=True)