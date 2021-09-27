Status: published
Date: 2014-12-18 15:05:35
Author: Ben Chuanlong Du
Slug: vimium-tips
Title: Navigate Chrome Browser Like a Pro Using Vimium 
Category: Software
Tags: software, Chrome, Vimium, Vim, plugin, add-on, addon
Modified: 2021-09-25 19:38:42

**
Things on this page are
fragmentary and immature notes and thoughts of the author.
Please read with your own judgement!
**


## Customize Key Mappings

1. Open Vimium Options.

2. Paste your customized key mappings into "Custom key mappings".
    Below is an example of my customized key mapping configuration.

        :::text
        map d removeTab
        map u restoreTab
        unmap x
        unmap X
        map <c-d> scrollPageDown
        map <c-u> scrollPageUp
        map <c-f> scrollFullPageDown
        map <c-b> scrollFullPageUp

3. Click the "Save changes" button at the bottom-left corn.
