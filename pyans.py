#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# // PyANS a simple ANSI scroller
# Basic ANSI/ASCII scroller written in native python 
# -: @sairukau :-
#
# ISSUES:
#  Colours aren't quite right
#  Doesn't support all ansi correctly
#
# CHANGELOG:
#  v03: reads both zip and ans/asc etc from the libraries directory
#       changed rendering method but still term width dependant
#  v02: read randomly from artpacks, error checking, whitelists added
#  v01: initial version, support .ans only
#
import os, sys, zipfile
from time import sleep
from random import randint

#### Base Settings
baud = 57600        # emulated baud rate
bits = 10           # bits per char
cols = 80           # terminal cols
cp = 'cp437'        # code page
reset = '\033c'     # reset code for terminal
ansi_delay = 3      # set the delay between ansi loading
ansi_store = os.path.join(os.path.dirname(os.path.realpath(__file__)),'libraries')  # ANSi path

#### Whitelists
arclist = ['.zip','.ZIP']
anslist = ['.ans','.ANS','.asc','.ASC','.ice','.ICE']

debug = False

def writeout(c):
    sys.stdout.write(c)
    sys.stdout.flush()
    return

def main():
    #### Simulated baud delay (very basic)
    baud_delay = ( cols**2 / ( baud / bits ) ) / 6000.0

    #### Build List of available zips
    packlist = []
    for root, dirs, files in os.walk(ansi_store):
        for names in files:
            if os.path.splitext(names)[1] in arclist + anslist:
                packlist.append(os.path.join(root,names))

    while True and packlist:
        viewlist = []
        #### Select Random Pack
        pack = packlist[randint(0, len(packlist)-1)]

        ### Process Archive into filelist
        if os.path.splitext(pack)[1] in arclist:
            #### Read Archive
            try: 
                archive = zipfile.ZipFile(pack, 'r')
            except:
                archive = None
                if debug:
                    print "Couldn't read: %s" % pack
            if archive:
                for ans in archive.namelist():
                    if os.path.splitext(ans)[1] in anslist:
                        viewlist.append(archive.read(ans))


        #### Process ANSI into viewlist
        else:
            for ans in [pack]:
                viewlist.append(open(ans,'r').read())
            

        #### Select Random ANSI
        if len(viewlist) > 0:
            ansi = viewlist[randint(0, len(viewlist)-1)]
        else:
            if debug:
                print "No compatible files found in %s" % pack
            ansi = False

        #### Process ANSI
        writeout(reset) ## reset the screen
        for idx, char in enumerate(ansi):
            writeout(char.decode(cp))
            sleep(baud_delay)
            
        if debug:
            sleep(ansi_delay)
            writeout(reset)
            print "Displayed %s from %s" % (ansi, pack)
        sleep(ansi_delay) ## delay loading the next ansi
    else:
        sleep(0.2)

if __name__ == "__main__":
    if sys.version_info<(2,7,0):
        sys.stderr.write("Python 2.7 is required")
        exit(1)
    else:
        main()
