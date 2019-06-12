#!/usr/bin/env bash
rm function.zip
cd package
zip -r9 ../function.zip .
cd ..
zip -g function.zip *py
