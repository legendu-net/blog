UUID: a64534c3-c495-436a-a1f6-d21dd3fc135f
Status: published
Date: 2019-03-28 18:42:55
Author: Ben Chuanlong Du
Slug: apache-airflow-tips
Title: Apache Airflow Tips
Category: Programming
Tags: programming, Apache AirFlow, workflow, scheduler, scheduling

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Links

https://airflow.apache.org/start.html

https://airflow.apache.org/cli.html

## Installation (MySQL)

1. Install Apache AirFlow.

        wajig install \
            python3-dev python3-pip \
            mysql-server libmysqlclient-dev
        sudo AIRFLOW_GPL_UNIDECODE=yes pip3 install apache-airflow[mysql]

2. Add the following content into your `my.cnf` (e.g., `/etc/mysql/my.cnf`) file. 

        [mysqld]
        explicit_defaults_for_timestamp=1

Below is an example of `my.cnf`.

        #
        # The MySQL database server configuration file.
        #
        # You can copy this to one of:
        # - "/etc/mysql/my.cnf" to set global options,
        # - "~/.my.cnf" to set user-specific options.
        #
        # One can use all long options that the program supports.
        # Run program with --help to get a list of available options and with
        # --print-defaults to see which it would actually understand and use.
        #
        # For explanations see
        # http://dev.mysql.com/doc/mysql/en/server-system-variables.html

        #
        # * IMPORTANT: Additional settings that can override those from this file!
        # The files must end with '.cnf', otherwise they'll be ignored.
        #

        !includedir /etc/mysql/conf.d/
        !includedir /etc/mysql/mysql.conf.d/

        [mysqld]
        explicit_defaults_for_timestamp=1

3. Initial database.

        airflow initdb

4. Start the web server.

        airflow webserver -D -p 8080

5. Start a scheduler.

        airflow scheduler -D

## References

https://airflow.apache.org/start.html

https://airflow.apache.org/installation.html

https://airflow.apache.org/tutorial.html
