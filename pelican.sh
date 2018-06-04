#!/usr/bin/env bash

# run Pelican to complie Markdown files to HTML

pelican home -s home/pconf_ld.py
pelican en -s en/pconf_ld.py
pelican cn -s cn/pconf_ld.py
pelican mis -s mis/pconf_ld.py
