import ROOT

# global parameters
intLumi        = 150.0e+6 #in pb-1

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
#scaleSig       = 0
#scaleBack      = 0
ana_tex        = 'e^{+}e^{-} #rightarrow N #nu, N #rightarrow ee#nu'
#ana_tex        = ''
delphesVersion = '3.4.2'
#delphesVersion = ''
energy         = 91
collider       = 'FCC-ee'
inputDir       = 'DVTest/1mm_tracks/output_finalSel/'
#inputDir = 'reclustered/winter23_2el/output_finalSel_extra_cuts/'
#inputDir       = 'output_finalSel_Ztautau/'
formats        = ['png']
#formats        = ['pdf']
yaxis          = ['lin','log']
stacksig       = ['nostack']
outdir         = 'DVTest/1mm_tracks/plots'
#outdir = 'reclustered/winter23_2el/plots_stacked'
#outdir         = 'plots_Ztautau_spring2021_vs_prewinter2023/'
splitLeg       = True

variables = [      
        'n_seltracks_DVs',
        'n_RecoElectrons',
        'n_RecoMuons',
        'n_RecoJets',
        'RecoMissingEnergy_p',
        'RecoElectronTrack_absD0',
        'n_RecoPhotons',
        'n_antikt_jets',
        'reclustered_missing_p',
        'DV_Lxyz',
        'DV_Lxyz_sig',
             ]

    
###Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['HNL']  = [
    #"selNone",
    # "sel1FSGenEle",
    # "sel1FSGenEle_eeInvMassGt80",
    # "sel1FSGenNu",
    "selNone",
    "sel2RecoEle",
    "sel2RecoEle_1DV",
    "sel2RecoEle_1DV_vetoes",
    # "sel2RecoEle_absD0Gt0p1",
    "sel2RecoEle_1DV_vetoes_MissingEnergyGt10",
    # "sel2RecoE_1DVle_vetoes_absD0Gt0p5",
    "sel2RecoEle_1DV_vetoes_MissingEnergyGt10_absD0Gt0p5",
    "sel2RecoEle_1DV_vetoes_MissingEnergyGt10_absD0Gt2p0",
    "sel2RecoEle_1DV_vetoes_MissingEnergyGt10_absD0Gt4p0",
    #"sel2RecoEle_vetoes",
]

extralabel = {}
#extralabel['selNone'] = "Before selection"
# extralabel['sel1FSGenEle'] = "At least 1 final state gen electron"
# extralabel['sel1FSGenEle_eeInvMassGt80'] = "At least 1 final state gen electron, gen ee inv mass > 80 GeV"
# extralabel['sel1FSGenNu'] = "At least 1 final state gen neutrino
extralabel['selNone'] = "Before selection"
extralabel['sel2RecoEle'] = "2 electrons"
extralabel['sel2RecoEle_1DV'] = "2 electrons; Exactly 1 DV"
extralabel['sel2RecoEle_1DV_vetoes'] = "2 electrons; Exactly 1 DV; No muons, jets, or photons"
#extralabel['sel2RecoEle_vetoes'] = "2 electrons; No muons, or photons"
# extralabel['sel2RecoEle_absD0Gt0p1'] = "2 electrons with |d_0|>0.1 mm"
extralabel['sel2RecoEle_1DV_vetoes_MissingEnergyGt10'] = "2 electrons; No muons, jets, or photons; Missing momentum > 10 GeV; Exactly 1 DV"
# extralabel['sel2RecoE_1DVle_vetoes_absD0Gt0p5'] = "2 electrons with |d_0|>0.1 mm; No muons, jets, or photons"
extralabel['sel2RecoEle_1DV_vetoes_MissingEnergyGt10_absD0Gt0p5'] = "2 electrons with |d_0|>0.5 mm; No muons, jets, or photons; Missing momentum > 10 GeV; Exactly 1 DV"
extralabel['sel2RecoEle_1DV_vetoes_MissingEnergyGt10_absD0Gt2p0'] = "2 electrons with |d_0|>2.0 mm; No muons, jets, or photons; Missing momentum > 10 GeV; Exactly 1 DV"
extralabel['sel2RecoEle_1DV_vetoes_MissingEnergyGt10_absD0Gt4p0'] = "2 electrons with |d_0|>4.0 mm; No muons, jets, or photons; Missing momentum > 10 GeV; Exactly 1 DV"

