UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Read CPU Temperature in Linux
Date: 2012-05-19 00:00:00
Tags: modprobe, sensors, CPU, Linux, temperature
Category: Linux
Slug: linux-read-cpu-temperature
Author: Ben Chuanlong Du

<img src="http://dclong.github.io/media/computer/hot.jpg" height="200" width="240" align="right"/>

First you have to install package "lm-sensors". 

    wajig install lm-sensors

To detect the cpu temperature, type the following command.

    modprobe coretemp
    sensors

For more instructions on this top, 
see [nixCraft](http://www.cyberciti.biz/faq/howto-linux-get-sensors-information/).
