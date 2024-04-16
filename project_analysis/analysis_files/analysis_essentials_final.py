#Input directory where the files produced at the stage1 level are
#inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/spring2021/output_stage1/"
#inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/pre_winter2023_tests_v2/output_stage1/"
#inputDir = "/eos/user/j/jalimena/FCCeeLLP/"
inputDir = "DVtest/winter23/output_stage1"


#Output directory where the files produced at the final-selection level are
#outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/spring2021/output_finalSel/"
#outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/pre_winter2023_tests_v2/output_finalSel/"
outputDir  = "DVtest/winter23/output_finalSel_afterDisplacement"

#Integrated luminosity for scaling number of events (required only if setting doScale to true)
intLumi = 150e+6 #pb^-1

#Scale event yields by intLumi and cross section (optional)
doScale = True

#Save event yields in a table (optional)
saveTabular = True

processList = {
    #run over the full statistics from stage1

    #backgrounds
    'p8_ee_Zee_ecm91':{},
    'p8_ee_Ztautau_ecm91':{},
    'p8_ee_Zbb_ecm91':{},
    'p8_ee_Zcc_ecm91':{},
    'p8_ee_Zud_ecm91':{},
    'p8_ee_Zss_ecm91':{},
    'p8_ee_Zmumu_ecm91':{},
    #'p8_ee_Zuds_ecm91':{},

    #signals
    'HNL_Majorana_eenu_10GeV_2e-4Ve':{},
    'HNL_Majorana_eenu_20GeV_9e-5Ve':{},
    'HNL_Majorana_eenu_20GeV_3e-5Ve':{},
    'HNL_Majorana_eenu_30GeV_1e-5Ve':{},
    'HNL_Majorana_eenu_50GeV_6e-6Ve':{},

    #'spring21_eenu_30GeV_1p41e-6Ve':{},    
    #'spring21_eenu_50GeV_1p41e-6Ve':{},
    #'spring21_eenu_70GeV_1p41e-6Ve':{},
    #'spring21_eenu_90GeV_1p41e-6Ve':{},
}



###Dictionary for prettier names of processes (optional)
processLabels = {
    #backgrounds
    'p8_ee_Zee_ecm91':"Z to ee",
    'p8_ee_Ztautau_ecm91':"Z to tau tau",
    'p8_ee_Zbb_ecm91':"Z to bb",
    'p8_ee_Zcc_ecm91':"Z to cc",
    'p8_ee_Zud_ecm91':"Z to ud",
    'p8_ee_Zss_ecm91':"Z to ss",
    'p8_ee_Zmumu_ecm91':"Z to mu mu",
    #'p8_ee_Zuds_ecm91':"Z to uds",

    #signals
    'HNL_Majorana_eenu_10GeV_2e-4Ve': "$m_N =$ 10 GeV, $|V_{eN}| =  2 * 10^{-4}$",
    'HNL_Majorana_eenu_20GeV_9e-5Ve': "$m_N =$ 20 GeV, $|V_{eN}| =  9 * 10^{-5}$",
    'HNL_Majorana_eenu_20GeV_3e-5Ve': "$m_N =$ 20 GeV, $|V_{eN}| =  3 * 10^{-5}$",
    'HNL_Majorana_eenu_30GeV_1e-5Ve': "$m_N =$ 30 GeV, $|V_{eN}| =  1 * 10^{-5}$",
    'HNL_Majorana_eenu_50GeV_6e-6Ve': "$m_N =$ 50 GeV, $|V_{eN}| =  6 * 10^{-6}$",
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
}



#Number of CPUs to use
nCPUS = 4

#produces ROOT TTrees, default is False
doTree = False

##Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
        #Cuts 1 - original   
    #"sel2RecoEle_1": "n_RecoElectrons==2",
    #"sel2RecoEle_vetoes_1": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_RecoJets==0",    
    #"sel2RecoEle_vetoes_MissingEnergyGt10_1": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_RecoJets==0 && RecoMissingEnergy_p[0]>10",    
    #"sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt0p5_1": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_RecoJets==0 && RecoMissingEnergy_p[0]>10 && RecoElectronTrack_absD0[0]>0.5 && RecoElectronTrack_absD0[1]>0.5", #both electrons displaced

    #cuts 2 - reclustered jets
    #"sel2RecoEle_2": "n_RecoElectrons==2",
    #"sel2RecoEle_vetoes_2": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0",
    #"sel2RecoEle_vetoes_MissingEnergyGt10_2": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0 &&RecoMissingEnergy_p[0]>10",
    #"sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt0p5_2": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0 && RecoMissingEnergy_p[0]>10 && RecoElectronTrack_absD0[0]>0.5 && RecoElectronTrack_absD0[1]>0.5",

    ##cuts 3 - reclustered jets and missing momentum after reclustering
    #Applying cut for 1 displaced vertex at end
    "sel2RecoEle": "n_RecoElectrons==2",
    "sel2RecoEle_vetoes": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0",
    "sel2RecoEle_vetoes_MissingEnergyGt10": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0 && reclustered_missing_p>10",
    "sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt0p5": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0 && reclustered_missing_p>10 && RecoElectronTrack_absD0[0]>0.5 && RecoElectronTrack_absD0[1]>0.5",
    "sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt2p0": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0 && reclustered_missing_p>10 && RecoElectronTrack_absD0[0]>2.0 && RecoElectronTrack_absD0[1]>2.0",
    "sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt4p0": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0 && reclustered_missing_p>10 && RecoElectronTrack_absD0[0]>4.0 && RecoElectronTrack_absD0[1]>4.0",
    "sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt4p0_1DV": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0 && reclustered_missing_p>10 && RecoElectronTrack_absD0[0]>4.0 && RecoElectronTrack_absD0[1]>4.0 && n_seltracks_DVs==1", 

    #Applying cut for 1 displaced vertex before vetoes
    #"sel2RecoEle": "n_RecoElectrons==2",
    #"sel2RecoEle_1DV": "n_RecoElectrons==2 && n_seltracks_DVs==1",
    #"sel2RecoEle_1DV_vetoes": "n_RecoElectrons==2  && n_seltracks_DVs==1&& n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0",
    #"sel2RecoEle_1DV_vetoes_MissingEnergyGt10": "n_RecoElectrons==2  && n_seltracks_DVs==1&& n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0 && reclustered_missing_p>10",
    #"sel2RecoEle_1DV_vetoes_MissingEnergyGt10_absD0Gt0p5": "n_RecoElectrons==2 && n_seltracks_DVs==1 && n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0 && reclustered_missing_p>10 && RecoElectronTrack_absD0[0]>0.5 && RecoElectronTrack_absD0[1]>0.5",
    #"sel2RecoEle_1DV_vetoes_MissingEnergyGt10_absD0Gt2p0": "n_RecoElectrons==2 && n_seltracks_DVs==1 && n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0 && reclustered_missing_p>10 && RecoElectronTrack_absD0[0]>2.0 && RecoElectronTrack_absD0[1]>2.0",
    #"sel2RecoEle_1DV_vetoes_MissingEnergyGt10_absD0Gt4p0": "n_RecoElectrons==2 && n_seltracks_DVs==1 && n_RecoMuons==0 && n_RecoPhotons==0 && n_antikt_jets==0 && reclustered_missing_p>10 && RecoElectronTrack_absD0[0]>4.0 && RecoElectronTrack_absD0[1]>4.0",

    #cuts to ignore n_jets for investigating missing momentum calc
    #"sel2RecoEle_vetoes": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0",

}

