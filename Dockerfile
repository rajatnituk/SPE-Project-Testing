FROM rajatiiitb/base_image

RUN pip install flask \
    logging
RUN git clone https://github.com/rajatnituk/SPE-Project-testing.git
RUN git clone https://github.com/rajatnituk/SPE-Pickle-file.git
EXPOSE 5000

#CMD ["python","SPE-Project-testing/testing.py"]

