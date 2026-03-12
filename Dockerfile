# Use a light Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from your folder to the container
COPY . .

# Manually install the libraries needed for a monitoring app
RUN pip install flask prometheus_client

# Expose port 5000
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]