# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install any dependencies (from requirements.txt, if any)
RUN pip install --no-cache-dir -r requirements.txt

# Run the script when the container launches
CMD ["python", "app.py"]
