FROM selenium/standalone-chrome-debug:latest

ENV LANGUAGE ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
RUN ls -l /tmp
RUN locale-gen ja_JP.UTF-8
RUN dpkg-reconfigure --frontend noninteractive locales
RUN apt-get update -qqy
RUN apt-get -qqy --no-install-recommends install language-pack-ja
RUN rm -rf /var/lib/apt/lists/* /var/chache/apt/*

