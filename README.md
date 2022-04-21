# pyANS /pan(t)s/
*An ANSI/ASCII art renderer*

This is a basic ANSI/ASCII art renderer with a simulated baud rate delay.

Script will choose art at random from available art packs or extract art files. Rendering time is based on a faux baud rate delay.

config.example is kept in github with default settings, on first run this is copied to .pyANS in the users home directory.

Edit your settings in the config file

    [path]
    ansi_store = ./libraries
    
    [base]
    baud = 57600
    bits = 10
    cols = 80
    cp = cp437
    ansi_delay = 3
    
    
    [whitelists]
    arclist = zip
    anslist = ans,asc,ice
    
    [misc]
    debug = False

----
## Options
| Option        | Desc          |
| ------------- |:--------------|
| **ansi_store** | path where the artpacks/artfiles are stored |
| **baud/bits/cols** | used to calculate the fake rate delay |
| **cp** | the code page used to render the artfile |
| **ansi_delay** | the delay between each artfile |
| **arclist** | comma separated whitelist of zipfile library compatible archive extensions to process |
| **anslist** | comma separated whitelist of artfile extensions to process |

----
## usage
1. clone
2. copy config.example to ~/.pyANS
3. copy artpacks archives into the libraries folder
4. run python pyANS.py

----

<a href="https://www.youtube.com/watch?v=eWz5cLIOal4" target="_blank"><img src="https://i.ytimg.com/vi/eWz5cLIOal4/hqdefault.jpg" 
alt="pyANS Demo on CentOS" width="240" height="180" border="10" /></a>


    sairuk : //mameau.com : @sairukau
