# Upload a photo of Trump or Biden and it'll tell you who it is

# Installation
- Install Docker
- Run `sudo docker pull python`
- Run `sudo docker pull nginx`
- Clone this repo & cd into it
- Run `sudo ./run-docker.sh` to build the docker containers
- Run `sudo docker-compose up` to run the docker containers


# Running it
- Run `sudo docker run president`

# How the face recognizer is trained and stored

- The face recognizer is trained using the train script and then the trained classifier is stored as an XML file to later be imported by the Flask app
