linkodeit
=========

... lets you send your code to http://linkode.org web service


```
$ linkodeit -h
usage: linkodeit [-h] [-p PARENT | -g GET] [-i INPUT] [-t TYPE] [-o]
                 [-r REVISION] [-v] [--version]

Paste a text on linkode.org

optional arguments:
  -h, --help            show this help message and exit
  -p PARENT, --parent PARENT
                        linkode id of its parent
  -g GET, --get GET     linkode id to get is parent to this new one
  -i INPUT, --input INPUT
                        text file to be pasted on linkode.org
  -t TYPE, --type TYPE  the type of the content (plain text, Python, diff, C,
                        etc.)
  -o, --open            open the default browser with the link
  -r REVISION, --revision REVISION
                        the revision number of the node that is parent to this
                        new one
  -v, --verbose         show all the debug information
  --version             show the version and exit
```

Installation
------------

```
$ sudo pip3 install linkodeit
```

Usage
-----

```
$ echo "Hello world" | linkodeit
http://linkode.org/mqNUYxvinPK9dfHeYa0zF2
```
