# Use Python 3.11 official image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app/tubers

# Copy requirements.txt first to leverage Docker caching for dependency installation
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .


# Copy entrypoint script and set execution permissions
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


# Expose port 8000 for the Django development server
EXPOSE 8000


ENTRYPOINT ["/entrypoint.sh"]

# Default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
