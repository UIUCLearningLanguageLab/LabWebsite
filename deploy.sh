#!/usr/bin/env bash

if [[ "$1" != "" ]]; then
    echo "Positional parameter 1 contains something"
else
    exit
fi

hugo
cd ../lab_website_static
git commit -a -m "$1"
git push godaddy master