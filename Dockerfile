FROM python:3.8

# Set the working directory
WORKDIR /fyle_app

# Copy the requirements first to leverage Docker cache
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port your app runs on
EXPOSE 4040

# Set environment variables for Flask
ENV FLASK_ENV=development
ENV FLASK_APP=core/server.py

# Run the run.sh script
CMD ["bash", "run.sh"]
