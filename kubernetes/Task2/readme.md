To complete Task 2 using Kubernetes (K8s) with MongoDB and MongoDB-Express in separate pods, and without custom Docker images, follow these steps. The MongoDB instance will be secured with authentication, and MongoDB-Express will communicate with MongoDB.

Overview
MongoDB will be deployed in one pod.
MongoDB-Express will be deployed in another pod.
MongoDB authentication will be enabled (e.g., using a root user and password).
Kubernetes resources will be defined with deployment, services, and possibly an ingress (for external access to MongoDB-Express).

Steps to complete the task
1. Create Kubernetes YAML Files
We'll define the necessary Kubernetes manifests (YAML files) for both MongoDB and MongoDB-Express.

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


![image](https://github.com/user-attachments/assets/1a544489-5150-4b34-b457-bdcd5fef72e8)



![image](https://github.com/user-attachments/assets/f9e70cbe-dbba-4646-a029-c7c792728018)



