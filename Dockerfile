FROM frolvlad/alpine-python3
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

