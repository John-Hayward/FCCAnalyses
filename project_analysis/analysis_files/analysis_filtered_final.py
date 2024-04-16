#Input directory where the files produced at the stage1 level are
#inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/spring2021/output_stage1/"
#inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/pre_winter2023_tests_v2/output_stage1/"
#inputDir = "/eos/user/j/jalimena/FCCeeLLP/"
inputDir = "backgroundFilterTest/new_card/output_stage1"


#Output directory where the files produced at the final-selection level are
#outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/spring2021/output_finalSel/"
#outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/pre_winter2023_tests_v2/output_finalSel/"
outputDir  = "backgroundFilterTest/stack_test/output_finalSel"

#Integrated luminosity for scaling number of events (required only if setting doScale to true)
intLumi = 150e+6 #pb^-1

#Scale event yields by intLumi and cross section (optional)
doScale = True

#Save event yields in a table (optional)
saveTabular = True

processList = {
    #run over the full statistics from stage1

    #backgrounds
    #'p8_ee_Zee_ecm91':{},
    #'p8_ee_Ztautau_ecm91':{},
    #'p8_ee_Zbb_ecm91':{},
    #'p8_ee_Zcc_ecm91':{},
    #'p8_ee_Zud_ecm91':{},
    #'p8_ee_Zss_ecm91':{},
    #'p8_ee_Zmumu_ecm91':{},
    #'p8_ee_Zuds_ecm91':{},

    #signals
    #'HNL_Majorana_eenu_10GeV_2e-4Ve':{},
    #'HNL_Majorana_eenu_20GeV_9e-5Ve':{},
    #'HNL_Majorana_eenu_20GeV_3e-5Ve':{},
    #'HNL_Majorana_eenu_30GeV_1e-5Ve':{},
    #'HNL_Majorana_eenu_50GeV_6e-6Ve':{},

    #'spring21_eenu_30GeV_1p41e-6Ve':{},    
    #'spring21_eenu_50GeV_1p41e-6Ve':{},
    #'spring21_eenu_70GeV_1p41e-6Ve':{},
    #'spring21_eenu_90GeV_1p41e-6Ve':{},

    #'filteredevents_Zbb_lifetimecut3em11':{},

    #'1000_Zbb_lifetime_3e-11':{},
    #'5e4_Zbb_lifetimecut':{},
    #'filteredevents_Zbb_lifetimecut_3em11':{},
    #'Zbb_inclusive_test':{},
    #'no_filter_test':{},
    #'inclusive_scaled':{},
    #'main_branch_pythia_card':{},
    #'old_key4hep_stack_Zbb':{},
    #'winter23_delphes_Zbb_test':{},
    "Delphes_test":{},
}



###Dictionary for prettier names of processes (optional)
processLabels = {
    #backgrounds
    #'p8_ee_Zee_ecm91':"Z to ee",
    #'p8_ee_Ztautau_ecm91':"Z to tau tau",
    'p8_ee_Zbb_ecm91':"Z to bb",
    #'p8_ee_Zcc_ecm91':"Z to cc",
    #'p8_ee_Zud_ecm91':"Z to ud",
    #'p8_ee_Zss_ecm91':"Z to ss",
    #'p8_ee_Zmumu_ecm91':"Z to mu mu",
    ##'p8_ee_Zuds_ecm91':"Z to uds",

    ##signals
    #'HNL_Majorana_eenu_10GeV_2e-4Ve': "$m_N =$ 10 GeV, $|V_{eN}| =  2 * 10^{-4}$",
    #'HNL_Majorana_eenu_20GeV_9e-5Ve': "$m_N =$ 20 GeV, $|V_{eN}| =  9 * 10^{-5}$",
    #'HNL_Majorana_eenu_20GeV_3e-5Ve': "$m_N =$ 20 GeV, $|V_{eN}| =  3 * 10^{-5}$",
    #'HNL_Majorana_eenu_30GeV_1e-5Ve': "$m_N =$ 30 GeV, $|V_{eN}| =  1 * 10^{-5}$",
    #'HNL_Majorana_eenu_50GeV_6e-6Ve': "$m_N =$ 50 GeV, $|V_{eN}| =  6 * 10^{-6}$",

    #'filteredevents_Zbb_lifetimecut3em11': "Z to bb lifetime cut of 3e-11"
    #'1000_Zbb_lifetime_3e-11': "Z to bb lifetime cut of 3e-11",
    #'5e4_Zbb_lifetimecut': "Z to bb lifetime cut of 3e-11",
    #'filteredevents_Zbb_lifetimecut_3em11': "Z to bb lifetime cut of 3e-11",
    #'Zbb_inclusive_test': "Z to bb no cut",
    'no_filter_test': "Inclusive in chunks of 1000 events",
    #'inclusive_scaled': "Winter23 inclusive scaled by 10",
    #'main_branch_pythia_card': "Using pythia card from main branch",
    'old_key4hep_stack_Zbb': "Using old key4hep stack",
    'winter23_delphes_Zbb_test': "Generated using DelphesPythia_EDM4HEP",
    'Delphes_test': "inclusive k4run with delphes",
}

