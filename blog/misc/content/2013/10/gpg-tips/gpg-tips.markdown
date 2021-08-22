Status: published
Author: Ben Chuanlong Du
Date: 2013-10-12 09:13:02
Title: Tips on GPG
Slug: gpg-tips
Category: Software
Tags: tips, GPG, GnuPG, encryption, decryption
Modified: 2021-04-12 09:13:02

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**
 
1. Symmetric encryption (using passphrase).

        :::bash
        gpg -c file

2. Decrypt a symmetric encrypted file.
    You will be prompt to enter your passphrase.

        :::bash
        gpg file.gpg

1. You can use the following command to encrypt a file as ascii armor.

        :::bash
        gpg -a -c file

2. You can specified the password using the `--passphrase` option
    to avoid keyboard interaction. 
    You have to quote (in double/single quotation marks) the password 
    if it contains white spaces.
    And you when you quote the password in double/single quotation marks,
    the double/single quotation marks can be escaped as usual by `\"`/`\'`.

