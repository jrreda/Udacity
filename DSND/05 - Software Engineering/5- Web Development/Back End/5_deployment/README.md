In this exercise, you'll deploy a web app to **Heroku**. The files you'll need are in the *5_deployment* folder.

Here are the steps:
1. Run the web app inside the 5_deployment folder. In the terminal, use this command to get the link for viewing the app:  
`env | grep WORK`.

The link will be:  
http://WORKSPACESPACEID-3001.WORKSPACEDOMAIN replacing WORKSPACEID and WORKSPACEDOMAIN with your values.

To run the web app, go into the Terminal and type:  
```
cd 5_deployment
python worldbank.py
```
Make sure that the web app is working locally.

2. Next, a new folder was created for the web app and all of the web app folders and files were moved into the folder:  
`mkdir web_app
mv -t web_app data worldbankapp wrangling_scripts worldbank.py`

3. The next step was to create a virtual environment and then activate the environment:  
`conda update python
python3 -m venv worldbankvenv
source worldbankvenv/bin/activate`

4. Then, pip install the Python libraries needed for the web app:  
`pip install flask pandas plotly gunicorn`

5. The next step was to install the [heroku command](https://devcenter.heroku.com/articles/heroku-cli#standalone-installation) line tools:  
`curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
heroku --version`


6. Next, go to https://www.heroku.com and create an account if you haven't already. And then log into heroku with the following command:  
`heroku login`

Heroku asks for your account email address and password, which you type into the terminal and press enter.

7. The next steps involved some housekeeping:  
- remove `app.run()` from *worldbank.py*.
- type `cd web_app` into the Terminal so that you are inside the folder with your web app code.

8. Then create a *procfile*, which tells Heroku what to do when starting your web app, and put 'web gunicorn worldbank:app' in it using this command:  
`echo 'web gunicorn worldbank:app' > Procfile`

9. Next, create a *requirements.txt* file, which lists all of the Python library that your app depends on:  
`pip freeze > requirements.txt`

10. And initialize a git repository (Heroku) and make a commit:  
```
git init
git add .
git commit -m 'first commit'
```


11. Now, create a heroku app:  
`heroku create my-app-name`  
where my-app-name is a unique name that nobody else on Heroku has already used.

12. The `heroku create` command should create a git repository on Heroku and a web address for accessing your web app. You can check that a remote repository was added to your git repository with the following terminal command:  
`git remote -v`

13. Next, you need to push your git repository to the remote heroku repository with this command:  
`git push heroku master`
Now, you can type your web app's address in the browser to see the results.



Go to the link for your web app to see if it's working. The link should be https://app-name.heroku.com.
