from flask import Flask
import json
import time
from flask import render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
    
if __name__ == "__main__":

    
    @app.route("/getData/")
    def getData():
      print "getting the data"
      output = {"out":"This is the data"}
      return json.dumps(output)
    
    app.run(host='0.0.0.0',port=5000,debug=True,threaded=True)