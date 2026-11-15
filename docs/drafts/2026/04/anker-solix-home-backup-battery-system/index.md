---
title: Anker Solix Home Backup Battery System
created: '2026-04-03T21:39:15.050101-07:00'
date: '2026-11-15T09:29:04-08:00'
authors:
  - bendu
label: anker-solix-home-backup-battery-system
license: CC-BY-4.0
tags:
  - life
  - house
  - battery
  - backup
  - Anker Solix
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips and Tricks

1. The Anker Home Backup Battery System automatically decides when to charge based the time-of-use schedule.

1. A F3800 plus battery has to be disconnected from the Anker Home Power Panel
   before doing firmware update.

1. Use only one F3800 plus battery for system self-test.
   Once the system self-test is done,
   just connect the other F3800 plus battery (if you have 2 F3800 batteries).

1. Switch off breakers on the Anker Home Panel before plugging/unplugging batteris.

1. F3800 plus batteries can be added as devices in the Anker app
   but BP3800 extension batteries cannot be directly added as devices.
   A BP3800 extension battery shows up under the F3800 battery that it connects to in the app.

1. If battery capacity is an issue,
   you can

   - Add BP3800 expansion batteries.
   - Leverage manual override to charge batteries.
     Notice that manual override is one-time only.
   - Configure 10am - 5pm (off peak) as super off-peak in the app
     to fool the system to charge between the 2 peak periods.
   - Use an EV to charge batteries if necessary during a power outage.
     Notice that the batteries cannot supply power to the house
     while they are being charged.

1. The Anker app supports at most 6 time frames for time-of-use.
   If you this becomes a limit to you,
   you can remove the last super off-peak time frame (11pm - 12pm).
   This gives you the flexibility to hack other time frames.
   For example,
   you can split an off-peak time frame into an off-peak time frame and a super off-peak time frame
   to fool the system to do more charging.
   Even if you do need such a hacking,
   this can still provides a couple of benefits.

   - Easier to set up time-of-use in the app.
   - Cleaner as there's one fewer time frame in the app.

## Customer Service

- Phone: 800-988-5541 (9AM-5PM(PT) Monday to Friday)
- Email: support@anker.com

## PSE Time-Of-Use

https://www.pse.com/account-and-billing/time-of-use/tou-enroll-manage

<img width="817" height="1358" alt="Image" src="https://github.com/user-attachments/assets/7f3bb87d-0467-47e3-88c0-389677a91c87" />

## User Guide

https://support.ankersolix.com/s/article/Anker-SOLIX-BP3800-Expansion-Battery-USER-GUIDE

https://support.ankersolix.com/s/article/Anker-SOLIX-F3800-Portable-Power-Station-USER-GUIDE--A1790

https://support.ankersolix.com/s/article/Anker-SOLIX-F3800-Portable-Power-Station-USER-GUIDE--A1790#_idTextAnchor018

https://www.ankersolix.com/blogs/smart-home/f3800-hpp-owner-manual

https://support.ankersolix.com/s/article/Anker-SOLIX-Home-Power-Panel-User-Guide-A17B1

## References

- [Configured my Anker Solix F3800s for Time and Use Billing](https://www.youtube.com/watch?v=kZsdBRJR4Sg)
