#Input directory where the files produced at the stage1 level are
#inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/spring2021/output_stage1/"
#inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/pre_winter2023_tests_v2/output_stage1/"
#inputDir = "/eos/user/j/jalimena/FCCeeLLP/"
#inputDir = "winter2023_fulldataset/output_stage1_2el0mu0photons0jets"
inputDir = "genVsReco/smarter_tests/output_stage1/"


#Output directory where the files produced at the final-selection level are
#outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/spring2021/output_finalSel/"
#outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/pre_winter2023_tests_v2/output_finalSel/"
#outputDir = "winter2023_fulldataset/output_finalSel_2el0mu0photons0jets/"
outputDir = "genVsReco/effectiveness_final/output_finalSel/"

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

    #signals
    #'HNL_Majorana_eenu_30GeV_1p41e-6Ve':{},
    #'HNL_Majorana_eenu_50GeV_1p41e-6Ve':{},
    #'HNL_Majorana_eenu_70GeV_1p41e-6Ve':{},
    #'HNL_Majorana_eenu_90GeV_1p41e-6Ve':{},
}

###Dictionary for prettier names of processes (optional)
processLabels = {
    #backgrounds
    'p8_ee_Zee_ecm91':"Z $\rightarrow$ ee",
    'p8_ee_Ztautau_ecm91':"Z $\rightarrow \tau \tau$",
    'p8_ee_Zbb_ecm91':"Z $\rightarrow$ bb",
    'p8_ee_Zcc_ecm91':"Z $\rightarrow$ cc",
    'p8_ee_Zud_ecm91':"Z $\rightarrow$ ud",
    'p8_ee_Zss_ecm91':"Z $\rightarrow$ ss",
    'p8_ee_Zmumu_ecm91':"Z $\rightarrow \mu \mu$",

    #signals
    #'HNL_Majorana_eenu_30GeV_1p41e-6Ve': "$m_N =$ 30 GeV, $|V_{eN}| =  1.41 * 10^{-6}$",
    #'HNL_Majorana_eenu_50GeV_1p41e-6Ve': "$m_N =$ 50 GeV, $|V_{eN}| =  1.41 * 10^{-6}$",
    #'HNL_Majorana_eenu_70GeV_1p41e-6Ve': "$m_N =$ 70 GeV, $|V_{eN}| =  1.41 * 10^{-6}$",
    #'HNL_Majorana_eenu_90GeV_1p41e-6Ve': "$m_N =$ 90 GeV, $|V_{eN}| =  1.41 * 10^{-6}$",
}

#Link to the dictonary that contains all the cross section information etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
procDictAdd={
    #"MySample_p8_ee_ZH_ecm240":{"numberOfEvents": 10000000, "sumOfWeights": 10000000, "crossSection": 0.201868, "kfactor": 1.0, "matchingEfficiency": 1.0}
    "HNL_Majorana_eenu_30GeV_1p41e-6Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 6.4193e-10, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "HNL_Majorana_eenu_50GeV_1p41e-6Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 4.53738e-10, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "HNL_Majorana_eenu_70GeV_1p41e-6Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 1.96762e-10, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "HNL_Majorana_eenu_90GeV_1p41e-6Ve": {"numberOfEvents": 50000, "sumOfWeights": 50000, "crossSection": 1.74886e-12, "kfactor": 1.0, "matchingEfficiency": 1.0},
}

#Number of CPUs to use
nCPUS = 4

#produces ROOT TTrees, default is False
doTree = False

##Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    "selNone": "n_FSGenElectron > -1",
    "selEle": "n_FSGenElectron == 2",
    "selMu": "n_FSGenMuon == 0",
    "selEleMu": "n_FSGenElectron == 2 && n_FSGenMuon == 0",
    "selEleMuPho": "n_FSGenElectron == 2 && n_FSGenMuon == 0 && n_FSGenPhoton==0",
    #"selRecoEle": "n_RecoElectrons==2",
    #"selRecoGenEle":"n_RecoElectrons==2 && n_FSGenElectron==2",
    #"selRecoMu": "n_RecoMuons==0",
    #"selRecoGenMu": "n_RecoMuons==0 && n_FSGenMuon==0",
    #"selRecoPhot": "n_RecoPhotons==0",
    #"selRecoGenPhot": "n_RecoPhotons==0 && n_FSGenPhoton==0",
    #"selRecoMom": "RecoMissingEnergy_p[0]>20",
    #"selRecoGenMom": "RecoMissingEnergy_p[0]>20 && FSGenNeutrino_totalP>10",
    
    # "sel1FSGenEle": "n_FSGenElectron>0",
    # "sel1FSGenEle_eeInvMassGt80": "n_FSGenElectron>0 && FSGen_ee_invMass >80",
    # "sel1FSGenNu": "n_FSGenNeutrino>0",
    #"sel2RecoEle": "n_RecoElectrons==2",
    #"sel2RecoEle_vetoes": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_RecoJets==0 && n_RecoPhotons==0",
    ## "sel2RecoEle_absD0Gt0p1": "n_RecoElectrons==2 && RecoElectronTrack_absD0[0]>0.1 && RecoElectronTrack_absD0[1]>0.1", #both electrons displaced
    ## "sel2RecoEle_chi2Gt0p1": "n_RecoElectrons==2 && RecoDecayVertex.chi2>0.1", #good vertex
    ## "sel2RecoEle_chi2Gt0p1_LxyzGt1": "n_RecoElectrons==2 && RecoDecayVertex.chi2>0.1 && Reco_Lxyz>1", #displaced vertex
    #"sel2RecoEle_vetoes_MissingEnergyGt10": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_RecoJets==0 && n_RecoPhotons==0 && RecoMissingEnergy_p[0]>10", #missing energy > 10 GeV
    ## "sel2RecoEle_vetoes_absD0Gt0p5": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_RecoJets==0 && n_RecoPhotons==0 && RecoElectronTrack_absD0[0]>0.5 && RecoElectronTrack_absD0[1]>0.5", #both electrons displaced
    #"sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt0p5": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_RecoJets==0 && n_RecoPhotons==0 && RecoMissingEnergy_p[0]>10 && RecoElectronTrack_absD0[0]>0.5 && RecoElectronTrack_absD0[1]>0.5", #both electrons displaced
    # "sel2RecoEle_vetoes_MissingEnergyGt10_chi2Gt1_LxyzGt5": "n_RecoElectrons==2 && n_RecoMuons==0 && n_RecoPhotons==0 && n_RecoJets==0 && n_RecoPhotons==0 && RecoMissingEnergy_p[0]>10 && RecoDecayVertex.chi2>1 && Reco_Lxyz>5", #displaced vertex
}

###Dictionary for prettier names of cuts (optional)
cutLabels = {
    "selNone": "Before selection",
    "selEle": "just el",
    "selMu": "just mu",
    "selEleMu": "el and mu",
    "selEleMuPho": "all 3"
    #"selRecoEle": "Elec Reco",
    #"selRecoGenEle":"Elec Gen and Reco",
    #"selRecoMu": "Mu Reco",
    #"selRecoGenMu": "Mu Gen and Reco",
    #"selRecoPhot": "Phot Reco",
    #"selRecoGenPhot": "Phot Gen and Reco",
    #"selRecoMom": "Mom Reco",
    #"selRecoGenMom": "Mom Gen and Reco",
    #"sel2RecoEle": "Exactly 2 electrons",
    #"sel2RecoEle_vetoes": "Veto photons, muons, and jets",
    #"sel2RecoEle_vetoes_MissingEnergyGt10": "$\\not\\! p >$ 10 GeV",
    #"sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt0p5": "Electron $|d_0| >$ 0.5 mm",
}

###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    #gen variables
    "n_FSGenElectron":                   {"name":"n_FSGenElectron",                  "title":"Number of final state gen electrons",        "bin":5,"xmin":0 ,"xmax":5},
    "n_FSGenMuon":                   {"name":"n_FSGenMuon",                  "title":"Number of final state gen muons",        "bin":5,"xmin":0 ,"xmax":5},
    "n_FSGenPhoton":                   {"name":"n_FSGenPhoton",                  "title":"Number of final state gen photons",        "bin":5,"xmin":0 ,"xmax":5},

    "n_RecoElectrons": {"name":"n_RecoElectrons", "title":"Number of reconstructed electrons", "bin":5, "xmin":0, "xmax":5},
    "n_RecoMuons": {"name":"n_RecoMuons", "title":"Number of reconstructed muons", "bin":5, "xmin":0, "xmax":5},
    "n_RecoPhotons": {"name":"n_RecoPhotons", "title":"Number of reconstructed photons", "bin":5, "xmin":0, "xmax":5},

    "n_electron_dif": {"name":"n_electron_dif", "title":"Difference in number of reco and gen electrons", "bin":20, "xmin":-5, "xmax":5},
    "n_muon_dif": {"name":"n_muon_dif", "title":"Difference in number of reco and gen muons", "bin":20, "xmin":-5, "xmax":5},
    "n_photon_dif": {"name":"n_photon_dif", "title":"Difference in number of reco and gen photons", "bin":20, "xmin":-5, "xmax":5},
    #"missing_p_dif": {"name":"missing_p_dif", "title":"Missing reco momentum - sum FS gen neutrino momenta", "bin":100, "xmin":-25, "xmax":25},
    "RecoMissingEnergy_p": {"name":"RecoMissingEnergy_p", "title":"Reconstructed missing momentum", "bin": 200, "xmin":0, "xmax":100},
    "FSGenNeutrino_totalP": {"name":"FSGenNeutrino_totalP", "title":"Total momentum of FS gen neutrinos", "bin": 200, "xmin":0, "xmax":100},
    
    
}
