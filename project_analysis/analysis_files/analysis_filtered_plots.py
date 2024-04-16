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
inputDir       = 'backgroundFilterTest/stack_test/output_finalSel/'
#inputDir = 'reclustered/winter23_2el/output_finalSel_extra_cuts/'
#inputDir       = 'output_finalSel_Ztautau/'
formats        = ['png']
#formats        = ['pdf']
yaxis          = ['lin','log']
stacksig       = ['nostack']
outdir         = 'backgroundFilterTest/stack_test/plots_delphes'
#outdir = 'reclustered/winter23_2el/plots_stacked'
#outdir         = 'plots_Ztautau_spring2021_vs_prewinter2023/'
splitLeg       = True

variables = [      
        "n_AllGenBs",
        "AllGenBs_t",
        #"n_FSGenElectron",
        #"n_FSGenMuon",
        #"n_FSGenPhoton",
        #"n_RecoElectrons",
        #"n_RecoMuons",
        #"n_RecoPhotons",
        #"FSGen_Lxyz",
        #"RecoElectronTrack_absD0",
             ]

    
###Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['HNL']  = [
    "selNone",
    "selBs",
    #"sel2RecoEl",
    #"selVetoes",
    #"sel0p5disp",
]

extralabel = {}
extralabel['selNone'] = "Before selection"
extralabel['selBs'] = "At least one Bs"
#extralabel['sel2RecoEl'] = "2 reco electrons"
#extralabel['selVetoes'] = "No reco muons or photons"
#extralabel['sel0p5disp'] = "Both electrons diplaced > 0.5mm"


colors = {}
colors['filteredevents_Zbb_lifetimecut3em11'] = ROOT.kRed
colors['1000_Zbb_lifetime_3e-11'] = ROOT.kRed
colors['5e4_Zbb_lifetimecut'] = ROOT.kRed
colors['filteredevents_Zbb_lifetimecut_3em11'] = ROOT.kRed
colors['Zbb_inclusive_test'] = ROOT.kGreen
colors['no_filter_test'] = ROOT.kBlack
colors['main_branch_pythia_card'] = ROOT.kGreen
colors['old_key4hep_stack_Zbb'] = ROOT.kGreen
colors['winter23_delphes_Zbb_test'] = ROOT.kMagenta
colors['Delphes_test'] = ROOT.kGreen

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
colors['inclusive_scaled'] = ROOT.kPink
#colors['Zuds'] = ROOT.kViolet-4

#colors['Ztautau_spring2021'] = ROOT.kBlack
#colors['Ztautau_pre_winter2023_tests_v2'] = ROOT.kRed


plots = {}
plots['HNL'] = {'signal':{
                     #'HNL_Majorana_eenu_10GeV_2e-4Ve':['HNL_Majorana_eenu_10GeV_2e-4Ve'],
                     #'HNL_Majorana_eenu_20GeV_9e-5Ve':['HNL_Majorana_eenu_20GeV_9e-5Ve'],
                     #'HNL_Majorana_eenu_20GeV_3e-5Ve':['HNL_Majorana_eenu_20GeV_3e-5Ve'],
                     #'HNL_Majorana_eenu_30GeV_1e-5Ve':['HNL_Majorana_eenu_30GeV_1e-5Ve'],
                     #'HNL_Majorana_eenu_50GeV_6e-6Ve':['HNL_Majorana_eenu_50GeV_6e-6Ve'],
                     #'filteredevents_Zbb_lifetimecut3em11':['filteredevents_Zbb_lifetimecut3em11'],
                     #'1000_Zbb_lifetime_3e-11':['1000_Zbb_lifetime_3e-11'],
                     #'5e4_Zbb_lifetimecut':['5e4_Zbb_lifetimecut'],
                     #'filteredevents_Zbb_lifetimecut_3em11':['filteredevents_Zbb_lifetimecut_3em11'],
                     #'Zbb_inclusive_test':['Zbb_inclusive_test'],
                     #'no_filter_test':['no_filter_test'],
                     #'main_branch_pythia_card':['main_branch_pythia_card'],
                     #'old_key4hep_stack_Zbb':['old_key4hep_stack_Zbb'],
                     'winter23_delphes_Zbb_test':['winter23_delphes_Zbb_test'],
                     'Delphes_test':['Delphes_test'],
    },
                'backgrounds':{
                    'Zbb':['p8_ee_Zbb_ecm91'],
                    #'inclusive_scaled':['inclusive_scaled'],
                    #'Zcc': ['p8_ee_Zcc_ecm91'],
                    #'Zud': ['p8_ee_Zud_ecm91'],
                    #'Ztautau': ['p8_ee_Ztautau_ecm91'],
                    #'Zee':['p8_ee_Zee_ecm91'],
                    #'Zmumu':['p8_ee_Zmumu_ecm91'],
                    #'Zss':['p8_ee_Zss_ecm91'],
                    #'Zuds':['p8_ee_Zuds_ecm91'],
                    },
                    #'Ztautau_spring2021': ['p8_ee_Ztautau_ecm91_spring2021'],
                    #'Ztautau_pre_winter2023_tests_v2': ['p8_ee_Ztautau_ecm91_pre_winter2023_tests_v2'],
                }



