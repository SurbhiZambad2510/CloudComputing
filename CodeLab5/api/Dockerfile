
FROM python



RUN pip3 install flask
RUN pip3 install requests

RUN pip install psycopg2-binary --user
RUN pip3 install psycopg2


VOLUME app

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["api.py"]