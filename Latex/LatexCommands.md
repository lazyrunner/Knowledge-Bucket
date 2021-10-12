# Latex Commands 

## Author Sudeshna Bora 

---

### What is a .cls file ? 

It is a class file in latex. 
Class files help users generate documents with the same style and structure.
A class file simply has ```<class_name>.cls``` as its filename.

To identify a class template, we use ```class identification```.

```
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cv_sudeshna}[2021/10/12 My custom CV class]
```
Here, ```\NeedsTeXFormat``` gives us the information of the ```LaTex``` edition required. 
```\ProvidesClass``` gives us identification of the class template being created. The first parameter is same as the class file name. The second parameter gives
the latest date of modification and description. 

---

### What is \LoadClass command ?

It is a command that is used to load one other class. 
Usually when writing a document, the template of the class we will use is loaded using ```\DocumentClass```. 
This command allows loading one more class in the ```.cls``` file, this class will be the base class which will be modified by the class to create a custom template.
So, imagine it to be like the boilerplate.

Like other commands pertaining to class and packages. 
The syntax for ```\LoadClass``` is 

```
\LoadClass[option]{referred_class_name}

eg: 
\LoadClass{article}
```

This example loads the [article](https://ctan.org/pkg/article) class. The ```[option]``` are the optional parameter to be used while loading this class. 

---
