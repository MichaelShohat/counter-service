 #!flask/bin/python
from flask import Flask, request, request_started

app = Flask(__name__)
counter_post = 0
counter_get = 0
@app.route('/', methods=["POST", "GET"])
def index():
    global counter_post, counter_get
    if request.method == "POST":
        counter_post+=1
        return "Hmm, Plus 1 please "
    else:
        counter_get+=1
        return str(f"Our POST counter is: {counter_post} and our GET counter is: {counter_get}")
if __name__ == '__main__':
    app.run(debug=True,port=80,host='0.0.0.0')
