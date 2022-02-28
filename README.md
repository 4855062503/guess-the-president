# Upload a photo of Trump or Biden and it'll tell you who it is

# Installation
- Install Docker
- Run `sudo docker pull python`
- Clone this repo & cd into it
- Run `sudo docker build -t president .`

# Running it
- Run `sudo docker run president`

# How the face recognizer is trained and stored

- The face recognizer is trained using the train script and then the trained classifier is stored as an XML file to later be imported by the Flask app
