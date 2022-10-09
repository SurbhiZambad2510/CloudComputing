FROM python:3.10.7

USER root

RUN apt-get update && apt-get install wget

RUN pip3 install jupyter

WORKDIR /codeLab2

RUN wget "https://raw.githubusercontent.com/mschermann/forensic_accounting/master/Introduction.ipynb"

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

ENV JUPYTER_USER our_user 

RUN useradd -ms /bin/bash ${JUPYTER_USER}

EXPOSE 8888

USER ${JUPYTER_USER}

USER root

CMD jupyter notebook --ip=0.0.0.0 --port 8888 --allow-root