FROM tensorflow/tensorflow:latest-gpu

RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install \
    jupyter \
    scikit-learn \
    pandas \
    numpy \
    matplotlib

CMD ["jupyer", "notebook", "--ip", "0.0.0.0", "--port", "8888", "--allow-root"]

# docker build -t <name> .
# docker run --gpus all -p 8888:8888 <name>
