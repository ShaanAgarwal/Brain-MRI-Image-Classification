## Go To This Website For Uploading Images With Their Class And Training Them
```sh
https://teachablemachine.withgoogle.com/
```

## Building The Docker Image
```sh
docker build -t tensorflow-app .
```

## Running The Docker Image In A Container
```sh
docker run -it --rm -v ${PWD}:/app tensorflow-app
```

### Dockerfile is now inside Dockerfile.example
### The Above is used for Testing Purpose Of app.py

## For Using The Machine Learning Model With Streamlit Application

## Building The Docker Image
```sh
docker build -t tensorflow-app .
```

## Running The Docker Image In A Container
```sh
docker run -it --rm -p 8501:8501 -v ${PWD}:/app tensorflow-app