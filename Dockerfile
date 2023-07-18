# Base Image
FROM python:3.10-slim-bullseye

# Installing necessary packages
RUN pip install fpdf2
RUN pip install oloren==0.0.48

# Copying application code to the Docker image
COPY app.py /app.py

# Default command for the container
CMD ["python", "app.py"]