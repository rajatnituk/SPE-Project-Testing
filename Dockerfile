FROM ubuntu:18.04
#install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN apt-get update && apt-get install -y \
    python3.4 \
    python3-pip \ 
    python \
    python-pip \
    cmake \
    git
RUN pip install face_recognition \
    imutils \
    opencv-python \
    argparse \
    pickle-mixin \
    os-win
RUN git clone https://github.com/MS2017009/SPE-Project.git
