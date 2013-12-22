# pyscope

A modern software oscilloscope. Plug in leaders to an audio patch cable and watch your circuits live!

[xoscope](http://xoscope.sourceforge.net/) hasn't had a release since 2009,
so this is a remimplentation of it: shorter, in python, and more flexible. That's the end-goal, at least. It will probably languish as a hobby project, but pull requests are welcome!

Built on [SciPy](http://scipy.org) and [PySoundCard](https://github.com/bastibe/PySoundCard/) :)

## Installation

First, clone this repo.

If you can the dependencies installed on your system, pyscope should run on Windows, Linux, and OS X.

Pyscope is a py3k application, so you need to get SciPy, matplotlib, and PySoundCard installed in their python3 forms.
SciPy/matplotlib are almost certainly available in your distribution's package manager or are available from http://scipy.org, but
PySoundCard might not be. However, it is on pipi and you can install it with "sudo pip install PySoundCard".

## Running

In the directory you have the repo cloned, just run 'pyscope'. You should see something like
![pyscope init](TODO).
Hum at it and you should see something like
![pyscope active](TODO)
If you see the scope but do not get a response, check your volume settings.

To use pyscope to test electronics, you will need to build an 1/8th" TRS probe pair, using, for example,
[these instructions](http://www.yann.com/en/diy-turn-your-gnulinux-computer-into-a-free-oscilloscope-29/09/2010.html).
Be careful though! Running experimental circuitry direct into your computer might not be advised.
Find someone with the skills to make you a voltage limiter.

Does not yet support the ability to choose which soundcard to listen on, but that is in the works.


