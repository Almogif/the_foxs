
# Use the official Python image as the base
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (pygame requirements)
RUN apt-get update && apt-get install -y \
    libsdl1.2-dev \
    libsdl-image1.2-dev \
    libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev \
    libsmpeg-dev \
    python3-numpy \
    subversion \
    ffmpeg \
    libswscale-dev \
    libportmidi-dev \
    libavformat-dev \
    libavcodec-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

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
    python-numpy \
    subversion \
    ffmpeg \
    libportmidi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
RUN pip install pygame==1.9.6  # Specify the version of pygame to be installed

# Define the entry point command to run your game
CMD ["python", "game.py"]
