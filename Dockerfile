
FROM python:3.11.0-slim

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application to the container
COPY . .

# Expose the port
EXPOSE 8080

# Run application
CMD ["uvicorn", "my_app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]