Welcome to this starter repository.

The learning curve for Github can be steep and it's helpful to have a reference when creating your projects or investigating other people's projects. 

This repo should help introduce you to the most important pieces of a project. While it does not contain every possible file type – in fact, I leave out **a lot** – it should provide the bare necessities.

In this example I am using Python, but there is very little in here that is Python specific.

# Table of contents

* [Files](#files)
  * [README.md](#readmemd)
  * [Script.py](#scriptpy)
  * [.gitignore](#gitignore)
  * [secrets.json](#secretsjson)
  * [License](#license)
* [Issues](#issues)
* [Wikis](#wikis)
* [Pull request](#pull-request)
* [Forks](#forks)
* [Contact](#contact)

# Files

Below are a series of files that are common in Github repos. Again, this list is not exhaustive, if you come across a file you don't recognize Google it or ask the author.

## README.md

The most important piece of any repository is your README document. This should act as an introduction to the code and explain what everything does. A README is displayed by default on the home page of your repository on Github.

READMEs serve two main purposes in my mind. First, they should explain exactly how your code works to someone who has never seen it before. This is vitally important for open source projects or private work projects if you hire someone new. Often, READMEs provide the only documentation for a new hire and can totally save that person if the code author is no longer with the company. I am speaking from experience, please document your code as if someone new will have to maintain it without any help from you.

Second, they force you to write about your project in a way that makes you to think critically about your choices. When working on a project, you might take some shortcuts or make decisions that would not be obvious to the casual reader. A README provides a space for you to explain those decisions and forces you to think about them a second time. And sometimes this process helps the writer come up with a better solution than they had in the first place.

If your project has multiple directories, each one of those can have a README.

### Style and syntax

A README is typically written in [markdown](https://en.wikipedia.org/wiki/Markdown), which may or may not have [Github flavoring](https://github.github.com/gfm/#what-is-github-flavored-markdown-).

The easiest way to explain markdown is that it provides an easy-to-write syntax for interactive text. It's simpler than HTML but still allows for hyperlinks, styling and some advanced syntax.

The best way to learn markdown, after reading [any of the helpful introductions](https://www.google.com/search?q=markdown+introduction), is to start reading and writing it. I promise, you will pick it up quickly. If you're curious, you can read the raw version of this README [here](https://raw.githubusercontent.com/uohack/starter-repo/master/README.md).

## script.py

Of course, the code is quite important as well. I'm going to breeze right over this because the code will change based on what you're working on and this is more about the repo structure.

Again, your repo does not have to include Python if you want to do Ruby or C or HTML or whatever.

## .gitignore

It took me a while to understand the benefits of a .gitignore file but I use them all the time. These [dotfiles](https://medium.com/@webprolific/getting-started-with-dotfiles-43c3602fd789) are hidden by default becuause they are typically created by the system to store information. 

The function of a .gitignore is to tell Github (really git, but that's a different conversation) which files to ignore.

### An aside: Hidden files

No matter your system (PC or Mac), your computer has a whole bunch of hidden files that you can choose to display. These are files that your computer does not display by default because some of them are important and should not be messed with. In Unix-based systems these files will start with a period, hence the term dotfiles. The dot tells the system that they should be hidden.

On both a PC and a Mac you can toggle the visibility of hidden files. Just Google your OS and "show hidden files" and it should come right up. You may need to do this to see .gitignore files. Please use caution and don't just edit or trash dotfiles on a whim.

### Why would you want to ignore files?

Well, some code processes create logs or cache files that are not necessary to commit to Github. Other times, you'll have secrets files that include passwords or other credentials that you want to keep secret. Maybe you have a bunch of videos or project files (.ai, .psd, .prproj, etc.) and you don't want to put them online.

In any of these cases, you can use a .gitignore to ignore those files from being committed and pushed to Github.

**Use caution though,** if you accidentally commit files you didn't want to, it takes some work to get rid of them. You can't just add them to your .gitignore and hope they disappear from your previous commits. This is not how it works and Github will save all those old commits. Be sure to start your project with a .gitignore and add new files to it as you make them.

If you do find yourself in that situation (we all have), try to make your repo private (it's good to keep one private repo handy) and Google how to get rid of it. Depending on how far you got in the process determines what you need to do to fix it. 

Of course, all of this can be avoided if you use a .gitignore file correctly.

## secrets.json

More and more I find myself using a secrets file to store API credentials, passwords, or other information that I don't want to share with the world. While you may not need one in your first project, I bet you'll need one sooner rather than later.

Your secrets file does not have to be in the JSON format, but all major languages can read and parse JSON so it's a handy format to get familiar with.

You'll note that I have secrets.json commented out in my .gitignore. This is just so I can share this example file. Before you use one in your project, you should obviously uncomment it so that you don't share secrets with the world.

### Getting secrets

You may be wondering how to get at those secrets. Well, I included a method to retrieve secrets in my script.py file. Here's a heavily commented version of that code:

```python
# These are required
import os, json

# Let's define a method to use throughout our script
# There is one required argument and one optional one
def get_secret(service, token='null'):

    # First, we need to figure out where this secrets file is located
    # In this case, it's in the same directory as my script
    # Note: This might require more configuration on more complex projects
    # Note: This requires the os module
    secrets_path = os.path.abspath('.')

    # Now, let's crack open that file as the variable data
    with open("{}/secrets.json".format(secrets_path)) as data:

        # Let's parse the json so we can get at it
        # Note: This requires json to be imported
        s = json.load(data)
        
        # Now we access the data and set a secret variable
        # If there is no token, return whole parent object
        if token == 'null':
            secret = s['{}'.format(service)]
        # If there is a token, we have to go to dig deeper
        else:
            secret = s['{}'.format(service)]['{}'.format(token)]
        
        # Finally we return the secret as a string
        return secret

# Example call
my_secret = get_secret('twitter','consumer-key')
```


### License

I don't want to tell you how to license your stuff, though I always suggest making it open source in the spirit of Github. Read more about licensing [here](https://help.github.com/articles/licensing-a-repository/) and [here](https://choosealicense.com/).

### Other files

There are an infinite number of file types you might need to include for your project. Other common files I see on Github are:

* [.editorconfig](http://editorconfig.org/): Set preferences for your text editor (another hidden file) 
* authors.md: Lists authors of the code base (another markdown file)
* contributors.md: Lists contributors to the code base (another markdown file)
* changelog.md: Lists the changes for official releases (another markdown file)
* index.html: For sites hosted by Github (formerly Github pages), this is your homepage

# Issues

Every repo automatically comes with an issues tab. This can (and should) be used to manage bugs and keep track of random issues that you need to fix. Conversely, if you ever have a problem with an open source project, you can file an issue to report a bug or ask for help.

You can use markdown in issues, as well as upload files to include.

If your repo is public your issues will be too, so be sure not to include secrets in there.

# Wikis

In addition to your README, you can provide documentation in the wikis tab. Typically I use the README for overall documentation and wikis for really specific notes to my future self. 

For example, if I build a Twitter bot, I'll explain the overall purpose and code in the README. Then I might make a wiki page for how to go and find Twitter API credentials and another wiki for future plans I have for the project (like a marketing plan).

Like issues, wikis can be styles using markdown, but you cannot upload files.

Note: In the wikis tab there is only one home wiki, but you can make additional child wikis. If you have a lot of wikis, the home can be a table of contents, for the children. If that doesn't make sense, don't worry about it, you'll see.

# Pull request

If your repo is public, someone could clone it and make changes. Then they can make a pull request with suggested changes. This is how large open source projects work and can be really helpful. For example, I wrote a UOHack workshop on data literacy and had people do pull requests with suggested edits.

# Forks

If you need your own copy of a repo and plan on doing heavy customization then you can fork it. This shows the world that your repo is a fork, but allows you to do whatever you want.

# Contact

Have questions? Email us at hack [at] uohack [dot] com.

Suggestions? File a pull request or get in touch.
