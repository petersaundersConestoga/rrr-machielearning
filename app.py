from flask import Flask, escape, request, json;
from copy import deepcopy;
import HelloController
import TrumpController

app=Flask(__name__)

story = {
    "generator": "",
    "input":"",
    "story":""
}

@app.route('/')
async def hello():
    name=request.args.get("name", "World")
    return f'Hello, {HelloController.foo(2)} {escape(name)}!'

@app.route('/trump', methods=['GET','POST'])
async def trump():
    mystory = deepcopy(story)
    mystory["generator"] = "trump"

    if request.method == 'POST':
        data = json.loads(request.data)
        mystory["input"] = data["input"]
        mystory["story"] = TrumpController.tweet(mystory["input"]) #"this other story"
    elif request.method == 'GET':
        mystory["story"] = TrumpController.tweet() #"this cool story"
        
    mystory = json.dumps(mystory)
    return mystory
    
if __name__=="__main__":
    app.run(
        host="0.0.0.0",
        port="8082",
    )
