FROM	debian:wheezy

RUN     apt-get update
RUN     apt-get install -y python2.7 python-dev python-pip  openjdk-7-jre

ADD     javagames /opt/javagames
RUN     pip install -r /opt/javagames/requirements.txt

ENV GAMES_PORT 80
EXPOSE $GAMES_PORT

ENV GAMES_PATH /games
VOLUME $GAMES_PATH

WORKDIR /opt/javagames
CMD python javagames.py