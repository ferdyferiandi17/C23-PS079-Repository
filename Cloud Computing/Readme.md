# Cloud Computing Deploy 

- To build a Docker container locally, you can run the following command: docker build -t gcr.io/capstone-389113/flask-app-deploy .

- To test the container locally on localhost port 8080: docker run -p 8080:8080 gcr.io/capstone-389113/flask-app-deploy. This will ensure that the application runs correctly on localhost.

- To deploy the Docker container to Google Cloud Container Registry: docker push gcr.io/capstone-389113/flask-app-deploy.

 - to submit the build to Container Registry: gcloud builds submit --tag gcr.io/capstone-389113/flask-app-deploy.
 - Test API with Link provided by cloud run
 <br><br>
![Contoh Gambar](https://drive.google.com/uc?id=149eKbO-jBO_dh0lrpOOU7w7KWa1IoBBP)
