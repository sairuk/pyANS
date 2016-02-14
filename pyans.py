#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# // PyANS a simple ANSI scroller
# Basic ANSI/ASCII scroller written in native python 
# -: @sairukau :-
#
# ISSUES:
#  Colours aren't quite right
#  Doesn't support all ansis correctly
#
# CHANGELOG:
#  v02: read randomly from artpacks, error checking, whitelists added
#  v01: initial version, support .ans only
#
import os, sys, zipfile
from time import sleep
from random import randint

#### Base Settings
baud = 57600        # emulated baud rate
bits = 10	    # bits per char
cols = 80           # terminal cols
cp = 'cp437'        # code page
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
            if os.path.splitext(names)[1] in arclist:
                packlist.append(os.path.join(root,names))

    while True and packlist:
        #### Select Random Pack
        pack = packlist[randint(0, len(packlist)-1)]

        #### Read Archive
        try: 
            archive = zipfile.ZipFile(pack, 'r')
	except:
	    archive = None
	    if debug:
                print "Couldn't read: %s" % pack

	if archive:
            #### Build list of available ANSI's
            viewlist = []
            for ans in archive.namelist():
                if os.path.splitext(ans)[1] in anslist:
                    viewlist.append(ans)

            #### Select Random ANSI
            if len(viewlist) > 0:
                ansi = viewlist[randint(0, len(viewlist)-1)]
            else:
                if debug:
                    print "No compatible files found in %s" % pack
                ansi = False

            #### Process ANSI
            if ansi:
                anslines = None

                try:
                    anslines = archive.read(ansi)
                except NotImplementedError:
                    print "Failed reading %s" % ansi

                if anslines:
		    writeout("\033c") ## reset the screen
                    for line in anslines.split(r"^[[s"):
        	        for char in line:
               	            writeout(char.decode(cp))
                            sleep(baud_delay)
	                print "\n"

                if debug:
                    sleep(ansi_delay)
                    writeout("\033c")
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
