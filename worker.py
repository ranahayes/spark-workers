from flask import Flask
from flask import request
import requests
import os
import json
app = Flask(__name__)

@app.route("/key")
def get_api_key() -> str:
    secret = "ya29.a0AfB_byCJpM-BkZQuFmEAKk_3b24OuHOpL6GQ-fFMpXlVzusfebMVGUHGtPLn7AkqLBNIsNuZKbd_Fk4P9kFMlc4f5qqRLk-M5wOTEXlEZPlggS-Vs4syT9SvseI-x3Aw6TDJIktFeQIHzI1zOtxK7SzCjz9ZQ8-9Rmkuu8GnbUrrGu2QIefGw-JbmviG7w4m-yQqfkvgEkvDMSJ-SCq6V0rNaX9FZZlI88oPWDZ8J_gLfDzre8IpbX6KpDuD8PI5n3lQP4ixKyfpa1WCCh35oiZS6zLKl9SG-pprCfyx4hyWduZbvR_rEfQRpWlPiFMehfrPs1gYfqr_QdWBe7l6qnp3zGE5kqV3crHeYMGWqSLrOGdXJ7lQGzuIX5VBGrdQNK6YYiiIf1RqPOIs2wWGty9YDwVI_hMaCgYKAYASARISFQHGX2Mi4HbqHl2oGjuZXVUfR6Sjcg0422"
    return secret

      
@app.route("/")
def hello():
    return "Add workers to the Spark cluster with a POST request to add"

@app.route("/test")
def test():
    return(get_api_key())
    return "Test" 

@app.route("/add",methods=['GET','POST'])
def add():
  if request.method=='GET':
    return "Use post to add" # replace with form template
  else:
    token=get_api_key()
    ret = addWorker(token,request.form['num'])
    return ret


def addWorker(token, num):
    with open('payload.json') as p:
      tdata=json.load(p)
    tdata['name']='slave'+str(num)
    data=json.dumps(tdata)
    url='https://www.googleapis.com/compute/v1/projects/spark-408012/zones/europe-west1-b/instances'
    headers={"Authorization": "Bearer "+token}
    resp=requests.post(url,headers=headers, data=data)
    if resp.status_code==200:     
      return "Done"
    else:
      print(resp.content)
      return "Error\n"+resp.content.decode('utf-8') + '\n\n\n'+data



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
