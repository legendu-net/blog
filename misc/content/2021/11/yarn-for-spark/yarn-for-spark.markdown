Status: published
Date: 2021-11-29 12:32:33
Modified: 2021-12-05 11:19:49
Author: Benjamin Du
Slug: yarn-for-spark
Title: Yarn for Spark
Category: Computer Science
Tags: Computer Science, programming, Spark, big data, yarn

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


1. List all Spark applications.

        :::bash
        yarn application --list

2. Show status of a Spark application.

        :::bash
        yarn application -status application_1459542433815_0002

3. view logs of a Spark application.

        :::bash
        yarn logs -applicationId application_1459542433815_0002

4. kill a Spark application.

        :::bash
        yarn application -kill application_1459542433815_0002