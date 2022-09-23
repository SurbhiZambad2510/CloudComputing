FROM python:latest 
RUN apt-get update
RUN apt-get install wget
RUN wget "https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv"

WORKDIR /src/ 
COPY . /src/

ENTRYPOINT ["python","test.py"]
EXPOSE 8888


