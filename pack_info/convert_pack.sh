#!/bin/bash
#
# Convert old zipfile formats to something pyANS can read
# - sairuk
#
# ++++++++
# CAUTION: Use at your own risk, ensure backups are taken
# ++++++++                                                      
#
#
#set -x

VERSION="v0.01-alpha"
PYA_LIB=$(dirname $(basename $0)/)$(awk '/ansi_store/{print $3}' $HOME/.pyANS)
PYA_LIBU="${PYA_LIB}_unsupported"

echo -e "pyans pack convertor $VERSION - sairuk\n"

[ ! -d "$PYA_LIBU" ] && mkdir "$PYA_LIBU"
if [ -d "$PYA_LIB" ]
then
  echo "Looking for unsupported files in $PYA_LIB"
  UNSUPPORTED=($(find "$PYA_LIB/" -iname "*.zip" -exec file {} \; | awk '!/(deflate|store)/{print $1}' | sed 's/[: ]//'))
  [ ${#UNSUPPORTED[@]} -eq 0 ] && echo "No unsupported files found" && exit 1

  echo "Found ${#UNSUPPORTED[@]} files for processing"
  for UNFILE in ${UNSUPPORTED[@]}
  do
    PYA_CONV="${PYA_LIB}/$(basename ${UNFILE} .zip)_PYA.zip"
    echo "Processing $UNFILE"

    if [ ! -f "$PYA_CONV" ] 
    then
      PYA_TMP=$(mktemp -d)
      echo "Repacking $UNFILE as $PYA_CONV"
      unzip "$UNFILE" -d $PYA_TMP &>/dev/null
      zip -m "$PYA_CONV" -r $PYA_TMP &>/dev/null

      if [ $(file "$PYA_CONV" | awk -F '=' '{print $2}' | grep -E "(deflate|store)") ]
      then
        echo "OK, backing up $UNFILE to $PYA_LIBU/"
        mv "$UNFILE" "$PYA_LIBU"
      fi
    else
      echo "File is already converted as $PYA_CONV"
    fi
  done
fi
