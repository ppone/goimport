goimport
========

Install local Go packages.

Requirements: Go binary needs to be in your $PATH, and $GOPATH needs to be setup.
Python 3.3 needs to be installed.   You can modify goimport.py for Python3.3+ versions. 

To install goimport so you can use it anywhere
```
chmod +x goimport.py
cp goimport.py /usr/local/bin/goimport
```

cd into a Go package directory that you want to install.

```
cd ~/Desktop/oauth1
goimport
```
That is it.


