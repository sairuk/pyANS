# pyANS
*An ANSI art renderer*

Script will choose art at random from available art packs. Rendering time is based on a faux baud rate delay.

Settings can be tweaked in the script

    #### Base Settings
    baud = 57600        # emulated baud rate
    bits = 10	    # bits per char
    cols = 80           # terminal cols
    cp = 'cp437'        # code page
    ansi_delay = 3      # set the delay between ansi loading
    ansi_store = os.path.join(os.path.dirname(os.path.realpath(__file__)),'libraries')  # ANSi path

File types used can be tweaked in the script

    #### Whitelists
    arclist = ['.zip','.ZIP']
    anslist = ['.ans','.ANS','.asc','.ASC','.ice','.ICE']

----
## usage
1. Clone
2. Drop artpacks archives into the libraries folder

----

    sairuk : //mameau.com