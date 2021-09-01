FROM python:alpine3.7
COPY . /app
WORKDIR /app
# RUN pip3 install --upgrade pip; apk add build-base; pip3 install numpy
RUN pip3 install -r requirements.txt
EXPOSE 80
ENTRYPOINT [ "python" ]
CMD [ "/HelloWorld.py" ]
