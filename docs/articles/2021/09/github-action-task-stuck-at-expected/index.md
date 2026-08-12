---
title: GitHub Action Task Stuck at Expected
created: '2021-09-15T01:11:06-07:00'
date: '2026-08-11T22:19:13-07:00'
authors:
  - bendu
label: github-action-task-stuck-at-expected
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - GitHub
  - Actions
  - task
  - check
  - stuck
  - expected
---

Github pull request - Waiting for status to be reported

<img width="812" height="426" alt="Image" src="https://github.com/user-attachments/assets/671e80e7-94b0-4738-a1a1-83c36b9a3abf" />

1. The simplest manually solution is to close the PR and reopen it.

1. In my case,
   the issue was due to `GITHUB_TOKEN` was used for the GitHub Action
   [create-pull-request](https://github.com/peter-evans/create-pull-request)
   .
   Creating a repository secret
   and use it to authenticate the GitHub Action
   [create-pull-request](https://github.com/peter-evans/create-pull-request)
   resolved the issue.
