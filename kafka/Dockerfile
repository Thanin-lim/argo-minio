# Use a Python 3.8 image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the local requirements file to the container
# (assuming you have a `requirements.txt` in your local directory)
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port that the application will use (optional)
EXPOSE 8080

# Set the entry point to run the application
CMD ["bash"]
