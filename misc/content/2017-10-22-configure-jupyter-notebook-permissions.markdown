UUID: 79c95947-045f-40e9-b781-5210b10756c2
Status: published
Date: 2017-10-22 10:40:09
Author: Ben Chuanlong Du
Slug: configure-jupyter-notebook-permissions



1. umask in /etc/profile or /etc/bashrc doesn't work in docker,
which is strange.
Changing UMASK 022 in /etc/login.defs doesn't work either ...

[[:space:]] is recommended for sed

Had issues, tried to set /etc/profile, /etc/bashrc, in an init script, none of them worked worked well,
For JupyterHub, you can configure in the *.py file
https://github.com/jupyterhub/jupyterhub/issues/1402

2. setfacl, getfacl, umask all are useful ...

setfacl, etc. works partially, 
there is currently a bug in jupyter notebook 
and I have file a issue on GitHub for them for fix it.

3. inotify can be used as a temporary solution 

    #!/bin/bash
    dir=/jupyter
    inotifywait -m -r -e create --format '%w%f' "$dir" | while read f; do
        if [[ -d "$f" ]]; then
            chmod 775 "$f"
        fi
    done
