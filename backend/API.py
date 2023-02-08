from flask import Flask
from flask import jsonify
from flask import  render_template
from dataBook import export_data_me
from dataBook import export_data_person_simple

app = Flask(__name__)

# endpoints
@app.route("/")
def index():
    return "<a href='/getinfo'>view endpoints</a>"

@app.route("/getinfo")
def getInfo():
    # return "<p>endpoints: 1.-/person/name_user 2.- /normal</p>"
    return jsonify({"endpoint_1": "/person/name_user", "endpoints_2": "/normal"})

@app.route("/person/<string:book_name>", methods=['POST'])
def getData(book_name):
    if(book_name == "Hiram" or "hiram"):
        return jsonify({"stacks_hiram": export_data_me()})
        # ?
    # elif(book_name != "Hiram" or "hiram"):
    #     return jsonify({"stacks_normal_person": export_data_person_simple()})

# books data
@app.route("/normal", methods=['GET'])
def getBooks():
    return jsonify({"stack": export_data_person_simple()})

# error handlers
@app.errorhandler(404)
def notFound(e):
    return "not found",404

# run app
if __name__ == "__main__":
    app.run(debug=True)