legend = {}
#legend['filteredevents_Zbb_lifetimecut3em11'] = 'e^{+}e^{-} #rightarrow Z #rightarrow bb with MC level filter on lifetime'
legend['1000_Zbb_lifetime_3e-11'] = 'MC level cut'
legend['5e4_Zbb_lifetimecut'] = 'MC level cut'
legend['filteredevents_Zbb_lifetimecut_3em11'] = 'MC level cut'
legend['Zbb_inclusive_test'] = 'No MC level cut applied'
legend['no_filter_test'] = 'Inclusive in chunks of 1000'
legend['inclusive_scaled'] = 'winter23 lifetime scaled by 10'
legend['main_branch_pythia_card'] = 'Inclusive with pythia card from main'
legend['old_key4hep_stack_Zbb'] = 'Using old key4hep stack and k4run'
legend['winter23_delphes_Zbb_test'] = 'Generated with DelphesPythia_EDM4HEP'
legend['Delphes_test'] = 'Inclusive k4run with Delphes'


#legend['HNL_Majorana_eenu_10GeV_2e-4Ve'] = 'm_{N} = 10 GeV, V_{e} = 2e-4'
#legend['HNL_Majorana_eenu_20GeV_9e-5Ve'] = 'm_{N} = 20 GeV, V_{e} = 9e-5'
#legend['HNL_Majorana_eenu_20GeV_3e-5Ve'] = 'm_{N} = 20 GeV, V_{e} = 3e-5'
#legend['HNL_Majorana_eenu_30GeV_1e-5Ve'] = 'm_{N} = 30 GeV, V_{e} = 1e-5'
#legend['HNL_Majorana_eenu_50GeV_6e-6Ve'] = 'm_{N} = 50 GeV, V_{e} = 6e-6'
#
legend['Zbb'] = 'e^{+}e^{-} #rightarrow Z #rightarrow bb'
#legend['Zcc'] = 'e^{+}e^{-} #rightarrow Z #rightarrow cc'
#legend['Zud'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ud'
#legend['Ztautau'] = 'e^{+}e^{-} #rightarrow Z #rightarrow #tau#tau'
#legend['Zee'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ee'
#legend['Zmumu'] = 'e^{+}e^{-} #rightarrow Z #rightarrow #mu#mu'
#legend['Zss'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ss'
#legend['Zuds'] = 'e^{+}e^{-} #rightarrow Z #rightarrow uds'
#legend['Ztautau_spring2021'] = 'Z #rightarrow #tau#tau Spring2021'
#legend['Ztautau_pre_winter2023_tests_v2'] = 'Z #rightarrow #tau#tau pre winter2023 tests v2'

