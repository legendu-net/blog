UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2017-11-07 23:28:01
Slug: schedule-task-using-crontab-in-linux
Author: Ben Chuanlong Du
Title: Schedule Task Using Crontab in Linux
Category: Linux
Tags: task, crontab, schedule, linux, scheduling

The information of scheuled tasks are saved in the file `/etc/crontab`. 
It contains scheduled tasks of all users.
Though you can schedule tasks by editing the file directly,
you'd better not.
It is suggested that you use the command `crontab -e` to schedule tasks.
There are 6 fields that you need to fill for a task to be schedule: 
`m`, `h`, `dom`, `mon`, `dow` and `command`,
which stand for `minute`, `hour`, `day of month`, `month`, `day of week` (0 stands for Sunday) 
and `command` respectively. 
An alternative way is to save the information of a scheduled task in a file (e.g. 'task.txt'),
and then run the command `crontab task.txt` to import it.
To list all scheduled tasks, 
run the command `crontab -l`.
To remove a sheduled task,
use the command `crontab -r`.

As long as you use the `crontab` commands to edit the file `/etc/crontab`,
you do NOT have to restart `cron`.
`cron` will automatically reload tasks that were changed.


## Example 

1. Run the command `duplicity.lbp` at 03:00 every Thursday. 

        0   3   *     *     5     duplicity.lbp 

2. Run the command `rsnapshot daily` at 22:00 everyday. 

        0   22  *     *     *     rsnapshot daily

