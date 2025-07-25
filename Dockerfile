# Use Python 3.11 slim as the base image - slim version reduces image size while maintaining functionality
FROM python:3.11-slim

# Set the working directory inside the container where our application will live
WORKDIR /app

# Copy requirements file first to leverage Docker's cache mechanism
# This way, if requirements don't change, we don't need to reinstall dependencies
COPY requirements.txt .

# Install Python dependencies
# --no-cache-dir flag reduces the image size by not storing the pip cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 which is the default port for FastAPI applications
EXPOSE 8000

# Command to run the FastAPI application using uvicorn
# --host 0.0.0.0 makes the server accessible from outside the container
# --port 8000 specifies the port to run the server on
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]