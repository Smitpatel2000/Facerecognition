#import face_recognition
from flask import Flask, jsonify, request
import json 
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to khoj project - face recognizer"

@app.route('/recognizeface', methods=['POST'])
def recognizeface():     
    face1 = request.files['face1']
    face2 = request.files['face2']    
    known_image = face_recognition.load_image_file(face1)
    unknown_image = face_recognition.load_image_file(face2)
    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    return str(results)

if __name__ == '__main__':
    app.run()