#Link to the dictonary that contains all the cross section information etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
procDictAdd={
    #"MySample_p8_ee_ZH_ecm240":{"numberOfEvents": 10000000, "sumOfWeights": 10000000, "crossSection": 0.201868, "kfactor": 1.0, "matchingEfficiency": 1.0}
    "HNL_Majorana_eenu_10GeV_2e-4Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 1.688495e-5, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "HNL_Majorana_eenu_20GeV_9e-5Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 3.049068e-6, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "HNL_Majorana_eenu_20GeV_3e-5Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 3.386873e-7, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "HNL_Majorana_eenu_30GeV_1e-5Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 3.340798e-8, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "HNL_Majorana_eenu_50GeV_6e-6Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 8.215645e-9, "kfactor": 1.0, "matchingEfficiency": 1.0},
    #"HNL_Majorana_eenu_10GeV_2e-4Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 6.7e-9, "kfactor": 1.0, "matchingEfficiency": 1.0},
    #"HNL_Majorana_eenu_20GeV_9e-5Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 6.7e-9, "kfactor": 1.0, "matchingEfficiency": 1.0},
    #"HNL_Majorana_eenu_20GeV_3e-5Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 6.7e-9, "kfactor": 1.0, "matchingEfficiency": 1.0},
    #"HNL_Majorana_eenu_30GeV_1e-5Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 6.7e-9, "kfactor": 1.0, "matchingEfficiency": 1.0},
    #"HNL_Majorana_eenu_50GeV_6e-6Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 6.7e-9, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "filteredevents_Zbb_lifetimecut3em11": {"numberOfEvents":50000, "sumofWeights": 50000, "crossSection":6645.46, "kfactor":1.0, "matchingEfficiency":0.14999},
    "1000_Zbb_lifetime_3e-11": {"numberOfEvents":"1000", "sumofWeights":1000, "crossSection":6645.46, "kfactor":1.0, "matchingEfficiency":0.0075802},
    #"5e4_Zbb_lifetimecut": {"numberOfEvents":"50000", "sumofWeights":1000, "crossSection":6645.46, "kfactor":1.0, "matchingEfficiency":0.00762056},
    "5e4_Zbb_lifetimecut": {"numberOfEvents":"6561194", "sumofWeights":50000, "crossSection":6645.46, "kfactor":1.0, "matchingEfficiency":0.00762056},
    'filteredevents_Zbb_lifetimecut_3em11': {"numberOfEvents":"588727114", "sumofWeights":4500000, "crossSection":6645.46, "kfactor":1.0, "matchingEfficiency":0.007643609225716755},
    'Zbb_inclusive_test': {"numberOfEvents":100000, "sumofWeights":100000, "crossSection":6645.46, "kfactor":1.0, "matchingEfficiency":1.0},
    'no_filter_test': {"numberOfEvents":100000, "sumofWeights":100000, "crossSection":6645.46, "kfactor":1.0, "matchingEfficiency":1.0},
    'inclusive_scaled': {"numberOfEvents":100000, "sumofWeights":100000, "crossSection":6645.46, "kfactor":1.0, "matchingEfficiency":1.0},
    'main_branch_pythia_card': {"numberOfEvents":100000, "sumofWeights":100000, "crossSection":6645.46, "kfactor":1.0, "matchingEfficiency":1.0},
    'old_key4hep_stack_Zbb': {"numberOfEvents":100000, "sumofWeights":100000, "crossSection":6645.46, "kfactor":1.0, "matchingEfficiency":1.0},
    'winter23_delphes_Zbb_test': {"numberOfEvents":10000, "sumofWeights":10000, "crossSection":6645.46, "kfactor":1.0, "matchingEfficiency":1.0},
    'Delphes_test': {"numberOfEvents":100000, "sumofWeights":100000, "crossSection":6645.46, "kfactor":1.0, "matchingEfficiency":1.0},
}



