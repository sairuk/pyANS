#!/usr/bin/env python3
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
#  v04: added external config file as per issue #7
#       repaired issue #6, arose from last commit
#  v03: reads both zip and ans/asc etc from the libraries directory
#       changed rendering method but still term width dependant
#  v02: read randomly from artpacks, error checking, whitelists added
#  v01: initial version, support .ans only
#
import os, sys, zipfile, shutil
from time import sleep
from random import randint

try:
    import configparser as ConfigParser
except:
    import ConfigParser

# forced options
cfgname = os.path.join(os.path.expanduser('~'),'.pyANS')
cfgexample = 'config.example'
reset = '\033c'

def _log(s):
    print(s)

def commaToList(s):
    """ convert comma seperated whitelists to python lists """
    commaList = []
    for item in s.split(','):
        commaList.append('.%s' % item.lower())
        commaList.append('.%s' % item.upper())
    return commaList

def writeout(c):
    """ write to stdout then flush stdout """
    sys.stdout.write(c)
    sys.stdout.flush()
    return

def main():

    # Check for config file
    if not os.path.exists(cfgname):
        if os.path.exists(cfgexample):
            shutil.copy(cfgexample, cfgname)
        else:
            _log("Config file %s is missing" % cfgname)
            exit()

    # User options        
    config = ConfigParser.RawConfigParser(allow_no_value=False)
    config.read_file(open(cfgname,'r'))

    try:
        baud = config.getint("base", "baud")
        bits = config.getint("base", "bits")
        cols = config.getint("base", "cols")
        cp = config.get("base", "cp")
        ansi_delay = config.getfloat("base", "ansi_delay")
        ansi_store = config.get("path", "ansi_store")
        arclist = commaToList(config.get("whitelists", "arclist"))
        anslist = commaToList(config.get("whitelists", "anslist"))
        debug = config.getboolean("misc", "debug")
    except ConfigParser.NoOptionError or ConfigParser.NoSectionError:
        _log("Config file is damaged or out of date, cannot continue")

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
                    _log("Couldn't read: %s" % pack)
            if archive:
                for ans in archive.namelist():
                    if os.path.splitext(ans)[1] in anslist:
                        viewlist.append([ans, archive.read(ans)])


        #### Process ANSI into viewlist
        else:
            for ans in [pack]:
                viewlist.append([ans, open(ans,'rb').read()])
            

        #### Select Random ANSI
        if len(viewlist) > 0:
            ansi = viewlist[randint(0, len(viewlist)-1)]
        else:
            if debug:
                _log("No compatible files found in %s" % pack)
            ansi = False

        if ansi:
            #### Process ANSI
            writeout(reset) ## reset the screen
            for char in ansi[1].decode(cp):
                writeout(char)
                sleep(baud_delay)


            if debug:
                sleep(ansi_delay)
                writeout(reset)
                _log("\n\nDisplayed %s from %s" % (ansi[0], pack))
            sleep(ansi_delay)
        else:
            sleep(0.2)

if __name__ == "__main__":
    if sys.version_info<(2,7,0):
        sys.stderr.write("Python 2.7 is required")
        exit(1)
    else:
        main()
