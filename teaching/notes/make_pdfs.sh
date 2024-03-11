#!/bin/bash

jupyter nbconvert --execute --to html --output temp.html benchmarking.ipynb
wkhtmltopdf temp.html benchmarking.pdf

jupyter nbconvert --execute --to html --output temp.html computing_pi.ipynb
wkhtmltopdf temp.html computing_pi.pdf

rm -rf temp.html