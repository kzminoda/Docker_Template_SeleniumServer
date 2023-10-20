FROM selenium/standalone-chrome-debug:latest

ENV LANGUAGE ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
RUN locale-gen ja_JP.UTF-8
RUN dpkg-reconfigure --frontend noninteractive locales
RUN apt update -qqy
RUN apt -qqy --no-install-recommends install language-pack-ja
RUN rm -rf /var/lib/apt/lists/* /var/chache/apt/*

