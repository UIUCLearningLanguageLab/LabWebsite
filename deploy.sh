#!/usr/bin/env bash

if [[ "$1" != "" ]]; then
    echo "Commit message has been supplied"
else
    echo "Must supply commit message"
    exit
fi

hugo
cd ../lab_website_static
git commit -a -m "$1"
for i in 1 2 3 4 5; do "git push godaddy master" && break || sleep 1; done