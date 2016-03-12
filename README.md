# pyANS /pan(t)s/
*An ANSI/ASCII art renderer*

This is a very basic ANSI/ASCII art renderer with a simulated baud rate delay.

Script will choose art at random from available art packs or extract art files. Rendering time is based on a faux baud rate delay.

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
## usage
1. clone
2. copy config.example to config
3. crop artpacks archives into the libraries folder
4. run python pyANS.py

----

    sairuk : //mameau.com
