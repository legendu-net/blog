UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Date: 2015-08-26 22:03:20
Slug: use-eclipse-as-your-ide
Author: Ben Chuanlong Du
Title: Use Eclipse as Your IDE
Category: Software
Tags: IDE, programming, Eclipse, software, editor, 


1. There are at least 3 ways to jump to errors quickly in Eclipse

    - Click these red icons on the right margin.
    - Click the `Previous Annotation` button 
    or `Next Annotation` buttons on the tool bar or under the `Navigation` menu.
    - Use hot keys (`Ctrl+.` for `Next Annotation` and `Ctrl+,` for `Previous Annotation` by default).

2. To tidy code, 
use the `Format` button under the `Source` menu.

3. To quickly comment selected code in Eclipse, 
you can use hot keys `Crtl+/`. 
To uncomment selected code, 
simply press the hot keys again.

4. To quickly import a package which has no `.jar` files 
(i.e. you have available all source code) to an existing project, 
you can simply drag the package on the `src` folder 
in the corresponding project in eclipse. 
Another way is to first create a new package with the same
name as the existing package, 
then right click on the newly created
package and choose `Import...` in the short menu. 
In the prompt out,
you can choose either `Archive File` or `File System` under
the `General` tab depending on whether there are `.jar` files in the package
or not. 
Then you can choose which files you want to import into
the package and click finish after you have done.

5. To change a variable name, you'd better use refactor which will
automatically change all occurrences.

6. Use `TODO` to add task in eclipse.

7. To build projects manually, 
follow instructions 
[here](http://help.eclipse.org/helios/index.jsp?topic=%2Forg.eclipse.platform.doc.user%2Ftasks%2Ftasks-75.htm).