colors = {}
colors['HNL_Majorana_eenu_10GeV_2e-4Ve'] = ROOT.kOrange+1
colors['HNL_Majorana_eenu_20GeV_9e-5Ve'] = ROOT.kRed
colors['HNL_Majorana_eenu_20GeV_3e-5Ve'] = ROOT.kBlue
colors['HNL_Majorana_eenu_30GeV_1e-5Ve'] = ROOT.kGreen+1
colors['HNL_Majorana_eenu_50GeV_6e-6Ve'] = ROOT.kSpring+10

colors['Zbb'] = ROOT.kAzure-4
colors['Zcc'] = ROOT.kCyan-9
colors['Zud'] = ROOT.kViolet-4
colors['Ztautau'] = ROOT.kRed-3
colors['Zee'] = ROOT.kGray+2
colors['Zss'] = ROOT.kPink-8
colors['Zmumu'] = ROOT.kBlack
#colors['Zuds'] = ROOT.kViolet-4

#colors['Ztautau_spring2021'] = ROOT.kBlack
#colors['Ztautau_pre_winter2023_tests_v2'] = ROOT.kRed


plots = {}
plots['HNL'] = {'signal':{
                     'HNL_Majorana_eenu_10GeV_2e-4Ve':['HNL_Majorana_eenu_10GeV_2e-4Ve'],
                     'HNL_Majorana_eenu_20GeV_9e-5Ve':['HNL_Majorana_eenu_20GeV_9e-5Ve'],
                     'HNL_Majorana_eenu_20GeV_3e-5Ve':['HNL_Majorana_eenu_20GeV_3e-5Ve'],
                     'HNL_Majorana_eenu_30GeV_1e-5Ve':['HNL_Majorana_eenu_30GeV_1e-5Ve'],
                     'HNL_Majorana_eenu_50GeV_6e-6Ve':['HNL_Majorana_eenu_50GeV_6e-6Ve'],
    },
                'backgrounds':{
                    #'Zbb':['p8_ee_Zbb_ecm91'],
                    #'Zcc': ['p8_ee_Zcc_ecm91'],
                    #'Zud': ['p8_ee_Zud_ecm91'],
                    #'Ztautau': ['p8_ee_Ztautau_ecm91'],
                    #'Zee':['p8_ee_Zee_ecm91'],
                    #'Zmumu':['p8_ee_Zmumu_ecm91'],
                    #'Zuds':['p8_ee_Zuds_ecm91'],
                    },
                    #'Ztautau_spring2021': ['p8_ee_Ztautau_ecm91_spring2021'],
                    #'Ztautau_pre_winter2023_tests_v2': ['p8_ee_Ztautau_ecm91_pre_winter2023_tests_v2'],
                }



legend = {}
legend['HNL_Majorana_eenu_10GeV_2e-4Ve'] = 'm_{N} = 10 GeV, V_{e} = 2e-4'
legend['HNL_Majorana_eenu_20GeV_9e-5Ve'] = 'm_{N} = 20 GeV, V_{e} = 9e-5'
legend['HNL_Majorana_eenu_20GeV_3e-5Ve'] = 'm_{N} = 20 GeV, V_{e} = 3e-5'
legend['HNL_Majorana_eenu_30GeV_1e-5Ve'] = 'm_{N} = 30 GeV, V_{e} = 1e-5'
legend['HNL_Majorana_eenu_50GeV_6e-6Ve'] = 'm_{N} = 50 GeV, V_{e} = 6e-6'

legend['Zbb'] = 'e^{+}e^{-} #rightarrow Z #rightarrow bb'
legend['Zcc'] = 'e^{+}e^{-} #rightarrow Z #rightarrow cc'
legend['Zud'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ud'
legend['Ztautau'] = 'e^{+}e^{-} #rightarrow Z #rightarrow #tau#tau'
legend['Zee'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ee'
legend['Zmumu'] = 'e^{+}e^{-} #rightarrow Z #rightarrow #mu#mu'
legend['Zss'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ss'
#legend['Zuds'] = 'e^{+}e^{-} #rightarrow Z #rightarrow uds'
#legend['Ztautau_spring2021'] = 'Z #rightarrow #tau#tau Spring2021'
#legend['Ztautau_pre_winter2023_tests_v2'] = 'Z #rightarrow #tau#tau pre winter2023 tests v2'

