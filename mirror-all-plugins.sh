#!/bin/bash
DOWNLOAD_DIR="mirror"
if [ ! -d $DOWNLOAD_DIR ]
then
  mkdir $DOWNLOAD_DIR
fi
for plugin in `grep '"name"' listing.json|awk -F\" '{print $4}'`
do
  dirname=`echo $plugin|sed 's/.*\///g'`
  if [ ! -d $DOWNLOAD_DIR/$dirname ]
  then
    git -C $DOWNLOAD_DIR clone https://github.com/$plugin
  fi
  pushd $DOWNLOAD_DIR/$dirname
  git submodule update --init --recursive
  popd
done
