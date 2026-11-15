---
title: Hands on the Python Library notifiers
created: '2020-08-03T15:46:20-07:00'
date: '2026-11-15T09:24:37-08:00'
authors:
  - bendu
label: hands-on-the-python-library-notifiers
license: CC-BY-4.0
tags:
  - computer science
  - Python
  - notifiers
  - notification
  - email
  - web
  - internet
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Email

The function below is an example of sending email using the Python library notifiers.

```python
import notifiers
notifiers.get_notifier("email").notify(
    from_="sender@domain.com",
    to=["recipient1@domain.com", "recipient2@domain.com"],
    subject="Example of Sending Email Using notifiers",
    message="This is a testing email.",
    host="smtp.domain.com",
    username="user_name_if_needed",
    password="password_if_needed",
    attachements=["/path/to/file1", "/path/to/file2"]
)
```

Notice that notifiers supports email attachments via the `attachments` option
which accepts a **non-empty list of valid file paths**.
