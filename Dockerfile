
# Use the official Python image as the base
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files into the container
COPY game.py /app/
COPY graphics /app/graphics
COPY fonts /app/fonts

# Update the package manager and install necessary dependencies for pygame
RUN apt-get update && apt-get install -y \
    libsdl1.2-dev \
    libsdl-image1.2-dev \
    libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev \
    libsmpeg-dev \
    libportmidi-dev \
    libavformat-dev \
    libswscale-dev

# Install the specified version of pygame
RUN pip install pygame==1.9.6

# Define the entry point command to run your game
CMD ["python", "game.py"]
