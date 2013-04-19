Quick-Query
===========

A simple OS X service to query Wolfram Alpha. When you right click on some text and hit 'Wolfram Alpha,' the text will be replaced with the output of a Wolfram Alpha query?

![Example](https://raw.github.com/varunrau/Quick-Query/master/wolfram_screencap.png)

Installation
============

This works by creating a OS X service using Automator. To create a service, open Automator and choose service. Change the action to "Run Shell Script" and set "Pass input:" to "as arguments." Then simply copy the following line into the field.

    python /path/to/repo/wolfram.py "$*"

That's all you need for easy Wolfram Alpha queries!

