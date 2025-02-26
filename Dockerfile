# Use the official TensorFlow image
FROM tensorflow/tensorflow:2.12.0

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install additional Python dependencies
RUN pip install --no-cache-dir numpy pillow streamlit

EXPOSE 8501

# Set the command to run your application
CMD ["streamlit", "run", "main.py"]