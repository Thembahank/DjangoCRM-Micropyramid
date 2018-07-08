Django-CRM
==========

Forked from https://github.com/MicroPyramid/Django-CRM

Django 1.11 , Python 3.6 & Bootstrap

Django CRM is opensource CRM developed on django framework.


.. image:: https://travis-ci.org/MicroPyramid/Django-CRM.svg?branch=master
   :target: https://travis-ci.org/MicroPyramid/Django-CRM

.. image:: https://coveralls.io/repos/github/MicroPyramid/Django-CRM/badge.svg?branch=master
   :target: https://coveralls.io/github/MicroPyramid/Django-CRM?branch=master

.. image:: https://landscape.io/github/MicroPyramid/Django-CRM/master/landscape.svg?style=flat
   :target: https://landscape.io/github/MicroPyramid/Django-CRM/master
   :alt: Code Health

.. image:: https://img.shields.io/github/license/MicroPyramid/Django-CRM.svg
    :target: https://pypi.python.org/pypi/Django-CRM/

.. image:: https://www.codetriage.com/micropyramid/django-crm/badges/users.svg
    :target: https://www.codetriage.com/micropyramid/django-crm

http://django-crm.readthedocs.io for latest documentation


This project contains the following modules.

   * Contacts
   * Accounts
   * Cases
   * Leads
   * Opportunity
   * Planner


Installation - Requirements
===========================

Ubuntu 64bit - 16.04
--------------------
$ sudo apt-get update && apt-get upgrade -y

$ sudo apt-get install -y curl wget libpq-dev python3-dev gem ruby ruby-dev build-essential libssl-dev libffi-dev python-dev python-virtualenv python-pip git redis-server libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev tcl8.6-dev tk8.6-dev python-tk

$ sudo gem install sass

## Install postgres and create correct user that matches your database settings
$ sudo apt-get install postgresql postgresql-contrib
$ sudo -u postgres createuser -P -e username

## Use pipenv to install python modules::
pipenv install



Demo credentials for Django CRM:

  * **Email:** admin@micropyramid.com
  * **Password:** admin



