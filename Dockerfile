# Using official Debian 10 as base image
FROM debian:10

# Maintainer information
LABEL maintainer="ricardo.saad@proton.me"

# Update the package index and install required packages
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    bzip2 \
    ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    nano \
    less \
    net-tools \
    iputils-ping

# Set the PATH to include Miniconda
ENV PATH /opt/conda/bin:$PATH

# Create a new conda environment and install packages from conda
RUN conda create --name myenv \
    && conda activate myenv \
    && conda install numpy  \
    && conda install pandas \
    && conda install matplotlib

# Install packages from pip
RUN pip install scikit-learn  \
    && pip install

# Set the working directory
WORKDIR /root

# Set the default command to run when starting the container
CMD ["bash"]
