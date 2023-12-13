from flask import Flask
from flask import request
import requests
import os
import json
app = Flask(__name__)

@app.route("/key")
def get_api_key() -> str:
    secret = "ya29.a0AfB_byDhVs1I0rlG3HNgotYzdJHVFPvldh1exXlBfMYX4WYl0dLfW_EEAUWN6HaqMHmfwEbLrV5oNphxkm5l8V0dnUxj7FfkV2YUPjEh3r7KKHL-_2AOuA9g3_bFWOmbyKbX_FOwsJDiSzriJ1vMNxuaSblcWyAHg8jBw34XJddhLwLqDM3HcClUNCQrGgycKmBJnV-FgNPAHWRC-JW_KiyAtggAXbuzd6Rp-NLotKc58vL7Etxxj99DHHpDJAUO0ATytyJrCBR5y04XNHKeiIGJk4p66G_RR2WRsW5EKO91fbe7OzA2DXckeHt1Iok1mHa-U5pZ0WBFF-nPtAaqMka3XCczz4HMA7V4blgrcAIn8dx8Tqq0HNOmopr5OXjV0sNk2r09pvqc_wEUQP0j7HoMeybzAQaCgYKATcSARISFQHGX2MiC6I9N8WAJ5Eb83-KcDsNhQ0421"
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
    return "<p style="color: blue;">Use POST to add</p>" # replace with form template
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
