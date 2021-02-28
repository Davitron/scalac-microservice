from flask import Flask, jsonify, request
import requests, os

app = Flask(__name__)
app_port = os.environ['PORT']

def process(joke):
    formatted = {}
    if len(joke):
        desc = joke[0].split(" ")
        formatted["id"] = desc[0].strip()
        formatted["link"] = desc[1].strip()
        formatted["joke"] = '\n'.join(joke[1:]).strip()
    return formatted

@app.route('/')
def hello():
    return "Microservice is active!!"

@app.route('/hello')
def message():
    return "HELLO USER now"

@app.route('/getjokes')
def getJokes():
    jokes_count = request.args.get("count") or 100

    s = requests.Session()
    response = []
    with s.get("http://bash.org.pl/text", headers=None, stream=True) as resp:
        joke = []
        for line in resp.iter_lines():
            if line.decode("utf-8") != "%":
                if len(line.decode("utf-8")) != 0:
                    joke.append(line.decode("utf-8"))
            else:
                processed = process(joke)
                response.append(processed)
                joke.clear()
                if len(response) == int(jokes_count):
                   break 
    return { "jokes": response }
                


if __name__ == '__main__':
    app.run(port=app_port)