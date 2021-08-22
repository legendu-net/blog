Status: published
Date: 2020-08-03 15:46:20
Author: Benjamin Du
Slug: handons-the-python-library-notifiers
Title: Hands on the Python Library notifiers
Category: Computer Science
Tags: Computer Science, python, notifiers, notification, email, web, internet
Modified: 2020-11-03 15:46:20

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Email

The function below is an example of sending email using the Python library notifiers.

    :::python
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

Notice that notifiers supports email attachements via the `attachments` option
which accepts a **non-empty list of valid file paths**.