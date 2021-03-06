![](https://raw.githubusercontent.com/alecnunn/Ioun/master/resources/ioun.png)

Ioun is a simple to use wiki software written in Python and powered by [Bottle.py](http://www.bottlepy.org/) and 
[PureCSS](http://www.purecss.io/) and several other Python libraries.  For their license information, check the `licenses` folder

Ioun is small enough that it is self contained.  You can run your own instance by simply running the redistributable executable.  The reason I wanted it to be self contained, (including CSS, HTML, etc) is that I wanted to be able to use this offline or on segregated networks that do not have Internet access.  If you're willing to load the CSS from the Internet, I'm sure you could cut down the "compiled" size by even more.

This project is also not intended to be taken 100% seriously (not yet at least).  For the most part, I am using it as a learning experience.

# How To Use
- First download or clone the latest source
  - ```git clone https://github.com/alecnunn/Ioun.git```
- Run the build script
  - ```./build```
- Initialize the database
  - ```./ioun --init```
- Run the server
  - ```./ioun```

# License

Ioun is released under the LGPL v3 license with a modification (listed below).

If Ioun is used in a private network that is not accessible through public networks and modifications have been made to
the source, you do not have to disclose your modifications.
