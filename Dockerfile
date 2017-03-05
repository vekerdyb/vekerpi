FROM vekerdyb/rpi-python3
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

