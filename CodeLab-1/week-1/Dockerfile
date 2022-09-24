FROM python:latest 
RUN apt-get update
RUN apt-get install wget
RUN wget "https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv"

RUN grep -Eo "([A-Z]+ INC)" fb_sub.csv > newfile.txt

RUN awk 'NR==1' newfile.txt > company.txt