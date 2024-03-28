# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5007

ARG DB_PORT=8889
# Define environment variable
ENV DB_URL=mysql+mysqlconnector://root:root@host.docker.internal:${DB_PORT}/schedulingDB

# Run the Flask application
CMD ["python", "updateavailability.py"]
