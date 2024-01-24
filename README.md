# Lab 01: Intermediate Python

## Overview
In this lab, you'll prepare your development environment and learn (or refresh your knowledge of) some important features of the Python programming language. You may use your own machine or a department machine for lab.

### Learning objectives
After completing this lab, you should be able to do the following in Python:
* Create and call functions with required and optional parameters
* Create and use classes with constructors, instances variables, instance methods, property methods, class methods, and built-in methods
* Use lists and dictionaries

## Part 1: Prepare your development environment
We will be using the CS department's "tigers" pool of Linux servers for all our work this semester. You must be **connected to the `Eduroam` wireless network or [use VPN](https://www.colgate.edu/about/campus-services-and-resources/vpn-connections-campus-network)** to access the servers.

### Configure VS Code
If you are using your own machine to access the servers, [download](https://code.visualstudio.com) and install VS Code. If your computer is running Windows 10, you will also need to install the [OpenSSH client](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse).

Note: VS Code and SSH are already installed on all department machines.

After you have installed VS Code:
1. Click on the <img src="https://code.visualstudio.com/assets/docs/editor/extension-marketplace/extensions-view-icon.png" width="30px"> icon on the left of the VS Code window. 
2. Search for the `Remote - SSH` extension in the left panel, and click `Install` on the top of the right panel. 
3. Click the opposing arrows icon in the lower-left of your VS Code window:

    ![Screenshot of Remote Development icon in VS Code](https://microsoft.github.io/vscode-remote-release/images/remote-dev-status-bar.png)

4. In the command palette at the top of the VS Code window, select `Connect to Host...`, then `Add new SSH Host`. 
5. Fill in the command `ssh YOU@TIGER.cs.colgate.edu`, **replacing `YOU` with your CS username** (**NOT** your Colgate username) and **replacing `TIGER` with `caspian`, `bengal`, `javan`, or `malayan`**
6. When asked which SSH configuration file to update, select the file located in your user directory (usually the first file in the list).

To connect to the servers:
1. Click on the opposing arrows icon, in the lower-left corner of your VS Code window. 
2. Choose `Connect to Host...`, then select `TIGER.cs.colgate.edu` (where `TIGER` will be the name of the server you chose)
3. If prompted, select `Continue` to connect to the server with fingerprint `SHA256:Fx96G/IqfDhj3vXjsVW3DQMRkcS9CYKgUJGFJoWcJ8Q`
4. Enter your CS password.
5. After you are connected, `SSH: TIGER.cs.colgate.edu` will appear after the opposing arrows icon in the lower-left of your VS Code window.

For additional information and help with the VS Code SSH remote editing capability, click the opposing arrows icon in the lower left, then choose the menu option `Remote-SSH: Help`.

### Configure git
You must configure your git environment on the servers for this course. After you have connected to the servers, enter the following commands in a terminal in VS Code (**substituting your own name and email**):
```bash
git config --global user.name "Marian Croak"
git config --global user.email "mcroak@google.com"
ssh-keygen -f ~/.ssh/id_rsa -N ""
cat ~/.ssh/id_rsa.pub 
```

(Note: Marian Croak is a black computer scientist who [developed the Voice over Internet Protocol (VoIP)](https://www.invent.org/inductees/marian-croak). She is currently the [Vice President of Responsible AI and Human Centered Technologies](https://blog.google/authors/marian-croak) at Google.)

The last command will display your newly generated public key. Copy the entire key, then go to [https://github.com/settings/keys](https://github.com/settings/keys). Click `New SSH key`, enter `COSC 465` for the title, and paste the copied key into the `Key` textbox. Click `Add SSH key`.

## Part 2: Interactive Networking Glossary
Networking is full of acronyms. To help you decode these acronyms and expand/refresh your Python programming skills, you will write part of a Python program that implements an interactive glossary.

**THE INSTRUCTIONS THAT FOLLOW ARE INTENTIONALLY UNDERSPECIFIED! This is a 400-level computer science course, so I expect you can lookup documentation and/or examples. Always read examples carefully and look at multiple examples, because the first example you find may not be the correct/best/common way to accomplish your goal.**

### Getting started
To get started, **clone your git repository for this lab into your home directory on the tigers servers**. (If you don't remember how to do this from COSC 208, consult [GitHub's documentation on Basic Git commands](https://docs.github.com/en/get-started/using-git/about-git#basic-git-commands).)

Run the partially implemented interactive glossary program using the command:
```bash
python3 reference.py
```

**🧑🏽‍💻 TODO:** Follow the instructions output by the program to learn how to:
* List all the terms in the glossary
* Lookup a term based on an acronym
* Lookup terms based on a keyword
* Run a function with testing code

### Term class
Now look at the code in `reference.py`. The `test` function, which is called by the `main` function, first creates two `Term` objects, which are used to represent terms in the glossary.

The `Term` class is defined in `terminology.py` and includes a constructor (`__init__`), a property method (`acronym`), and an instance method (`matches`). Notice that the first parameter of all three methods is `self`, which is akin to the `this` keyword in Java. 

#### Constructor
The constructor, which is always named `__init__`, also takes a required parameter called `term` and an optional parameter called `keywords`. We know the `keywords` parameter is optional, because it is followed by `=[]`, which means an empty list will be used for the `keywords` parameter if no value for this parameter is provided to the constructor.

The constructor initializes one instance variable: `_term`. By convention, instance variables always start with an underscore (`_`). Including `self.` before the variable indicates it is an instance variables. If we did not include `self.` before `_term`, then we would create a local variable `_term`, which would be inaccessible from other methods in the class.

**🧑🏾‍💻 TODO:** Modify the constructor in the `Term` class to also initialize a `keywords` instance variable that takes the value of the `keywords` parameter passed to the constructor.

#### Property methods
The `@property` annotation before the `acronyms` method indicates this is a like a `get` method in Java and returns some value associated with the object.

**🧑🏼‍💻 TODO:** Add a `keywords` method to the `Term` class that returns a sorted list of the keywords. (Hint: see the [Sorting HOW TO](https://docs.python.org/3.12/howto/sorting.html) in the Python documentation)

**🧑‍💻 TODO:** Modify the `test` method in `reference.py` to print the keywords of each term in a semicolon-separated list. (Hint: either call the `join` method on the list of keywords or use the optional `sep` parameter in your call to `print`)

#### Instance methods
The `matches` method is a regular instance method with takes a `keyword` as a parameter and checks if that keyword appears in any of the keywords associated with the term.

**👩🏼‍💻 TODO:** Uncomment the calls to the `matches` method in the `test` method in `reference.py` and make sure the program produces the correct output (which it should if you have completed the above TODOs correctly).

#### Built-in methods
Some methods exist for every class in Python and have a default behavior that can be overridden by adding the method to your class. For example the `__str__` method is akin to the `toString` method in Java. Currently the default method is being used when `term1` and `term2` are printed in the `test` function in `reference.py`.

**👩🏽‍💻 TODO:** Add a `__str__` method to the `Term` class that provides the term followed by its acronym in parenthesis. For example, `print(term1)` should now output `Virtual Private Network (VPN)`.

### Glossary class
**👩🏻‍💻 TODO:** Add a `Glossary` class to `terminology.py`. The class should include:
* A constructor which initializes an instance variable to an empty dictionary
* A `terms` property method that returns a list of `Term` objects sorted in alphabetical order by acronym (Hint: iterate over the keys of the dictionary in sorted order, or implement the built-in `eq` and `lt` methods for the `Term` class and sort the list of values from the dictionary)
* An `add` instance method which takes a `Term` object and adds it the dictionary, using the term's acronym as the key
* A `lookup_by_acronym` instance method which takes an acronym (i.e., a string) and returns the corresponding `Term` object from the dictionary, or `None` if there is no such term in the dictionary with that acronym
* A `lookup_by_keyword` instance method which takes a keyword (i.e., a string) and returns a list of `Term` objects whose `matches` method returns `True` for that keyword

**🧑🏻‍💻 TODO:** Test your `Glossary` class by uncommenting the remaining code in the `test` method in `reference.py`.

#### Class methods
Class methods in Python are like static methods in Java: they are invoked using the class name instead of an instance of the class (i.e., an object). Adding the `@classmethod` decorator before a method defined in class will make it a class method. Also, the first parameter of a class method should be `cls`, not `self`, because the method is called on the class not an instance of the class.

**👩🏼‍💻 TODO:** Add a `load` class method to your `Glossary` class that takes an optional parameter `filename` whose default value is `networking.json`. The `load` method should:
* Open the corresponding file
* Convert the contents of the file into a dictionary using the `json` Python module
* Create `Term` objects for each entry in the dictionary
* Add the created `Term` objects to a new `Glossary` object that is created and returned by the `load` method

**👨🏼‍💻 TODO:** Uncomment the call to the `load` method in `main` in `reference.py`. Run the `reference.py` program to confirm that you can lookup terms by their acronym.

### More features
If there is time remaining in lab (or to get more practice after lab), continue to develop your interactive networking glossary program.

**🧑‍💻 TODO:** Modify the `display_terms` function in `reference.py` to list all terms (and their acronyms) contained in the glossary; you can decide whether you want to include the keywords for each term in the output.

**👨🏾‍💻 TODO:** Implement the `lookup_keyword` function in `reference.py` to output a list of terms that match the keyword specified on the command-line.

**👩🏿‍💻 TODO:** The acronym for some networking terms is not simply the first letter of each word. For example, the acronym for the `Hypertext Transfer Protocol` is `HTTP`, but your program currently outputs `HTP`. Modify the `Term` class to take an optional acronym parameter that can be used to override the "inferred" acronym. Modify the contents of `networking.json` to include the correct acronym for the `Hypertext Transfer Protocol` and modify the `load` method in the `Glossary` class to properly pass this information to the `Term` constructor.

**👨🏻‍💻 TODO:** Your program doesn't have to be limited to networking. Create your own JSON file with terms and keywords for a different category. Modify the call to `load` in `main` in `references.py` to load your custom JSON file instead. Better yet, modify argument parser code at the beginning of `main` to include an optional command-line parameter for specifying which JSON file to load.

## Self-assessment
The self-assessment for this lab will be available on Moodle after 5pm on Thursday, January 25. Please complete the self-assessment by 11pm on Monday, January 29.