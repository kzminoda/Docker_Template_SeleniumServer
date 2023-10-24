FROM php:latest
RUN apt-get update
RUN apt-get install -y sudo git wget vim
RUN apt-get install -y p7zip p7zip-full zip unzip zlib1g-dev libzip-dev zlib1g-dev
RUN docker-php-ext-install zip

WORKDIR /work
RUN chmod 0777 -R /work
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

CMD ["/bin/bash"] 

