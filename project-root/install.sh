#!/bin/bash

# Ensure script is run as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Update and upgrade the system
echo "Updating and upgrading the system..."
apt-get update && apt-get upgrade -y

# Install Python3 and pip
echo "Installing Python3 and pip..."
apt-get install python3 python3-pip -y

# Install Docker
echo "Installing Docker..."
apt-get install docker.io -y

# Install Docker Compose
echo "Installing Docker Compose..."
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Clone the repository
echo "Cloning the repository..."
git clone <repository-url> project-root
cd project-root

# Install project dependencies
echo "Installing project dependencies..."
pip3 install -r requirements.txt

# Build and run the Docker container
echo "Building and running the Docker container..."
docker-compose up --build -d

echo "Installation complete. The application is now running."
