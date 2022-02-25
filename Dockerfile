FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["sudo","apt-get","install","python3-opencv"]
CMD ["python", "app.py"]
