FROM frolvlad/alpine-python3
RUN apk add -U build-base linux-headers pcre python3-dev
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

