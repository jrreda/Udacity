# Introduction to Object-Oriented Programming (OOP)


**Lesson Outline:**

* Object-oriented programming syntax:  
1. procedural vs object-oriented programming  
2. classes, objects, methods and attributes  
3. coding a class  
4. magic methods  
5. inheritance  

* Using object-oriented programming to make a Python package:
1. making a package  
2. tour of scikit-learn source code  
3. putting your package on PyPi


### Why Object-Oriented Programming?

Object-oriented programming has a few benefits over procedural programming, which is the programming style you most likely first learned. As you'll see in this lesson:  

- object-oriented programming allows you to create large, modular programs that can easily expand over time.  
- object-oriented programs hide the implementation from the end-user.  

Consider Python packages like [Scikit-learn](https://github.com/scikit-learn/scikit-learn), [pandas](https://pandas.pydata.org/), and [NumPy](http://www.numpy.org/). These are all Python packages built with object-oriented programming. Scikit-learn, for example, is a relatively large and complex package built with object-oriented programming. This package has expanded over the years with new functionality and new algorithms.

When you train a machine learning algorithm with Scikit-learn, you don't have to know anything about how the algorithms work or how they were coded. You can focus directly on the modeling.


## OOP Vocabulary

* **class** - a blueprint consisting of methods and attributes.  
* **object** - an instance of a class. It can help to think of objects as something in the real world like a yellow pencil, a small dog, a blue shirt, etc. However objects can be more abstract.  
* **attribute** - a descriptor or characteristic. Examples would be color, length, size, etc. These attributes can take on specific values like blue, 3 inches, large, etc.  
* **method** - an action that a class or object could take.  
* **OOP** - a commonly used abbreviation for object-oriented programming.  
* **encapsulation** - one of the fundamental ideas behind object-oriented programming is called encapsulation: you can combine functions and data all into a single entity. In object-oriented programming, this single entity is called a class. Encapsulation allows you to hide implementation details much like how the [Scikit-learn](https://github.com/scikit-learn/scikit-learn) package hides the implementation of machine learning algorithms.  
* **Python module** - is just a Python file containing code.  
* **package** - is a collection of Python modules. Although the previous code might already seem like it was a Python package because it contained multiple files, a Python package also needs an `__init__.py` file.   
*  **virtual environment** - is a silo-ed Python installation apart from your main Python installation. That way you can install packages and delete the virtual environment without affecting your main Python installation.


In English, you might hear an attribute described as a property, description, feature, quality, trait, or characteristic. All of these are saying the same thing.  

Here is a reminder of how a class, object, attributes and methods relate to each other.

<img src='CLASS-vs-OBJECTS.png' alt="CLASS-vs-OBJECTS" width="80%;"/>


## A Note about Attributes

There are some drawbacks to accessing attributes directly versus writing a method for accessing attributes.

In terms of object-oriented programming, the rules in Python are a bit looser than in other programming languages. As previously mentioned, in some languages, like C++, you can explicitly state whether or not an object should be allowed to change or access an attribute's values directly. Python does not have this option.  

Why might it be better to change a value with a method instead of directly? Changing values via a method gives you more flexibility in the long-term.  


## Advanced OOP Topics

Inheritance is the last object-oriented programming topic in the lesson. Thus far you've been exposed to:  

- classes and objects  
- attributes and methods  
- magic methods  
- inheritance  

Classes, object, attributes, methods, and inheritance are common to all object-oriented programming languages.  

Knowing these topics is enough to start writing object-oriented software. What you've learned so far is all you need to know to complete this OOP lesson. However, these are only the fundamentals of object-oriented programming.

Here is a list of resources for advanced Python object-oriented programming topics.

- **[class methods, instance methods, and static methods](https://realpython.com/instance-class-and-static-methods-demystified/)** - these are different types of methods that can be accessed at the class or object level.  
- **[class attributes vs instance attributes](https://www.python-course.eu/python3_class_and_instance_attributes.php)** - you can also define attributes at the class level or at the instance level.  
- **[multiple inheritance, mixins](https://easyaspython.com/mixins-for-fun-and-profit-cb9962760556)** - A class can inherit from multiple parent classes.  
- **[Python decorators](https://realpython.com/primer-on-python-decorators/)** - Decorators are a short-hand way for using functions inside other functions.  



## Virtual Environments

If you decide to install your package on your local computer, you'll want to create a virtual environment. That way you can install packages and delete the virtual environment without affecting your main Python installation.  

Let's talk about two different Python environment managers: conda and venv. You can create virtual environments with either one.  


#### [Conda](https://conda.io/docs/)

**[Conda](https://conda.io/docs/)** does two things: manages packages and manages environments.  

As a package manager, conda makes it easy to install Python packages especially for data science. For instance, typing `conda install numpy` will install the numpy package.  

As an environment manager, conda allows you to create silo-ed Python installations. With an environment manager, you can install packages on your computer without affecting your main Python installation.  

The command line code looks something like this:  
```
conda create --name environmentname
source activate environmentname
conda install numpy
```

#### Pip and Venv

There are other environmental managers and package managers besides conda. For example, venv is an environment manager that comes pre-installed with Python 3. Pip is a package manager.

Pip can only manage Python packages whereas conda is a language agnostic package manager. In fact, conda was invented because pip could not handle data science packages that depended on libraries outside of Python. If you look at the [history of conda](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/#Myth-#5:-conda-doesn't-work-with-virtualenv,-so-it's-useless-for-my-workflow), you'll find that the software engineers behind conda needed a way to manage data science packages (NumPy, Matplotlib, etc.) that relied on libraries outside of Python.  

Conda manages environments AND packages. Pip only manages packages.  

To use venv and pip, the commands look something like this:  
```
python3 -m venv environmentname
source environmentname/bin/activate
pip install numpy
```



## Putting Code on PyPi

Note that **[pypi.org](https://pypi.org/)** and **[test.pypy.org](https://test.pypi.org/)** are two different websites. You'll need to register separately at each website. If you only register at **[pypi.org](https://pypi.org/)**, you will not be able to upload to the **[test.pypy.org](https://test.pypi.org/)** repository.  

Also, remember that your package name must be unique. If you use a package name that is already taken, you will get an error when trying to upload the package.  

#### Summary of the Terminal Commands

```
cd binomial_package_files
python setup.py sdist
pip install twine

# commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ dsnd-probability

# command to upload to the pypi repository
twine upload dist/*
pip install dsnd-probability
```
