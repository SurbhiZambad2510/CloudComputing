FROM python


RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install psycopg2-binary


VOLUME app


WORKDIR /app

EXPOSE 81

ENTRYPOINT ["python"]
CMD ["consumer.py"]