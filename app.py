from flask import Flask, render_template, request
from rivescript import RiveScript
import os.path
import kmean

cluster = kmean.Cluster()

brain = os.path.dirname(__file__)


bot = RiveScript()
bot.load_directory(brain)
bot.sort_replies()

answerkey = {"tech":[1,2,4,4,4,1,3,1,3,2],"verbal":[2,2,2,2,2,2,3,1,3,2]}
app = Flask(__name__)
useranswer = {"tech":[],"verbal":[]}
test = "tech"
count = 0

def evaluate(useranswer):
    d =[]
    c = 0
    for i in range(len(answerkey["tech"])):
        if answerkey["tech"][i] == useranswer["tech"][i]:
            c+=1
    d.append(c)
    c = 0
    for i in range(len(answerkey["verbal"])):
        if answerkey["verbal"][i] == useranswer["verbal"][i]:
            c+=1
    d.append(c)
    return d
    
@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    global count,test
    userText = request.args.get('msg')

    if userText.isdigit():
        if int(userText) > 0 and int(userText) < 5:
            count += 1
            useranswer[bot.get_variable("currenttopic")].append(int(userText))
        print(useranswer)
    
    if bot.get_variable("currenttopic") == "done":
        d = evaluate(useranswer)
        return str("verbal score: "+str(d[1])+"\ntechnical score: "+str(d[0])+"\nYou may be placed in "+cluster.predict(d)+" company")
    return str(bot.reply('localuser',userText)) 

if __name__ == "__main__":    
    app.run()


