# Use the official Python image as the base
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (pygame requirements)
RUN apt-get update && apt-get install -y \
    libsdl1.2-dev \
    libsdl-image1.2-dev \
    libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev \
    libsmpeg-dev \
    python3-dev \
    python3-numpy \
    subversion \
    ffmpeg \
    libswscale-dev \
    libportmidi-dev \
    libavformat-dev \
    libavcodec-dev

# Copy the necessary files into the container
COPY game.py /
COPY graphics /graphics  # If you have a 'graphics' directory containing game assets
COPY fonts /fonts        # If you have a 'fonts' directory containing fonts

# Install pygame
RUN pip install pygame

# Define the entry point command to run your game
CMD ["python", "your_game_script.py"]
