#!/bin/sh

VERSION=$1

# git clone ssh://git.fedorahosted.org/git/python-dmidecode.git
# cd python-dmidecode
git archive --format=tar --prefix=python-dmidecode-$VERSION/ -o python-dmidecode-$VERSION.tar v$VERSION 
tar -xvf python-dmidecode-$VERSION.tar
rm -r python-dmidecode-$VERSION/debian
tar -cJvf python-dmidecode-$VERSION.tar.xz python-dmidecode-$VERSION
