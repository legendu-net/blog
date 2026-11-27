---
title: Age Is a Modern Alternative to GnuPG
created: '2026-04-13T21:13:36.601982-07:00'
date: '2026-11-26T23:00:29-08:00'
authors:
  - bendu
label: age-is-a-modern-alternative-to-gnupg
license: CC-BY-4.0
tags:
  - age
  - GnuPG
  - GPG
  - encryption
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation

### Ubuntu / Debian

```
sudo apt install age
```

### Homebrew / linuxbrew

```
brew install age
```

## Usage

Encrypt an file to age format using a passphrase.

```
age -p -o file.age file 
```

Decrypt an age file using passphrase.

```
age -d -o file file.age
```
