# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt file to the working directory
COPY requirements.txt ./

# Install any dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the working directory
COPY . .

# Expose the port that the Django app will run on
EXPOSE 8000

# Run Django migrations and start the development server
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
