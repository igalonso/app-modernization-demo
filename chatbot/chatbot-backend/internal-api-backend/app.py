import flask
import json
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {
        "id": 1,
        "isbn":"9781593279509",
        "title":"Eloquent JavaScript, Third Edition",
        "subtitle":"A Modern Introduction to Programming",
        "author":"Marijn Haverbeke",
        "published":"2018-12-04T00:00:00.000Z",
        "publisher":"No Starch Press",
        "pages":472,
        "description":"JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.",
        "website":"http://eloquentjavascript.net/"
    },
    {
        "id": 2,
        "isbn":"9781491943533",
        "title":"Practical Modern JavaScript",
        "subtitle":"Dive into ES6 and the Future of JavaScript",
        "author":"Nicolás Bevacqua",
        "published":"2017-07-16T00:00:00.000Z",
        "publisher":"O'Reilly Media",
        "pages":334,
        "description":"To get the most out of modern JavaScript, you need learn the latest features of its parent specification, ECMAScript 6 (ES6). This book provides a highly practical look at ES6, without getting lost in the specification or its implementation details.",
        "website":"https://github.com/mjavascript/practical-modern-javascript"
    }
]

# ROUTES
@app.route("/chatbot")
def homepage():
    return {}
@app.route("/chatbot/response")
def getResponse():
    question = str(request.args.get('question'))
    answer = {"response":"Is this your question?: " + question}
    print({"response":"Is this your question?: " + question})
    response = jsonify(answer)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type','application/json')
    return response
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8090)