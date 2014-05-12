# TODO

Remember that a TODO doc is a living document:
this is not a _spec_; you should edit this freely as ideas come up
and let it help you shape your ideas.

* [ ] Configurable scope window (controllable by, say, matplotlib widgets?)
  * blocksize
  * window length (distinct from blocksize--or the option to let window length follow blocksize as blocksize gets read)
  * colour
* [ ] grid lines
* [ ] display min-max and energy values, maybe on a subplot as bargraphs, or an alpha-faded fill behind the scope
* [ ] remember the signal (using my RingBuffer.py?) so that longer windows can be shown but signal can still be updated rapidly
* [ ] Commandline sound source option
* [ ] Reporting of underruns to the GUI
* [ ] Figure out (and write up) the intricacies of matplotlib interactive vs noninteractive mode:
  * **why is it so hard to just reliably make an empty plot and put data on it? Why does how that works change depending on environment?**
  * see: [[minimal.py]]

* [ ] If I must use a thread anyway, put the stream reader in a thread so I can control block reads
  * it seems I am doomed to threads because matplotlib uses Qt which has to have a main thread, and pysoundcard's callback system is, internally, run on a python thread
* [ ] find how to index into generators (see above)
* [ ] implement DFT views
  * it's starting to look like maybe I am cloning Friture?

* [ ] investigate http://bastibe.de/2013-05-30-speeding-up-matplotlib.html
