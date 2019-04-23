import face_recognition
import argparse
import pickle
import cv2
import os
import logging
from flask import Flask,request, render_template, send_from_directory
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def testing(image_name):
	

	ap = argparse.ArgumentParser()
	ap.add_argument("-e", "--encodings", default="../SPE-Pickle-file/encoding.pickle",help="path to serialized db of facial encodings")
	ap.add_argument("-i", "--image", default=image_name,help="path to input image")
	ap.add_argument("-d", "--detection-method", type=str, default="cnn",help="face detection model to use: either `hog` or `cnn`")
	args = vars(ap.parse_args())

	print("[INFO] loading encodings...")
	data = pickle.load(open(args["encodings"], "rb"))

	image = cv2.imread(args["image"])
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


	print("[INFO] recognizing faces...")
	boxes = face_recognition.face_locations(rgb,model=args["detection_method"])
	encodings = face_recognition.face_encodings(rgb, boxes)

	names = []


	for encoding in encodings:
	
		matches = face_recognition.compare_faces(data["encodings"],encoding)
		name = "Unknown"


		if True in matches:
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			name = max(counts, key=counts.get)
	
	
		names.append(name)
	for i in range(len(names)):
		if(names[i]!='Unknown'):
			return "Criminal"
		else: 
			return "Not Criminal"
	# for ((top, right, bottom, left), name) in zip(boxes, names):
	# 	cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
	# 	y = top - 15 if top - 15 > 15 else top + 15
	# 	cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)

	# cv2.imshow("Image", image)
	# cv2.waitKey(0)

# @app.route("/")
# def hello():
#     return render_template('home.html')
@app.route("/")
def index():
    return render_template("upload.html")
@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
        test=testing(destination)
    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete_display_image.html", image_name=filename,test=test)    

    
    #return render_template('home.html',test=test)


if __name__ == '__main__':
    logging.basicConfig(filename='log',level=logging.DEBUG)
    app.run(debug=True,host="0.0.0.0")
