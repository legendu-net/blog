Status: published
Date: 2022-05-04 11:21:24
Modified: 2022-05-04 11:21:24
Author: Benjamin Du
Slug: wirelss-for-debian
Title: Wirelss for Debian
Category: Computer Science
Tags: Computer Science, programming, OS, Linux, Debian, wireless

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Depending on the wireless card on your machine,
    you might have to install a wireless card dirver manually. 
    You can use the following command 
    to check the type of the wireless card on your machine.

        :::bash
        lspci | grep -i wireless

    Then you can search for the driver/package that support your wireless card. 
    For example, the result of the above command on my laptop is:

        06:00.0 Network controller: Intel Corporation PRO/Wireless 5100 AGN [Shiloh] Network Connection

    This wireless card is supported by iwlwifi. 
    If you have included non-free softwares in your debian repository 
    (see the first step after installation),
    you can type `wajig install firmware-iwlwifi` in terminal to install it. 

2. If you have installed a desktop environment, 
    you can use a network manager to manager the wireless interface. 
    In this case, 
    it is strongly suggested that 
    you comment everything out in the 
    configuration file `/etc/network/interface`
    Otherwise, 
    you might not be able to use the wireless network 
    even though the network manager says that you have connected to it. 
