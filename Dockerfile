FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install opencv-python
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./script.py" ]
#CMD ["tail", "-f", "/dev/null"]
