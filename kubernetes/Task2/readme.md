
File Structure:

k8s-mongo-express/
│
├── mongodb/
│   ├── mongodb-deployment.yaml
│   └── mongodb-service.yaml
│
├── mongoexpress/
│   ├── mongoexpress-deployment.yaml
│   └── mongoexpress-service.yaml
│
└── README.md

MongoDB and MongoDB-Express Deployment on Kubernetes
Deploy MongoDB and MongoDB-Express on a Kubernetes cluster, using Secrets for securely managing MongoDB authentication credentials.
Overview
MongoDB will be deployed in a Kubernetes pod and will be secured with authentication.
MongoDB-Express will be deployed in another pod to provide a web-based interface for managing MongoDB.
Both services will communicate securely, with MongoDB exposing its service, and MongoDB-Express connecting to it using environment variables that hold the credentials stored in Kubernetes Secrets.
Steps to Deploy MongoDB and MongoDB-Express with Kubernetes
1. Create MongoDB Secret
First, create a Kubernetes Secret to securely store MongoDB credentials .
The following YAML will create a secret named mongodb-secret:


mongo-root-username and mongo-root-password are the base64-encoded credentials.
Apply the secret to your Kubernetes cluster:
kubectl apply -f mongodb-secret.yaml


2. Create MongoDB Deployment
Next, create the MongoDB deployment. This deployment will use the mongodb-secret to inject the root credentials into the MongoDB container as environment variables:

Apply the MongoDB deployment:

kubectl apply -f mongodb-deployment.yaml
3. Create MongoDB Service
Create a Service to expose MongoDB inside the cluster:


Apply the service:
kubectl apply -f mongodb-service.yaml












4. Create MongoDB-Express Deployment
Create the MongoDB-Express deployment that will connect to the mongodb-service using the same secret for authentication. This deployment will allow you to manage MongoDB through a web-based interface.

Apply the MongoDB-Express deployment:
kubectl apply -f mongo-express-deployment.yaml



5. Create MongoDB-Express Service
To expose MongoDB-Express externally (for web access), create a Service for MongoDB-Express:


Apply the service:
kubectl apply -f mongo-express-service.yaml

6. Verify Deployment
After applying all the configurations, verify that the MongoDB and MongoDB-Express pods are running:
kubectl get pods



7. Access MongoDB-Express
To access MongoDB-Express from your browser, use the NodePort or LoadBalancer IP that Kubernetes exposes for MongoDB-Express. For example:
kubectl get svc


Look for the mongo-express-service and find the external IP or NodePort.
Access MongoDB-Express by navigating to http://198.96.95.203:30000/ 
Output:



