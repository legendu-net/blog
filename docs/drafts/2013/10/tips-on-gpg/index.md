---
title: Tips on GPG
created: '2013-10-12T09:13:02-07:00'
date: '2026-11-15T12:20:33-08:00'
authors:
  - bendu
label: tips-on-gpg
license: CC-BY-4.0
tags:
  - tips
  - GPG
  - GnuPG
  - encryption
  - decryption
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Symmetric encryption (using passphrase).

   ```
    :::bash
    gpg -c file
   ```

1. Decrypt a symmetric encrypted file.
   You will be prompt to enter your passphrase.

   ```
    :::bash
    gpg file.gpg
   ```

1. You can use the following command to encrypt a file as ascii armor.

   ```
    :::bash
    gpg -a -c file
   ```

1. You can specified the password using the `--passphrase` option
   to avoid keyboard interaction.
   You have to quote (in double/single quotation marks) the password
   if it contains white spaces.
   And you when you quote the password in double/single quotation marks,
   the double/single quotation marks can be escaped as usual by `\"`/`\'`.
