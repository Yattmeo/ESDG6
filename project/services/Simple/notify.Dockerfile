# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5005

# Define environment variable (need to update auth token)
ENV TWILIO_ACCOUNT_SID='ACea65d1e2ea1abe9ca0e8c443e0cbdc79'
ENV TWILIO_AUTH_TOKEN=your_auth_token_here

# Run the Flask application
CMD ["python", "notify.py"]