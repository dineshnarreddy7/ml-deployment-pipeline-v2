# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app
COPY . .

# Expose port for uvicorn
EXPOSE 8000

# Command to run the API with uvicorn
CMD ["uvicorn", "serving.main:app", "--host", "0.0.0.0", "--port", "8000"]
