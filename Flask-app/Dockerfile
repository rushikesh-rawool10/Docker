# Docker base image with python installed
FROM python:3.9

#working directory for the app inside the container
WORKDIR app/

#copy the code from system to container
COPY app.py .

#install required libraries
RUN pip install flask

#Run the appliucation
CMD ["python" "app.py"]
