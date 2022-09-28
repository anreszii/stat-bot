from flask import Flask,request,jsonify
import cv2

from recognizer import recognizer

app = Flask(__name__)



@app.route("/recog",methods=["POST"])
def recog():
    print("let it go")
    request.files.get("img").save("qwe.jpg")
    resposne = recognizer("qwe.jpg")
    return jsonify(resposne)



@app.route("/")
def home():
    print("hello")
    return "<h1>Img recognizer</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)