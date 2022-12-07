Status: published
Date: 2019-03-27 10:12:19
Author: Benjamin Du
Slug: commonly-used-file-formats-for-configuration
Title: Commonly Used File Formats for Configuration
Category: Computer Science
Tags: programming, configuration, JSON, YAML, TOML, XML, file format
Modified: 2021-09-26 16:11:03

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. JSON is more commonly used for application data and configurations  
    which are not intended to be read by human directly.

2. TOML and YAML are more popular for application configurations 
    which are maintained by human directly.
    Both of them supports comments (in contract to JSON)
    which improves readability.

## JSON

## [YAML](https://yaml.org/)

## [TOML](https://github.com/toml-lang/toml)

## XML

## [translate/translate](https://github.com/translate/translate)

## Configuration Languages
    
When you need your application to be very "configurable" in ways that you cannot imagine today, then what you really need is a plugins system. You need to develop your application in a way that someone else can code a new plugin and hook it into your application in the future.

Every Sufficiently Advanced Configuration Language is Wrong
https://matt-rickard.com/advanced-configuration-languages-are-wrong

Against The Use Of Programming Languages in Configuration Files
https://taint.org/2011/02/18/001527a.html

At what point does a config file become a programming language?
https://stackoverflow.com/questions/648246/at-what-point-does-a-config-file-become-a-programming-language/

### Use a General Purpose Programming Language

### [jsonnet](https://github.com/google/jsonnet)
[jsonnet](https://github.com/google/jsonnet)
is the data templating language.

### [Dhall](https://github.com/dhall-lang/dhall-lang)

## References

https://www.zionandzion.com/json-vs-xml-vs-toml-vs-cson-vs-yaml/
