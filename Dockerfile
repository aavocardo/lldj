# Use an official Ubuntu 18.04 as a parent image
FROM nvidia/cuda:11.4.2-cudnn8-runtime-ubuntu18.04

# Set the working directory to /app
WORKDIR /app

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3-pip python3-dev python3-venv && \
    apt-get install -y curl && \
    apt-get install -y wget && \
    apt-get install -y git && \
    apt-get install -y libsm6 libxext6 libxrender-dev

# Install TensorFlow and its dependencies
RUN pip3 install tensorflow-gpu==2.7.0

# Copy the current directory contents into the container at /app
COPY . /app

# Set environment variables
ENV PYTHONPATH=$PYTHONPATH:/app

# Run the command when the container starts
CMD ["python3", "app.py"]
