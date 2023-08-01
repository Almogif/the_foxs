# Use the official Python image as the base
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files into the container
COPY game.py /app/
COPY graphics /app/graphics
COPY fonts /app/fonts


# Install the specified version of pygame
RUN pip install pygame==1.9.6

# Define the entry point command to run your game
CMD ["python", "game.py"]
