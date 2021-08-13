FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip; apk add build-base; pip install numpy
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "/HelloWorld.py" ]