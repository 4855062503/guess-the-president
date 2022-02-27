# Installation
- Install Docker
- Run `sudo docker pull python`
- Clone this repo & cd into it
- Run `sudo docker build -t octo-vision .`

# Running it
- Run `sudo docker run octo-vision`

# How the face recognizer is trained and stored

- The face recognizer is trained using the train script and then the trained classifier is stored as a pickle file to be used with our flask backend for fast read/write
