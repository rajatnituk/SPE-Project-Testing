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
    virtualenv \
    git
RUN virtualenv SPE-testing \
    source ./SPE-testing/bin/activate \
RUN pip install face_recognition \
    imutils \
    opencv-python \
    argparse \
    pickle-mixin \
    os-win \
    flask \
RUN git clone https://github.com/rajatnituk/SPE-Project-Testing.git
RUN cd testing \
    python testing.py
