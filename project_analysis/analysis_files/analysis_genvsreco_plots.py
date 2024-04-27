import ROOT

# global parameters
intLumi        = 150.0e+06 #in pb-1

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
#scaleSig       = 0.
#scaleBack      = 0.
ana_tex        = 'e^{+}e^{-} #rightarrow N #nu, N #rightarrow ee#nu'
#ana_tex        = ''
delphesVersion = '3.4.2'
#delphesVersion = ''
energy         = 91
collider       = 'FCC-ee'
inputDir       = 'genVsReco/smarter_tests/output_finalSel/'
#inputDir       = 'output_finalSel_Ztautau/'
formats        = ['png']
#formats        = ['pdf']
yaxis          = ['lin','log']
stacksig       = ['nostack']
outdir         = 'genVsReco/smarter_tests/plots/'
#outdir         = 'plots_Ztautau_spring2021_vs_prewinter2023/'
splitLeg       = True

variables = [

    #gen variables
    "n_FSGenElectron",
    "n_FSGenMuon",
    "n_FSGenPhoton",

    "n_RecoElectrons",
    "n_RecoMuons",
    "n_RecoPhotons",

    "n_electron_dif",
    "n_muon_dif",
    "n_photon_dif",
    #"missing_p_dif",
    "RecoMissingEnergy_p",
    "FSGenNeutrino_totalP",

             ]

    
###Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['HNL']  = [
    "selNone",
    "selEleCut",
    "selMuCut",
    "selPhotCut",
    "selMomentumCut",
    # "sel1FSGenEle",
    # "sel1FSGenEle_eeInvMassGt80",
    # "sel1FSGenNu",
    #"sel2RecoEle",
    #"sel2RecoEle_vetoes",
    ## "sel2RecoEle_absD0Gt0p1",
    #"sel2RecoEle_vetoes_MissingEnergyGt10",
    ## "sel2RecoEle_vetoes_absD0Gt0p5",
    #"sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt0p5",
]

extralabel = {}
extralabel['selNone'] = "Before selection"
extralabel['selEleCut'] = "Not 2 final state generator electrons"
extralabel['selMuCut'] = "Not 0 final state generator muons"
extralabel['selPhotCut'] = "Not 0 final state generator photons"
extralabel['selMomentumCut'] = "Total final state generator neutrino momentum < 10GeV"
# extralabel['sel1FSGenEle'] = "At least 1 final state gen electron"
# extralabel['sel1FSGenEle_eeInvMassGt80'] = "At least 1 final state gen electron, gen ee inv mass > 80 GeV"
# extralabel['sel1FSGenNu'] = "At least 1 final state gen neutrino"
extralabel['sel2RecoEle'] = "2 electrons"
extralabel['sel2RecoEle_vetoes'] = "2 electrons; No muons, jets, or photons"
# extralabel['sel2RecoEle_absD0Gt0p1'] = "2 electrons with |d_0|>0.1 mm"
extralabel['sel2RecoEle_vetoes_MissingEnergyGt10'] = "2 electrons; No muons, jets, or photons; Missing momentum > 10 GeV"
# extralabel['sel2RecoEle_vetoes_absD0Gt0p5'] = "2 electrons with |d_0|>0.1 mm; No muons, jets, or photons"
extralabel['sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt0p5'] = "2 electrons with |d_0|>0.5 mm; No muons, jets, or photons; Missing momentum > 10 GeV"

colors = {}
colors['eenu_30GeV_1p41e-6Ve'] = ROOT.kOrange+1
colors['eenu_50GeV_1p41e-6Ve'] = ROOT.kRed
colors['eenu_70GeV_1p41e-6Ve'] = ROOT.kBlue
colors['eenu_90GeV_1p41e-6Ve'] = ROOT.kGreen+1

colors['Zbb'] = ROOT.kAzure-4
colors['Zcc'] = ROOT.kCyan-9
colors['Zud'] = ROOT.kViolet-4
colors['Zss'] = ROOT.kOrange+1
colors['Ztautau'] = ROOT.kRed-3
colors['Zee'] = ROOT.kGray+2
colors['Zmumu'] = ROOT.kGreen+1

#colors['Ztautau_spring2021'] = ROOT.kBlack
#colors['Ztautau_pre_winter2023_tests_v2'] = ROOT.kRed


plots = {}
plots['HNL'] = {'signal':{
                     #'eenu_30GeV_1p41e-6Ve':['eenu_30GeV_1p41e-6Ve'],
                     #'eenu_50GeV_1p41e-6Ve':['eenu_50GeV_1p41e-6Ve'],
                     #'eenu_70GeV_1p41e-6Ve':['eenu_70GeV_1p41e-6Ve'],
                     #'eenu_90GeV_1p41e-6Ve':['eenu_90GeV_1p41e-6Ve'],
    },
                'backgrounds':{
                    'Zbb':['p8_ee_Zbb_ecm91'],
                    'Zcc': ['p8_ee_Zcc_ecm91'],
                    'Zud': ['p8_ee_Zud_ecm91'],
                    'Zss': ['p8_ee_Zud_ecm91'],
                    'Ztautau': ['p8_ee_Ztautau_ecm91'],
                    'Zee':['p8_ee_Zee_ecm91'],
                    'Zmumu':['p8_ee_Zmumu_ecm91'],
                    #'Ztautau_spring2021': ['p8_ee_Ztautau_ecm91_spring2021'],
                    #'Ztautau_pre_winter2023_tests_v2': ['p8_ee_Ztautau_ecm91_pre_winter2023_tests_v2'],
                },}
                #'backgrounds':{}}



legend = {}
legend['eenu_30GeV_1p41e-6Ve'] = 'm_{N} = 30 GeV, V_{e} = 1.41e-6'
legend['eenu_50GeV_1p41e-6Ve'] = 'm_{N} = 50 GeV, V_{e} = 1.41e-6'
legend['eenu_70GeV_1p41e-6Ve'] = 'm_{N} = 70 GeV, V_{e} = 1.41e-6'
legend['eenu_90GeV_1p41e-6Ve'] = 'm_{N} = 90 GeV, V_{e} = 1.41e-6'

legend['Zbb'] = 'e^{+}e^{-} #rightarrow Z #rightarrow bb'
legend['Zcc'] = 'e^{+}e^{-} #rightarrow Z #rightarrow cc'
legend['Zud'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ud'
legend['Zss'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ss'
legend['Ztautau'] = 'e^{+}e^{-} #rightarrow Z #rightarrow #tau#tau'
legend['Zmumu'] = 'e^{+}e^{-} #rightarrow Z #rightarrow #mu#mu'
legend['Zee'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ee'
#legend['Ztautau_spring2021'] = 'Z #rightarrow #tau#tau Spring2021'
#legend['Ztautau_pre_winter2023_tests_v2'] = 'Z #rightarrow #tau#tau pre winter2023 tests v2'

