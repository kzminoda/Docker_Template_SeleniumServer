FROM php:latest

RUN apt update
RUN apt install -y p7zip p7zip-full zip unzip zlib1g-dev libzip-dev zlib1g-dev
RUN docker-php-ext-install zip

WORKDIR /app
RUN chmod 0777 -R /app
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php
RUN php -r "unlink('composer-setup.php');"
RUN mv composer.phar /usr/local/bin/composer

ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /composer
ENV PATH $PATH:/composer/vendor/bin

