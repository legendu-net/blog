Status: published
Date: 2018-10-10 09:32:40
Author: Ben Chuanlong Du
Title: Job Scheduling and Management Using Apache Airflow
Slug: apache-airflow-tips
Category: Computer Science
Tags: programming, Apache AirFlow, workflow, scheduler, scheduling
Modified: 2021-06-10 09:32:40

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

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

## Tips and Traps

1. Just place your Python script which defines a DAG into the directory `AIRFLOW_HOME/dags/`
    and AirFlow will pick it up automatically.

2. Avoid defining tasks using the BashOperator.
    Some bash commands (e.g., `rsync`) might return the error code 0 
    even if it essentially succeeds.
    It is quite challenge to handle exceptions/error code of shell command
    to ingore non-critical errors.

## Delete DAGs

https://gist.github.com/villasv/8bb1492beb46162c28dbc242d4887533

## References

https://airflow.apache.org/start.html

https://airflow.apache.org/installation.html

https://airflow.apache.org/tutorial.html

https://airflow.apache.org/cli.html

[Airflow Lesser Known Tips Tricks and Best Practises](https://medium.com/datareply/airflow-lesser-known-tips-tricks-and-best-practises-cf4d4a90f8f)

[We Are All Using AirFlow Wrong and How to Fix It](https://medium.com/bluecore-engineering/were-all-using-airflow-wrong-and-how-to-fix-it-a56f14cb0753)

[AirFlow Why Is Nothing Working](https://medium.com/bluecore-engineering/airflow-why-is-nothing-working-f705eb6b7b04)

[Yet Another Scalable Apache AirFlow with Docker Example Setup](https://medium.com/@tomaszdudek/yet-another-scalable-apache-airflow-with-docker-example-setup-84775af5c451)

https://kubernetes.io/blog/2018/06/28/airflow-on-kubernetes-part-1-a-different-kind-of-operator/

https://towardsdatascience.com/kubernetesexecutor-for-airflow-e2155e0f909c

https://bostata.com/built-to-scale-running-highly-concurrent-etl-with-apache-airflow/
