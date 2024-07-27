for i in range(0,101):
    with open(f"./executables/chunk_{i}.sh", 'w+') as f:
        f.write('#!/bin/bash \n \n echo "Hello World" \n')
        #f.write('source /cvmfs/fcc.cern.ch/sw/latest/setup.sh \n')
        f.write('source /cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh \n')
        f.write('mkdir filteredevents_Zbb_lifetimecut_3em11 \n')
        f.write('cd filteredevents_Zbb_lifetimecut_3em11 \n')
        f.write(f"/cvmfs/sw.hsf.org/key4hep/releases/2024-03-10/x86_64-almalinux9-gcc11.3.1-opt/k4fwcore/1.0pre19-zlns7f/bin/k4run /afs/cern.ch/user/j/jhayward/k4Gen/k4Gen/options/pythiaEventsFiltered.py --out.filename chunk_{i}.root &> output.txt \n")
        f.write("tail -100 output.txt &> short_output.txt \n")
        f.write(f"xrdcp chunk_{i}.root root://eosuser.cern.ch//eos/user/j/jhayward/signalGeneration/signals/Delphes_test/chunk_{i}.root \n")
        f.write(f"xrdcp short_output.txt root://eosuser.cern.ch//eos/user/j/jhayward/signalGeneration/signals/Delphes_test/chunk_{i}_log.txt \n")

