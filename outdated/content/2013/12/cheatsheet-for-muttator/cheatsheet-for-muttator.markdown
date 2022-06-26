UUID: 03a0e2cd-fce2-48ec-9fdd-4addcaad0021
Status: published
Author: Ben Chuanlong Du
Date: 2013-12-19 21:19:59
Title: Cheatsheet for Muttator
Slug: cheatsheet-for-muttator
Category: Software
Tags: software, Muttator, Vim, tips, Mozilla
Modified: 2013-12-19 21:19:59

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**
 
Adopted from http://waxandwane.org/muttator.html

A Muttator Reference Sheet / Cheat Sheet

Muttator v0.6 for Thunderbird v3.0 and 3.1.* (muttator-20100629.xpi)

The main thing to know about using Muttator is that there are two primary modes, EX mode and MESSAGE mode, and keyboard mappings can work very differently in the two modes. It's not obvious which mode you're in; you have to look at the bottom left of your Thunderbird window where the status line with either be blank (EX mode) or will say "-- MESSAGE --". There is also an odd "-- CARET --" mode that you'll probably want to <ESC> out of as soon as possible.

When composing a new message, the two primary modes are "-- COMPOSE --" and "-- INSERT --". While typing in INSERT mode, you can press <ESC> at any time to return to COMPOSE mode.
Mappings in EX mode

i               "Switch to MESSAGE mode"
<Return>, I     "Open the message in new tab"
<Space>         "Scroll message or select next unread one"
t               "Select thread"
d, <Del>        "Move mail to Trash folder"
s               "Move selected messages"
S               "Copy selected messages"
u               "Undo"
<C-r>           "Redo"
gg              "Select first message"
G               "Select last message"
+               "Scroll message down pagewise"
-               "Scroll message up pagewise"
j, <Right>      "Select next message"
gj              "Select next message, including closed threads"
J, <Tab>        "Select next unread message"
k, <Left>       "Select previous message"
gk              "Select previous message"
K               "Select previous unread message"
*               "Select next message from the same sender"
#               "Select previous message from the same sender"
T               "Mark current folder as read",
<C-t>           "Mark all messages as read",
h               "Toggle displayed headers",
x               "Toggle HTML message display",
<C-i>           "Go forward in your navigation history"
<C-o>           "Go back in your navigation history"

SENDING MESSAGES
m               "Compose a new message"
M               "Compose a new message to the sender of selected mail"
r               "Reply to sender"
R               "Reply to all"
f               "Forward message"
F               "Forward message inline"

TAB NAVIGATION
g0, g^          "Go to the first tab"
g$              "Go to the last tab"
gt, <C-Tab>, <C-PgDn>
"Go to the next tab"
gT, <C-S-Tab>, <C-PgUp>
"Go to previous tab"
B               "Show tab (buffer) list"
b               "Open a prompt to switch tabs (buffers)"

MOVING MAIL
<C-s>           "Archive message"
!               "Mark/unmark selected messages as junk"
]s              "Select next starred message"
[s              "Select previous starred message"
]a              "Select next message with an attachment"
[a              "Select previous message with an attachment"

FOLDER SWITCHING
c               "Change folders"
gi              "Go to inbox"
<C-n>           "Select next folder"
<C-N>           "Go to next mailbox with unread messages"
<C-p>           "Select previous folder"
<C-P>           "Go to previous mailbox with unread messages"

THREADING
za              "Toggle thread collapsed/expanded"
zc              "Collapse thread"
zo              "Open thread"
zr, zR          "Expand all threads"
zm, zM          "Collapse all threads"

MISCELLANEOUS MAPPINGS
a               "Save new addressbook entry for sender of selected message"
gm              "Get new messages"
gM              "Get new messages for current account only"
l               "Tag with a  message label"
r               "MsgMarkMsgAsRead"
s               "MsgMarkAsFlagged"
i, 1            "Important"
w, 2            "Work"
p, 3            "Personal"
t, 4            "TODO"
l, 5            "Later"
p               "Open RSS message in browser",
Y               "Yank subject",
y               "Yank sender or feed URL",

Mappings in MESSAGE mode

<ESC>           "Switch to EX mode"
f               "Follow hyperlinks"
/               "Search forward for a pattern"
?               "Search backwards for a pattern"
<C-f>           "Scroll message down by page"
<C-b>           "Scroll message up by page"
<C-d>           "Scroll message down by half page"
<C-u>           "Scroll message up by half page"
<Down>          "Scroll message down by line"
<Up>            "Scroll message up by line"
<Left>          "Select previous message"
<Right>         "Select next message"
+               "Increase text zoom by 10%"
-               "Decrease text zoom by 10%"

Mappings in COMPOSE mode

e               "Edit message in an external editor"
y               "Send message now"
Y               "Send message later"
t               "Select To: field"
s               "Select Subject: field"
i               "Select message body"
q               "Close composer, ask when for unsaved changes"
Q, ZQ           "Force closing composer"

Commands

:addo[ns]           "Manage Add-ons"
:addr[essbook]      "Address book"
:con[tact]          "Add an address book entry"
-firstname, -f
-lastname -l
-name -n
:contacts           "List or open multiple addresses"
:copy[to]           "Copy selected messages"
:dia[log]      "Open a Thunderbird dialog"
about           "About Thunderbird"
addons          "Manage Add-ons"
addressbook     "Address book"
accounts        "Account Manager"
console         "JavaScript console"
preferences     "Show Thunderbird preferences dialog 
printsetup      "Setup the page size and orientation before printing 
print           "Show print dialog 
savepage        "Save page to disk 
:em[enu]            "Execute the specified menu item from the command line"
:empty[trash]       "Empty trash of the current account"
:exta[dd]           "Install an extension"
:extde[lete]        "Uninstall an extension"
:extd[isable]       "Disable an extension"
:exte[nable]        "Enable an extension"
:extens[ions]       "List available extensions"
:exto[ptions]       "Open an extension's preference dialog"
:extp[references]   "Open an extension's preference dialog"
:get[messages]      "Check for new messages"
:go[to]             "Select a folder"
:ha[rdcopy]         "Print current document"
:help               "Open the help page"
:helpall            "Open the single unchuncked help page"
:m[ail]             "Write a new message"
-subject, -s
-attachment, -a
-bcc, -b
-cc, -c
-text -t
:mes[sages]         "Display previously given messages"
:messc[lear]        "Clear the message history"
:move[to]           "Move selected messages"
:pa[geinfo]         "Show various page information"
:pref[erences]      "Show Thunderbird preferences (also :prefs)"
:sav[eas], :w[rite] "Save current document to disk"
:tabc[lose], :q     "Delete current tab"
:tabl[ast]          "Switch to the last tab"
:tabn[ext], :tn[ext]
"Switch to the next or [count]th tab"
:tabp[revious], :tp[revious], :tabN[ext], tN[ext]
"Switch to the previous tab or go [count] tabs back"
:tabr[ewind], :tabfir[st]
"Switch to the first tab"
:b[uffer]           "Switch to a tab (buffer)"
:tabs, :buffers, :ls, :files
"Show a list of all tabs"
:quita[ll], :qa[ll]  "Quit Thunderbird"
:ve[rsion]          "Show version information"
:vie[wsource]       "View source code of current document"

Options

:set archivefolder  "Set the archive folder" (Archive)

:set guioptions     "Set GUI display options (default is 'f')"
m               "Toggle MenuBar"
f               "Toggle Folder List"

:set layout         "Set the layout of the mail window"
inherit         "Default View"
classic         "Classic View"
wide            "Wide View"
vertical        "Vertical View"

:set smtpserver     "Set the default SMTP server"


