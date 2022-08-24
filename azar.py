#!/usr/bin/python3
# coding: utf8
from random import randint

azar = randint(100, 254)

green = "\033[1;32m"
red = "\033[1;31m"
blue = "\033[1;34m"
end = "\033[00m"

print(f"{red}------------------------------{end}")
print(f"{blue}   Numero Random{end}: {green}{azar}{end}")
print(f"{red}------------------------------{end}")
