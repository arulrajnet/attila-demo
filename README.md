Attila Demo
----------------

- [Attila Demo](#attila-demo)
  - [Setup](#setup)
  - [Clone and install theme](#clone-and-install-theme)
  - [Convert to your blog](#convert-to-your-blog)
  - [Build](#build)

This is the demo blog of theme [attila](https://github.com/arulrajnet/attila). Blog powered by pelican, hosted on [https://arulrajnet.github.io/attila-demo](https://arulrajnet.github.io/attila-demo)


### Setup

you can take this repo and start static [blogging](#convert-to-your-blog)

**Requirements**

Install python3 depends on your OS

    sudo apt-get install python3-pip python3-dev

Install virtualenv module

    sudo pip3 install -U virtualenv

### Clone and install theme

Clone the blog

    git clone --depth=1 https://github.com/arulrajnet/attila-demo
    cd attila-demo
    git submodule init
    cd pelican-plugins
    git pull
    git checkout master
    cd ..
    git submodule update --init --recursive

Install the following module for pelican inside `attila-demo` folder

    virtualenv .venv
    source .venv/bin/activate
    pip install .

To activate virtualenv in windows(git-bash)

    source .venv/Scripts/activate

**Install attila theme**

This is not needed. All the required dependencies are already installed. This is just an example to install the theme.

    pip install git+https://github.com/arulrajnet/attila.git@master

OR

    git clone --depth=1 https://github.com/arulrajnet/attila
    pelican-themes -i ${PWD}/attila
    pelican-themes -l

Install using pip is recommended

### Convert to your blog

* Change [author](https://github.com/arulrajnet/attila-demo/blob/master/pelicanconf.py#L5), sitename and description
* Change [social](https://github.com/arulrajnet/attila-demo/blob/master/pelicanconf.py#L39) links
* Change [disqus](https://github.com/arulrajnet/attila-demo/blob/master/pelicanconf.py#L133) and google analytics
* Change [author bio](https://github.com/arulrajnet/attila-demo/blob/master/pelicanconf.py#L173C1-L173C13)
* Change [site url](https://github.com/arulrajnet/attila-demo/blob/master/publishconf.py#L13)
* Delete existing content. `rm -rf content/*`
* Update the git config and push to your repo.

Note: Change your branch name instead of "main"

```
rm -rf .git
git init
git remote add origin https://github.com/username/new-repository.git
git branch -M main
git push -u origin main
```

### Build

invoke commands

    invoke --list
    invoke build
    invoke serve

OR make commands

    make help
    make html
    make serve

Then visit [http://localhost:8000](http://localhost:8000)

**To publish**

    invoke gh-pages

OR

    make publish
    make github
