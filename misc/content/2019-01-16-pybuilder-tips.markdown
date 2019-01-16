UUID: e853fa52-9673-49d0-9ff9-c39216d73964
Status: published
Date: 2019-01-16 09:30:41
Author: Ben Chuanlong Du
Slug: pybuilder-tips
Title: Pybuilder Tips
Category: Programming
Tags: programming, pybuilder, Python, project management

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
It is not meant to readers
but rather for convenient reference of the author and future improvement.
**

https://dev.to/awwsmm/managing-your-python-project-with-git-and-pybuilder-21if

https://pybuilder.readthedocs.io/en/latest/walkthrough-new.html

http://pybuilder.github.io/documentation/tutorial.html#.XC-5d_x7nmE

https://python-packaging.readthedocs.io/en/latest/minimal.html


pybuilder check and format code?

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

