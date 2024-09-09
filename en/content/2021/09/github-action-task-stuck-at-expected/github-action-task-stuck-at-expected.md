Status: published
Date: 2021-09-15 01:11:06
Modified: 2022-08-11 09:01:10
Author: Benjamin Du
Slug: github-action-task-stuck-at-expected
Title: GitHub Action Task Stuck At Expected
Category: Computer Science
Tags: Computer Science, programming, GitHub, Actions, task, check, stuck, expected



Github pull request - Waiting for status to be reported

![github-action-wf](https://i.stack.imgur.com/xHqbI.png)

1. The simplest manually solution is to close the PR and reopen it.

2. In my case, 
    the issue was due to `GITHUB_TOKEN` was used for the GitHub Action
    [create-pull-request](https://github.com/peter-evans/create-pull-request)
    .
    Creating a repository secret 
    and use it to authenticate the GitHub Action
    [create-pull-request](https://github.com/peter-evans/create-pull-request)
    resolved the issue.
