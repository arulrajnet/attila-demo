Attila Demo
----------------

This is the demo blog of theme [attila](http://sdf/). Blog powered by pelican


### Setup

you can take this repo as reference point to start static bloging


**Requirements**

Install below python modules

```
sudo apt-get install python-pip python-dev
sudo pip install -U pelican fabric ghp-import s3cmd pysvg Pygments requests webassets pillow jsmin cssmin BeautifulSoup4 
```

**To build**

Clone the blog

```
git clone https://github.com/arulrajnet/attila-demo
cd attila-demo
git submodule update --init --recursive
git fetch --recurse-submodules
git pull --recurse-submodules
```

fabric commands

```
fab help
fab build
fab serve
```

To build with specific theme

```
pelican -s pelicanconf.py -t my-pelican-themes/attila/
```


Then visit http://localhost:8000

**To publish**

```
fab gh_pages
```
