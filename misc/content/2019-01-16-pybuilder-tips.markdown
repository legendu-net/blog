UUID: e853fa52-9673-49d0-9ff9-c39216d73964
Status: published
Date: 2019-01-16 09:30:41
Author: Ben Chuanlong Du
Slug: pybuilder-tips
Title: PyBuilder Tips
Category: Programming
Tags: programming, PyBuilder, Python, project management

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

## Jump Start a Python 3 Project Using pybuilder

1. Install the Python package venv if you haven't. 

        wajig install python3-venv 

2. Create a directory for your new project (e.g., myproj).

        mkdir myproj

3. Change directory to the created directory. 

        cd myproj 

4. Create a new virtual environment.

        python3 -m venv venv 

5. Activate the virtual environment.

        source venv/bin/activate 

5. Install `pybuilder` in the virtual environment.

    pip3 install pybuilder
   
6. Run the `pyb` command to initialize your project.

    pyb --start-project 


## Copy/Install Non-Python Files
```
from pybuilder.core import use_plugin, init
 	 
use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("copy_resources")
 	 
name = "demo_proj"
version = "0.0.1"
default_task = "publish"
 	 
 	 
@init
def set_properties(project):
 	project.set_property("coverage_break_build", False)
 	project.depends_on_requirements("requirements.txt")
 	project.get_property("copy_resources_glob").append("src/main/resources/*.jar")
 	project.set_property("copy_resources_target", "$dir_dist")
 	project.install_file("share/demo_proj/", "src/main/resources/ojdbc14.jar")
 	project.install_file("share/demo_proj/", "src/main/resources/tdgssconfig.jar")
 	project.install_file("share/demo_proj/", "src/main/resources/terajdbc4.jar")
```

https://stackoverflow.com/questions/37409282/pybuilder-non-python-files-are-not-packaged


## References

https://pybuilder.readthedocs.io/en/latest/walkthrough-new.html

http://pybuilder.github.io/documentation/tutorial.html#.XC-5d_x7nmE
