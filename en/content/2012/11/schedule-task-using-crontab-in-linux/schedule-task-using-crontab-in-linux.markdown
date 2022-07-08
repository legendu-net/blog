Status: published
Date: 2012-11-27 11:28:08
Slug: schedule-task-using-crontab-in-linux
Author: Ben Chuanlong Du
Title: Schedule Task Using Cron in Linux
Category: OS
Tags: task, crontab, schedule, linux, scheduling, AirFlow
Modified: 2022-07-07 22:08:14


Note: Cron is great for simple scheduling requests. 
For complicated scheduling with many dependencies 
you probably want to go with 
[AirFlow](http://www.legendu.net/misc/blog/apache-airflow-tips)
.

## Installation

Cron is usually installed by default.
It not (e.g., if you are using a Docker image),
you can install it using the following command (on Ubuntu).

    :::bash
    wajig update && wajig install cron

## Alternative to Cron

1. AirFow is a more rigorous job scheduling system. 

2. When cron is not available,
    a simple alternative is to 
    write a simple Python script to run a task at certain times.

## Tips and Traps

1. There are 6 fields that you need to fill for a task to be schedule: 
    `m`, `h`, `dom`, `mon`, `dow` and `command`,
    which stand for the minute, the hour, the day of month, the month, the day of week 
    (of the scheduled time), 
    and the command to run, respectively.
    The graph below shows possible values for each field.

        ┌────────── minute (0 - 59)
        │ ┌──────── hour (0 - 23)
        │ │ ┌────── day of month (1 - 31)
        │ │ │ ┌──── month (1 - 12)
        │ │ │ │ ┌── day of week (0 - 6 => Sunday - Saturday, or
        │ │ │ │ │                1 - 7 => Monday - Sunday)
        ↓ ↓ ↓ ↓ ↓
        * * * * * command to be executed

    Notice that abbreviations of days (MON, TUE, etc.) can be used for the field `dow`.
    For example `SUN,MON,THU` for (day of week) 
    will exectute the command on Sundays, Mondays on Thursdays.
    [Crontab Guru](https://crontab.guru/)
    is a quick and simple editor for cron schedule expressions.

2. The information of scheuled tasks are saved in the file `/etc/crontab`. 
    It contains scheduled tasks of all users.
    Though you can schedule tasks by editing the file directly,
    you'd better not.
    It is suggested that you use the command `crontab -e` to schedule tasks.
    If you just want to add crontab tasks,
    an alternative way is to save the information of tasks in a file (e.g. `task.txt`),
    and then run the command `crontab task.txt` to import it.
    To list all scheduled tasks, 
    run the command `crontab -l`.
    To remove a sheduled task,
    use the command `crontab -r`.

3. As long as you use the `crontab` commands to edit the file `/etc/crontab`,
    you do NOT have to restart `cron`.
    `cron` will automatically reload tasks that were changed.
    The log of cron jobs can be found at 
    `/var/log/syslog` (Ubuntu) or `/var/log/cron` (CentOS).
    If you do not have read permission to cron log files, 
    you'd better redict the output and error messages of a cron job 
    to a log file which you have read access.

4. If your cron job consists of multiple shell commands,
    it is best to put those commands into a shell script 
    and call the shell script when you schedule your cron job. 
    This has multiple benefits. 

    - Avoid careless mistakes caused by concatenating multiples commands using `&&`, `||` or `;`. 
    - Have better control and logging of each command.
    - Easier to update the job (if you do not have to update the schedule) 
        as you can update the shell script without touching `crontab`.

4. You can schedule a frequently run task using crontab 
    and then reduce the running frequency of the application in your scripts.
    Below is such an example in Bash shell.

        if [[ $(date +%H) =~ ^(10|12|14|16|18)$ ]]; then
            ...
        fi

    This trick is useful to avoid editing crontab tasks frequently
    as you can control (or more precisely, reduce) the frequency of the task 
    in your script directly.

## Cron Job Examples 

1. Run the command `duplicity.lbp` at 03:00 every Thursday. 

        0   3   *     *     5     duplicity.lbp 

2. Run the command `rsnapshot daily` daily at 22:00. 

        0   22  *     *     *     rsnapshot daily

3. Run the command `rsnapshot daily` hourly at the 5th minutes,
    and redict standard output and error messages to `/home/dclong/cron.log`.

        5   *   *     *     *     /home/dclong/schedule.sh >> /home/dclong/cron.log 2> &1

3. Run a command at 22:00 on the 1st day of every month. 

        0   22  1     *     *     command_to_run

4. There is no intrinsic way to run commands weekly using cron. 
    One way to approximate that is to run a command multiple times per month.
    For example, 
    the setup below runs a command at 22:00 on the 1st and 15th day of every month
    (biweekly approximately)
    .

        0   22  1,15     *     *     command_to_run

## Start a Crontab Service on Ubuntu

```
# start cron service
sudo service cron start
# check status of the cron service 
service cron status
# stop the cron service
service cron stop
```

## Check Crontab Logs

You can use the following command to check crontab logs on Ubuntu.
```
sudo cat /var/log/syslog | grep cron
```

## References

- [crontab guru](https://crontab.guru/)

- [How to Run a cron Job Every Two Weeks / Months / Days](https://www.systutorials.com/how-to-run-a-cron-job-every-two-weeks-months-days/)

- https://stackoverflow.com/questions/18919151/crontab-day-of-the-week-syntax

- https://askubuntu.com/questions/56683/where-is-the-cron-crontab-log

