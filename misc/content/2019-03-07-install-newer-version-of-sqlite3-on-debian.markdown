Status: published
Date: 2019-03-07 03:17:18
Author: Benjamin Du
Slug: install-newer-version-of-sqlite3-on-debian
Title: Install Newer Version of Sqlite3 on Debian
Category: Linux
Tags: Linux, SQLite3, Debian, backports

**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

# via: http://www.fangiotophia.com/journal/2010/8/31/random-act-of-stupidity-6-debian-rails-3-setup-guide.html

# Open /etc/apt/sources.list and add the following line to the end, then save the file:
deb http://www.backports.org/debian lenny-backports main contrib non-free

# Then, run the following command to make sure the GPG signatures are correct and don't give you warnings when running apt commands:
sudo aptitude update
sudo aptitude install debian-backports-keyring

# Finally, you can install SQLite3:
sudo aptitude update
sudo aptitude -t lenny-backports install sqlite3 libsqlite3-dev
gem install sqlite3-ruby
