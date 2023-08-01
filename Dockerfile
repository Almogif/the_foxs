# Use the official Python image as the base
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files into the container
COPY game.py /app/
COPY graphics /app/graphics
COPY fonts /app/fonts

# Install pygame and its dependencies
RUN apt-get update && apt-get install -y \
    python-dev \
    python3-dev \
    build-essential \
    libsdl-dev \
    libsdl-image1.2-dev \
    libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev \
    libsmpeg-dev \
    python3-numpy \  # Corrected typo: changed from python-numpy to python3-numpy
    subversion \
    ffmpeg \
    libportmidi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install the specified version of pygame
RUN pip install pygame==1.9.6

# Define the entry point command to run your game
CMD ["python", "game.py"]
