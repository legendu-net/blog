UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Title: Tips for Vimperator
Date: 2017-01-02 22:35:52
Slug: vimperator-tips
Category: Software
Tags: tips, software, Vimperator, Firefox, Vim

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
It is not meant to readers but rather for convenient reference of the author and future improvement.
**
 
1. Shift + ESC temporarily disables vimperator, type it again enable ...

2. gt, d, u, o, T, t, c, v, zi, zo, zz

3. :bma -f=toolbar/blogs -k=... 

4. use :! to run command, but how can I can run user-defined command? 

5. one possible way to send links is to use external commands if you can setup a mail server ...

6. y yanks the current link to the clipboard, see how can you read the clipboard and then send the link to your own email ...

7. you can define your own vimperator command to simply important jobs ...

8. when using f/F for navigation, 
you can also use words in the link that you want to navigate to instead of numbers. 
This make things very convenient.

9. use :hardcopy to print a web page

## Disable Vimperator 

http://stackoverflow.com/questions/14271624/disable-vimperator-temporarily

shift + esc

autocmd LocationChange .*                             js modes.passAllKeys = false
autocmd LocationChange mail\\.google\\.com            js modes.passAllKeys = true
autocmd LocationChange www\\.google\\.com/calendar    js modes.passAllKeys = true
autocmd LocationChange www\\.google\\.com/reader      js modes.passAllKeys = true
autocmd LocationChange mail\\.google\\.com/tasks      js modes.passAllKeys = false

ignorekeys add mail.yahoo.com
ignorekeys add mail.google.com
