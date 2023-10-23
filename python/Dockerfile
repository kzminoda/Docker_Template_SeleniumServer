FROM python:latest
RUN apt-get update
RUN apt-get install -y sudo git wget vim
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip install --upgrade pip
RUN pip install selenium pandas openpyxl 
WORKDIR /work
CMD ["/bin/bash"] 

