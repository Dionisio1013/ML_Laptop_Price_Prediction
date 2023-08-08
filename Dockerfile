# Stage 1: Build the React.js frontend
FROM node:14 as frontend_build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install npm dependencies
RUN npm install

# Copy the rest of the frontend source code
COPY . .

# Build the React.js app for production
RUN npm run build

# Stage 2: Build the Flask backend and serve React.js frontend
FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Copy the React.js build output from the previous stage
COPY --from=frontend_build /app/build /app/build

# Install AWS CLI
RUN apt update -y && apt install awscli -y

# Copy the backend source code
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port where your Flask app will run (should match the port in app.py)
EXPOSE 8080

# Start the Flask app
CMD ["python3", "app.py"]
