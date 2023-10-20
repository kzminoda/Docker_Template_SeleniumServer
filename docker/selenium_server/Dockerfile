FROM php:latest

WORKDIR /app
RUN chmod 0777 -R /app
#RUN php -r "copy('https://getcomposer.org/installer', './composer-setup.php');"
RUN ls -l
RUN wget https://getcomposer.org/installer
#RUN php ./composer-setup.php
RUN php ./installer
#RUN php -r "unlink('./composer-setup.php');"
RUN rm -f ./installer
RUN mv composer.phar /usr/local/bin/composer

ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /composer
ENV PATH $PATH:/composer/vendor/bin

