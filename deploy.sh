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
git push godaddy master