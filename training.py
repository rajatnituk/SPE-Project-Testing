#made changes
#to run the file python training.py --dataset dataset --encodings encoding.pickle
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,help="path to input directory of faces + images")
ap.add_argument("-e", "--encodings", required=True,help="path to serialized db of facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())
print("reading the face images")
imagePaths = list(paths.list_images(args["dataset"]))


knownEncodings = []
knownNames = []

for (i, imagePath) in enumerate(imagePaths):
	
	print("processing the faces {}/{}".format(i + 1,len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]
 	
	
	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	boxes = face_recognition.face_locations(rgb,model=args["detection_method"])
	 
	encodings = face_recognition.face_encodings(rgb, boxes)
 
	for encoding in encodings:
		knownEncodings.append(encoding)
		knownNames.append(name)
print("[serializing encodings...")
data = {"encodings": knownEncodings, "names": knownNames}
f = open(args["encodings"], "wb")
f.write(pickle.dumps(data))
f.close()

