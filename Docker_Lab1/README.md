# Docker - Lab 1
## Creating a Simple Python Backend App with Docker:
Create a simple Python backend app using Flask, containerize it with Docker, and then run the app in a custom bridge network. 

Test it by accessing the application in a browser.

---
### Step 1: Create a Simple Python Backend App and HTML

- **Create backend directory structure:**

![image](https://github.com/user-attachments/assets/faefc2cd-f250-459b-9c06-d8143969b7fa)

- **Create the Python App (app.py) and HTML files:**

Create a file named app.py inside the backend directory. 
This file will contain the code for a simple Flask application that serves different endpoints, performs a simple computation, and renders an HTML template.

The templates directory will contain three HTML files that correspond to the different pages.

GO TO: Docker_Lab1/backend/  & Docker_Lab1/backend/templates

### Step 2: Create the Dockerfile
Inside the same directory (python-backend/)
- **Write the Dockerfile**

GO TO: Docker_Lab1/backend/Dockerfile

- **Build the Docker Image from Dockerfile**

```
docker build -t python-backend .
docker images
```

![image](https://github.com/user-attachments/assets/0b1c6eab-8b96-4195-86f6-76925e342e0a)


Output is a custom image created with name python-backend:
![image](https://github.com/user-attachments/assets/6e34e8a6-a63f-4f14-9d55-2c4724487cc2)


- **Step 3: Create a Custom Bridge Network**
```
docker network create --driver bridge bridge-network-2
docker network ls
```

**Output:**

![image](https://github.com/user-attachments/assets/65f4f883-cbac-4ddb-a0aa-6357cfa98afb)

![image](https://github.com/user-attachments/assets/c9783619-58f7-404c-971d-09de5d4e0751)

- **Step 4: Create the Docker Container**
Run the container from the image(python-backend)  built and connect it to the custom bridge network created. 

```
docker run -d --name pythonbackend-container --network bridge-network-2 -p 5055:5055 python-backend
```

**Output:**

![image](https://github.com/user-attachments/assets/b0d2bcd7-f8d0-4c81-96fc-65d835fb1811)


**Test the app**

- Check local IP:
```
ip a
```
![image](https://github.com/user-attachments/assets/e17be0bc-6e19-4292-9a9a-c8a43d810949)

**Output:**

- **Home page:**

![image](https://github.com/user-attachments/assets/699f3905-9f93-4b49-850a-5e40ed002a3a)

- **multiply page:**

![image](https://github.com/user-attachments/assets/124e27c7-e4fe-4b8c-8bbb-55098b55941a)

- **multiply page result:**

![image](https://github.com/user-attachments/assets/17abdd75-aae0-437c-959d-81a3bb9cd9aa)

- **About page:**

![image](https://github.com/user-attachments/assets/cfb77846-b941-45fe-bb6f-7c408786bf2e)

