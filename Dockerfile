FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt update
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install -y python3-opencv
RUN pip install opencv-contrib-python
COPY . .
CMD ["python", "app.py"]

