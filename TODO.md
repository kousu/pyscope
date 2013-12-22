# TODO

Remember that a TODO doc is a living document:
this is not a _spec_; you should edit this freely as ideas come up
and let it help you shape your ideas.

* [ ] Configurable scope window (controllable by, say, matplotlib widgets?)
  * blocksize
  * window length (distinct from blocksize--or the option to let window length follow blocksize as blocksize gets read)
  * colour
* [ ] grid lines
* [ ] saving the signal for reference
* [ ] Commandline sound source option
* [ ] Reporting of underruns to the GUI
* [ ] Figure out (and write up) the intricacies of matplotlib interactive vs noninteractive mode:
  * **why is it so hard to just reliably make an empty plot and put data on it? Why does how that works change depending on environment?**
  * see: [[minimal.py]]

* [ ] if I need to use a thread anyway, put the stream reader in a thread so I can control block reads
* [ ] find how to index into generators (see above)
