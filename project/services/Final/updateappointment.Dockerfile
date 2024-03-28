# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5008

# Define environment variable
ENV DB_URL=mysql+mysqlconnector://root:root@host.docker.internal:8889/APPOINTMENTDB

# Run the Flask application
CMD ["python", "updateappointment.py"]