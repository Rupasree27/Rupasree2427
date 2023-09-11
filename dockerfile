# Use an official Python runtime as a parent image
FROM python:3.8-slim
# Set the working directory in the container
WORKDIR /testwork



COPY person.xml /testwork/
# Copy the Python script to the container
COPY getapi.py /testwork/

#Install flask
Run pip install flask

# Run the Python script when the container launches
ENTRYPOINT ["python", "/testwork/getapi.py"]

