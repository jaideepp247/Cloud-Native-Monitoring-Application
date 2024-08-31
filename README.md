# Cloud-Native-Monitoring-Application

## Overview

This project is a Cloud-Native Resource Monitoring Application built using Python, Flask, and psutil. It monitors system resources such as CPU and memory usage and displays them in a web interface. The application is containerized using Docker and deployed on AWS EKS (Elastic Kubernetes Service). AWS ECR (Elastic Container Registry) is used to store Docker images, and Kubernetes manages the application deployment.

## Features

- **Flask Web App:** A simple web interface using Python’s Flask framework.
- **Dockerized Application:** The app is containerized using Docker for portability.
- **AWS ECR Integration:** Docker image is pushed to AWS ECR.
- **Kubernetes Orchestration:** The app is deployed on AWS EKS.

## Files

- `templates/`: Contains the HTML template for the Flask application.
- `Dockerfile`: Defines the container configuration for the Flask application.
- `Requirements.txt`: Lists the dependencies required by the Python application.
- `app.py`: The main Flask application code that fetches system resource data and renders it on the web interface.
- `ecr.py`: Python script to create an AWS ECR repository and obtain the repository URI.
- `eks.py`: Python script to create and manage Kubernetes deployments and services on AWS EKS.

## Prerequisites

Before starting the project, ensure the following are installed and configured:

- **AWS Account:** Set up an AWS account and configure programmatic access using the AWS CLI.
- **Docker:** Install Docker for containerization.
- **Kubernetes and kubectl:** Install Kubernetes CLI (`kubectl`) to manage Kubernetes clusters.
- **AWS CLI:** Configure AWS CLI for programmatic access.
- **Python:** Make sure Python is installed on your system.

## Project Setup

### Part 1: Running the Flask Application Locally

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```
2. Install the dependencies:
    ```bash
    pip install -r Requirements.txt
    ```
3. Run the application:
    ```bash
    python app.py
    ```
   The app will start on `http://localhost:5000`, where you can view the resource monitoring dashboard.

### Part 2: Dockerizing the Application

1. Build the Docker image using the Dockerfile:
    ```bash
    docker build -t resource_monitoring_app .
    ```
2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 resource_monitoring_app
    ```
   Access the application at `http://localhost:5000` in your browser.

### Part 3: Pushing the Docker Image to AWS ECR

1. Run the ECR creation script to create a new repository and get the repository URI:
    ```bash
    python ecr.py
    ```
2. Tag and push the Docker image to ECR:
    ```bash
    docker tag resource_monitoring_app:latest <repository_uri>:latest
    docker push <repository_uri>:latest
    ```

### Part 4: Deploying the App on AWS EKS

1. Create an EKS cluster and node group using the AWS console or CLI.
2. Run the Kubernetes deployment script:
    ```bash
    python eks.py
    ```
   This will create a deployment and service in your EKS cluster.
3. Check the status of the deployment:
    ```bash
    kubectl get deployment -n default (check deployments)
    kubectl get service -n default (check service)
    kubectl get pods -n default (to check the pods)
    ```
4. Port-forward the service to access the application:
    ```bash
    kubectl port-forward service/my-service 5000:5000
    ```

## Dependencies

Ensure the following Python libraries listed in `Requirements.txt` are installed:


You can install them using:
```bash
pip install -r Requirements.txt