###Dictionary for prettier names of cuts (optional)
cutLabels = {
    #"sel2RecoEle_1": "Exactly 2 electrons v.1",
    #"sel2RecoEle_vetoes_1": "Veto photons, muons, and jets v.1",
    #"sel2RecoEle_vetoes_MissingEnergyGt10_1": "$\\not\\! p >$ 10 GeV v.1",
    #"sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt0p5_1": "Electron $|d_0| >$ 0.5 mm v.1",

    #"sel2RecoEle_2": "Exactly 2 electrons v.2",
    #"sel2RecoEle_vetoes_2": "Veto photons, muons, and jets v.2",
    #"sel2RecoEle_vetoes_MissingEnergyGt10_2": "$\\not\\! p >$ 10 GeV v.2",
    #"sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt0p5_2": "Electron $|d_0| >$ 0.5 mm v.2",

    "sel2RecoEle": "Exactly 2 electrons",
    "sel2RecoEle_vetoes": "Veto photons, muons, and jets",
    "sel2RecoEle_vetoes_MissingEnergyGt10": "$\\not\\! p >$ 10 GeV",
    "sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt0p5": "Electron $|d_0| >$ 0.5 mm",
    "sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt2p0": "Electron $|d_0| >$ 2.0 mm",
    "sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt4p0": "Electron $|d_0| >$ 4.0 mm",
    "sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt4p0_1DV": "Exactly 1 displaced vertex",

    #"sel2RecoEle": "Exactly 2 electrons",
    #"sel2RecoEle_1DV": "Exactly 1 displaced vertex",
    #"sel2RecoEle_1DV_vetoes": "Veto photons, muons, and jets",
    #"sel2RecoEle_1DV_vetoes_MissingEnergyGt10": "$\\not\\! p >$ 10GeV",
    #"sel2RecoEle_1DV_vetoes_MissingEnergyGt10_absD0Gt0p5": "Electrons $|d_0| >$ 0.5 mm",
    #"sel2RecoEle_1DV_vetoes_MissingEnergyGt10_absD0Gt2p0": "Electrons $|d_0| >$ 2.0 mm",
    #"sel2RecoEle_1DV_vetoes_MissingEnergyGt10_absD0Gt4p0": "Electrons $|d_0| >$ 4.0 mm",    

    #"sel2RecoEle_vetoes": "xactly 2 electrons and vetoes muons and photons",
}

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

        "n_RecoElectrons":          {"name":"n_RecoElectrons", "title": "Number reconstructed electrons", "bin":5, "xmin":0, "xmax":5},
        "n_RecoMuons":              {"name":"n_RecoMuons", "title": "Number reconstructed muons", "bin":5, "xmin":0, "xmax":5},
        "n_RecoJets":               {"name":"n_RecoJets", "title": "Number reconstructed jets", "bin":5, "xmin":0, "xmax":5},
        "RecoMissingEnergy_p":      {"name":"RecoMissingEnergy_p", "title": "Reco Total Missing p[GeV]", "bin":100, "xmin":0, "xmax":50},
        #"RecoMissingEnergy_e":      {"name":"RecoMissingEnergy_e", "title": "Reco Total Missing Energy[GeV]", "bin":100, "xmin":0, "xmax":50},
        "RecoElectronTrack_absD0":  {"name":"RecoElectronTrack_absD0",     "title":"Reco electron tracks |d_{0}| [mm]",      "bin":100,"xmin":0, "xmax":10},
        "n_RecoPhotons":            {"name":"n_RecoPhotons", "title": "Number reconstructed photons", "bin":5, "xmin":0, "xmax":5},
        "n_antikt_jets":            {"name":"n_antikt_jets", "title": "Number reconstructed jets after reclustering", "bin":5, "xmin":0, "xmax":5},
        "reclustered_missing_p":    {"name":"reclustered_missing_p", "title": "Total Missing p after reclustering [GeV]", "bin":100, "xmin":0, "xmax":50},
        "n_seltracks_DVs":          {"name":"n_seltracks_DVs", "title": "Number of displaced vertices", "bin": 10, "xmin":0, "xmax":5},  
    

}
