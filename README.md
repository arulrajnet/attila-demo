Attila Demo
----------------

This is the demo blog of theme [attila](https://github.com/arulrajnet/attila). Blog powered by pelican, hosted on [https://arulrajnet.github.io/attila-demo](https://arulrajnet.github.io/attila-demo)


### Setup

you can take this repo as reference point to start static bloging

**Requirements**

Install below python modules

    sudo apt-get install python3-pip python3-dev
    sudo pip3 install -U pelican Markdown fabric2 ghp-import s3cmd pysvg Pygments requests webassets pillow jsmin cssmin BeautifulSoup4

**Install attila theme**

    git clone https://github.com/arulrajnet/attila
    sudo pelican-themes -i ${PWD}/attila
    pelican-themes -l

**To build**

Clone the blog

    git clone https://github.com/arulrajnet/attila-demo
    cd attila-demo
    git submodule update --init --recursive
    git fetch --recurse-submodules
    git pull --recurse-submodules

fabric commands

    fab2 help
    fab2 build
    fab2 serve

Then visit [http://localhost:8000](http://localhost:8000)

**To publish**

    fab2 gh_pages
