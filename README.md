Attila Demo
----------------

This is the demo blog of theme [attila](https://github.com/arulrajnet/attila). Blog powered by pelican, hosted on [https://arulrajnet.github.io/attila-demo](https://arulrajnet.github.io/attila-demo)


### Setup

you can take this repo as reference point to start static bloging

**Requirements**

Install python3 depends on your OS

    sudo apt-get install python3-pip python3-dev

Install virtualenv module

    sudo pip3 install -U virtualenv

### Clone and install theme

Clone the blog

    git clone --depth=1 https://github.com/arulrajnet/attila-demo
    cd attila-demo
    git submodule update --init --recursive
    git fetch --recurse-submodules
    git pull --recurse-submodules

Install the following module for pelican inside `attila-demo` folder

    virtualenv .venv
    source .venv/bin/activate
    pip3 install -U pelican Markdown ghp-import invoke awscli pysvg Pygments requests webassets pillow jsmin cssmin BeautifulSoup4

To activate virtualenv in windows

    source .venv/Scripts/activate

**Install attila theme**

    git clone --depth=1 https://github.com/arulrajnet/attila --depth=1
    pelican-themes -i ${PWD}/attila
    pelican-themes -l

### Convert to your blog


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

    invoke publish
    invoke gh_pages

OR

    make publish
    make github
