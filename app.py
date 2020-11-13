import flask
from flask_cors import CORS
import json
import pdfkit
import uuid

# Initializing flask app
app = flask.Flask(__name__)
# Adding cors to flask
CORS(app)

options = {
    'page-size': 'A3',
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',    
    'orientation': 'landscape',
    'encoding': 'UTF-8'
}

# Controller-1
@app.route("/", methods=['GET'])
def get_alive():
    print("It's alive!");
    return "It's alive"


# Controller-2
@app.route("/report", methods=['POST'])
def get_report():
    fileName = "files/" + str(uuid.uuid4()) + ".pdf"
    data = flask.request.data
    body = json.loads(data)
    url = body["url"]        
    print("Convertendo a url:" + url)

    if "orientation" in body:
        options["orientation"] = body["orientation"]    
    
    
    
    pdfkit.from_url(url, fileName, options=options)    
    return flask.send_file(fileName, as_attachment=True)

# Running the api
if __name__ == '__main__':
    app.run(port=5000)