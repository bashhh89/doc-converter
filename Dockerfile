# Start with a standard Python image
FROM python:3.9-slim

# Set the working directory inside our service
WORKDIR /app

# Update the system and install pandoc
RUN apt-get update && apt-get install -y pandoc

# Copy the requirements file
COPY requirements.txt .

# Install the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of our application code
COPY . .

# Expose port 5001 so we can communicate with the service
EXPOSE 5001

# Define the command to run when the service starts
CMD ["python", "app.py"]