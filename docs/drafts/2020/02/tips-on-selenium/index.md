---
title: Tips on Selenium
created: '2020-02-21T12:25:39-08:00'
date: '2026-11-15T12:20:36-08:00'
authors:
  - bendu
label: tips-on-selenium
license: CC-BY-4.0
tags:
  - programming
  - Selenium
  - web automation
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips and Traps

1. Selenium IDE is very useful.
   You can use it to record (test) actions
   and then export it into (testing) code in different programming languages (e.g., Python).

   ![selenium-ide-menu](https://user-images.githubusercontent.com/824507/108128434-92163680-7061-11eb-8870-7721c70eaf53.png)

   ![selenium-ide-menu-export](https://user-images.githubusercontent.com/824507/108128195-3cda2500-7061-11eb-974c-6bc5828dfae3.png)

## Examples

```
:::java
DesiredCapabilities cap = DesiredCapabilities.chrome();
cap.setCapability("download.default_directory","C:");
cap.setCapability("download.prompt_for_download","false");
cap.setCapability("directory_upgrade","true");
cap.setCapability("plugins.plugins_disabled","Chrome PDF Viewer");

WebDriver driver = new ChromeDriver(cap);
```

Or you can add the options.AddArgument("---printing"); to automatically click the print button.

https://stackoverflow.com/questions/30452395/selenium-pdf-automatic-download-not-working

## Docker Images

https://hub.docker.com/u/selenium

https://github.com/dclong/docker-jupyterhub-selenium-chrome

https://github.com/dclong/docker-jupyterhub-selenium-firefox

https://github.com/dclong/docker-selenium

## References

https://stackoverflow.com/questions/30452395/selenium-pdf-automatic-download-not-working

https://stackoverflow.com/questions/31136581/automate-print-save-web-page-as-pdf-in-chrome-python-2-7