#Number of CPUs to use
nCPUS = 4

#produces ROOT TTrees, default is False
doTree = False

##Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    "selNone": "n_AllGenBs > -1",
    "selBs": "n_AllGenBs > 0",
    #"sel2RecoEl": "n_RecoElectrons == 2",
    #"selVetoes": "n_RecoElectrons ==2 && n_RecoMuons == 0 && n_RecoPhotons == 0",
    #"sel0p5disp": "n_RecoElectrons ==2 && n_RecoMuons == 0 && n_RecoPhotons == 0 && RecoElectronTrack_absD0[0] > 0.5 && RecoElectronTrack_absD0[1] > 0.5",
    #"selAtLeastOneBs": "n_AllGenBs > 0",
    #"selLifetimes": "n_AllGenBs > 0 && std::all_of(std::begin(AllGenBs_t), std::end(AllGenBs_t), [](int i) {return i >= 3e-11}I)",

}

###Dictionary for prettier names of cuts (optional)
cutLabels = {
    
    "selNone": "No selection",
    "selBs": "At least one Bs",
    #"sel2RecoEl": "Exactly 2 final state reconstructed electrons",
    #"selVetoes": "No final state reconstructed muons or photons",
    #"sel0p5disp": "Both electrons vertex displacement >0.5mm"
    
}

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {
    "n_AllGenBs": {"name":"n_AllGenBs", "title": "Number of generator level Bs", "bin":6, "xmin":0, "xmax":6},
    "AllGenBs_t": {"name":"AllGenBs_t", "title": "Lifetime of generator level Bs", "bin":500, "xmin":0, "xmax":5e-11},
    #"n_FSGenElectron": {"name":"n_FSGenElectron", "title": "Number of generator level FS electrons", "bin":10, "xmin":0, "xmax":10},
    #"n_FSGenMuon": {"name":"n_FSGenMuon", "title": "Number of generator level FS muons", "bin":10, "xmin":0, "xmax":10},
    #"n_FSGenPhoton": {"name":"n_FSGenPhoton", "title": "Number of generator level FS photons", "bin":10, "xmin":0, "xmax":10},

    #"n_RecoElectrons": {"name":"n_RecoElectrons", "title": "Number of reco level electrons", "bin":10, "xmin":0, "xmax":10},
    #"n_RecoMuons": {"name":"n_RecoMuons", "title": "Number of reco level muons", "bin":10, "xmin":0, "xmax":10},
    #"n_RecoPhotons": {"name":"n_RecoPhotons", "title": "Number of reco level photons", "bin":10, "xmin":0, "xmax":10},

    #"FSGen_Lxyz": {"name": "FSGen_Lxyz", "title": "Generator electron vertex displacement", "bin":50, "xmin":0, "xmax":10},
    #"RecoElectronTrack_absD0": {"name": "RecoElectronTrack_absD0", "title": "Reconstructed electron vertex displacement", "bin":50, "xmin":0, "xmax":10},


}
