# Use the official TensorFlow Docker image as a base
FROM tensorflow/tensorflow:latest-gpu-jupyter

# Install dependencies
RUN pip install matplotlib numpy pandas scikit-learn

# Set the working directory
WORKDIR /app

# Copy the code to the working directory
COPY . .

# Set the entrypoint to start Jupyter
ENTRYPOINT ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
