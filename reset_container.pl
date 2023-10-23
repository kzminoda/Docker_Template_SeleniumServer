#!/usr/bin/perl
#
use strict;
use warnings;

my $r = `docker-compose down --rmi all --volumes --remove-orphans`;

