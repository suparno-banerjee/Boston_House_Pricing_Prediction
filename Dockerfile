FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r required_libraries.txt
EXPOSE $PORT
CMD python flasg.py