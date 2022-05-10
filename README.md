# pyANS
*An ANSI/ASCII art renderer*

This is a basic ANSI/ASCII art renderer with a simulated baud rate delay.

Script will choose art at random from available art packs. Rendering time is based on a faux baud rate delay.

config.example is kept in github with default settings, on first run this is copied to the .pyANS directory in the users home directory.

Edit your settings in the config file located at `$HOME/.pyANS/config.ini`

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
## Requirements
* A valid config file
* zlib, lzma support on the host system depending on the archives
on debian based systems this is probably
`# apt-get install zlib1g and liblzma5`

## Limitations
Only zip archives are supported and are subject to the limitations of the core zipfile python library

The python zipfile library does not support `Imploding/Shrinking` compression type, these were the first round of implentations in PKzip shortly after the Arcwars. This artifically limits what is available to pyANS. The good news however is the problematic archives are only a small subset of pack releases.

sixteencolors-archive stats (2202-04)
```
      1 
   3454 deflate
     49 Imploding
      3 Shrinking
    967 store
```

pyANS should skip problematic packs when detected, see pack_info folder for a full list of packs with unsupported compression methods

You can however repack these with the `deflate` or `store` method for use with pyANS

You may attempt to use `pack_info/convert_pack.sh` (AT YOUR OWN RISK) but please make sure you have appropriate backups, it will unpack and repack the files to FNAME_PYA.zip in the libraries directory, these zips will use `store` compression.

```
./convert_pack.sh 
pyans pack convertor v0.01-alpha - sairuk

Looking for unsupported files in ../libraries
Found 2 files for processing
Processing ../libraries/acdu0792.zip
Repacking ../libraries/acdu0792.zip as ../libraries/acdu0792_PYA.zip
OK, backing up ../libraries/acdu0792.zip to ../libraries_unsupported/
Processing ../libraries/acdu1092.zip
Repacking ../libraries/acdu1092.zip as ../libraries/acdu1092_PYA.zip
OK, backing up ../libraries/acdu1092.zip to ../libraries_unsupported/
```

Please never upload converted packs to any official archives, original releases/metadata is important for preservation. These are intended for personal use only with pyANS

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
2. copy config.example to ~/.pyANS/config.ini
3. copy artpacks archives into the libraries folder
4. run python pyans.py

----
## regenerate the cache
1. run python pyans.py --update-cache

----

## differences in the rewrite
* python3 only
* uses a cachefile (better rand)
* only supports zipped art packs
* logging added
* code split up into classes



<a href="https://www.youtube.com/watch?v=eWz5cLIOal4" target="_blank"><img src="https://i.ytimg.com/vi/eWz5cLIOal4/hqdefault.jpg" 
alt="pyANS Demo on CentOS" width="240" height="180" border="10" /></a>


    sairuk : //mameau.com : @sairukau



## Notes
* https://xn--rpa.cc/irl/term.html
* https://en.wikipedia.org/wiki/ANSI_escape_code
* http://nethack4.org/blog/portable-terminal-codes.html
