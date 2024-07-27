with open("sub_100_chunks.job", "w+") as f:
    f.write("executable = $(filename) \n")
    f.write("Log = /afs/cern.ch/user/j/jhayward/k4Batch/logs/$(ProcId).log \n")
    f.write("Error = /afs/cern.ch/user/j/jhayward/k4Batch/errors/$(ProcId).error \n")
    f.write("Output = /afs/cern.ch/user/j/jhayward/k4Batch/out/$(ProcId).out \n")
    f.write('requirements     = ( (OpSysAndVer =?= "AlmaLinux9") && (Machine =!= LastRemoteHost) && (TARGET.has_avx2 =?= True) ) \n')
    f.write("on_exit_remove   = (ExitBySignal == False) && (ExitCode == 0) \n")
    f.write("max_retries      = 3 \n")
    f.write("RequestCpus      = 8 \n")
    f.write('+JobFlavour = "tomorrow" \n')
    f.write("queue filename matching files ")
    for i in range(0,101):
        f.write(f"/afs/cern.ch/user/j/jhayward/k4Batch/executables/chunk_{i}.sh ")
