## Go To This Website For Uploading Images With Their Class And Training Them
```sh
https://teachablemachine.withgoogle.com/
```

## Building The Docker Image
```sh
docker build -t tensorflow-app .
```

## Running The Docker Image On A Container
```sh
docker run -it --rm -v ${PWD}:/app tensorflow-app
```