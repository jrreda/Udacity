# Upload a Package to PyPi

Build a Python package and upload the package to **[pypi](https://pypi.org/)**. We encourage you to use object-oriented programming and tackle a problem that interests you. The Introduction to Object-Oriented Programming lesson has all of the information needed to create a package and upload the package. As mentioned in the lesson material, you'll need to use a unique name to upload the package to **[pypi](https://pypi.org/)** since each package needs a unique name; hence 'dsnd-probability' will not work since that package name is already taken.  

Here are a few ideas for packages:  

- create a package that does basic matrix algebra such as addition, subtraction, multiplication, matrix inversion, etc.  
- make a calculus package that implements algorithms such as Newton's method.  
- create a package built on top of Matplotlib or Seaborn that creates well-formatted, well labeled visualizations.  
- create an object-oriented package to play a game of tic-tac-toe between two human players.  
- make a number guessing game where the computer randomly chooses an integer and then tells a human player if a guess is higher or lower than the number.

Feel free to come up with your own ideas. The main goal is to develop and demonstrate your skills in object-oriented programming and uploading packages to **[pypi](https://pypi.org/)**.


## Reminders

- include a README file detailing the files in your package and how to install the package.  
- Comment your code - use docstrings and inline comments where appropriate.  
- Refactor code when possible - if you find your functions are getting too long, then refactor your code!  
- Use object-oriented programming whenever it makes sense to do so.  
- You're encouraged to write unit tests! The coding exercises in this lesson contained unit tests, so you can use those tests as a model for your package.  
- Use GitHub for version control, and commit your work often.  


As a reminder, your package should be placed in a folder with the following folders and files:  

- a folder with the name of your package that contains:  
1. the Python code that makes up your package  
2. a `README.md` file  
3. an `__init__.py`  
4. `license.txt`  
5. `setup.cfg`  
- `setup.py` file.



## Uploading to PyPi

When you are ready to upload your package, you can first upload to the [PyPi test repository](https://test.pypi.org/). Once everything is working as expected, you can upload to the public facing [PyPi repository](https://pypi.org/).  

As a reminder, you'll need to create a username for both the test and public facing repositories. You'll also need to pip install the twine package with: `pip install twine`.   


## Package details

* Package link on **[PyPi test](https://test.pypi.org/project/jrreda-distributions/)**.
* Package link on **[PyPi](https://pypi.org/project/jrreda-distributions/)**.


You can download the package by typing `pip install jrreda-distributions` in the Terminal.


### Summary of the Terminal Commands Used to upload the package:

```
cd binomial_package_files
python setup.py sdist
pip install twine

# commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ jrreda-distributions

# command to upload to the pypi repository
twine upload dist/*
pip install jrreda-distributions
```



#### Other Links

If you'd like to learn more about [PyPi](https://pypi.org/), here are a couple of resources:

* [Overview of PyPi](https://docs.python.org/3/distutils/packageindex.html).
* [MIT License](https://opensource.org/licenses/MIT).
