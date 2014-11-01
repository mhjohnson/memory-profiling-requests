memory-profiling-requests
=========================

Just an attempted proof of concept that there could be a memory leak in python-requests


Setup
=====
$ virtualenv venv
$ source bin/venv/activate
$ pip install -r requirements.txt
$ pip install matplotlib # just in case you need it


Run
===

Step 1.  Run the script

$ mprof run python example.py

Step 2. Check the results with the memory profiler

$ mprof plot mprofile_*.dat


