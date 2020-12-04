#!/usr/bin/env python3
# coding: utf-8

import pdfplumber
import sys

if len(sys.argv) != 2:
    print("./utils-thesorus-extractor thesorus.pdf")
    exit(1)

with pdfplumber.open(sys.argv[1]) as pdf:
    page = pdf.pages[2:]
    t = ""
    for p in page:
        t += p.extract_text()

t = list(filter(lambda x: not x.isdigit() and not "/256" in x and x != "ANSM - Octobre 2020" and x != "www.ansm.sante.fr", t.split("\n")))

csv = []
l = 0
for x in t:
    if x[0] == "+":
        csv.append([c, x[2:], ""])
        l = 0
    elif x.isupper():
        c = x
        l = 1
    elif l == 0 and len(x.strip()):
        csv[-1][2] += x + " "

print("SUBSTANCE;SUBSTANCE2;CONFLICT_DESC")
for l in csv:
    print(f"{l[0]};{l[1]};{l[2]}")
