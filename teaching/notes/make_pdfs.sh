#!/bin/bash

# jupyter nbconvert --execute --to html --output temp.html benchmarking.ipynb
# wkhtmltopdf temp.html benchmarking.pdf

jupyter nbconvert --execute --to html --output temp.html computing_pi.ipynb
wkhtmltopdf temp.html computing_pi.pdf

jupyter nbconvert --execute --to html --output temp.html threads_and_processes.ipynb
wkhtmltopdf temp.html threads_and_processes.pdf

rm -rf temp.html