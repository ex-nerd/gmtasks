.. gmtasks documentation master file, created by
   sphinx-quickstart on Thu Jan 19 15:53:57 2012.

Welcome to gmtasks's documentation!
===================================

``gmtasks`` contains a simple multiprocessing server for Gearman workers,
designed for ease of configuration and maximum availability.  It includes a
task wrapper class that traps any interrupts or exceptions that might be thrown
by your task methods, and attempts to make sure that the affected job is
re-inserted into the queue (which is not the default behavior if the worker
script exits abnormally)

Contents:

.. toctree::
   :maxdepth: 2

   gmtasks
   jsonclass
   example


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Download
========

* https://github.com/ex-nerd/gmtasks
* http://pypi.python.org/pypi/gmtasks/
