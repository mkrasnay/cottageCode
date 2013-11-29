This repository contains three files:
fullauto2.py
parsecal.py
cottageRelay2.ino

These files are all of the custom code required to run the cottage automation solution.  See mikekrasnay.blogspot.ca for full context, parts list, pictures, and other implementation details.

fullauto2.py is the core logic that runs on a Raspberry Pi running a Raspian distro.

parsecal.py is a piece of code that parses out event data from an ical file.  This code seems to break when executed within fullauto2.py, and the python ical library that it uses does not appear to be documented.

cottageRelay2.ino is an Arduino sketch that listens for characters coming from the RPi over USB, and sends HIGH or LOW to the appropriate pins, causing the relays on the attached Relay Shield to open or close.

You can email me at mike@krasnay.ca, or comment at mikekrasnay@blogspot.ca.