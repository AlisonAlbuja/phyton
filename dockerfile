# Use the official Python base image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the files from your local project to the container
COPY . .

# Install the Python dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 (default port for Flask)
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
