# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5003

# Define environment variable
ENV DB_URL=mysql+mysqlconnector://caremd@host.docker.internal:3306/USERDETAILS

# Run the Flask application
CMD ["python", "user_details.py"]
