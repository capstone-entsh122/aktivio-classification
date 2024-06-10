# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port the app will run on
EXPOSE 8080

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]