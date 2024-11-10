FROM ollama/ollama:latest

# Install curl
RUN apt-get update && apt-get install -y curl

# Copy all files from the current directory to the /app directory in the container
COPY ./ /app/

# Create a directory for models
RUN mkdir -p /app/models

# Expose the port for the application
EXPOSE 11434
