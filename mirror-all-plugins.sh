#!/bin/bash
DOWNLOAD_DIR="mirror"
if [ ! -d $DOWNLOAD_DIR ]
then
  mkdir $DOWNLOAD_DIR
fi
for plugin in `grep '"name"' listing.json|awk -F\" '{print $4}'`
do
  git -C $DOWNLOAD_DIR clone https://github.com/$plugin
  pushd $DOWNLOAD_DIR
  git submodule update --init --recursive
  popd
done
