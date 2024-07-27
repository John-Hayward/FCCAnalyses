# Applying Filters at Generator Level.

This code shows the basic method I used for generating MC Level filtered events (as of ~March 2024 so may be outdated). Both the exact configurables used are included, as well as simple python scripts to generate files to be run in batch for larger samples. `make_sh_files.py` produces 100 shell scripts to generate filtered samples defined by a `pythiaEventsFiltered.py` file. These are then saved, along with the last 100 lines of standard output to get the filter efficiency, to a defined location on eos. `make_job_sub/py` produces a single .job file toexecute these 100 shell scripts using the batch computing service.


