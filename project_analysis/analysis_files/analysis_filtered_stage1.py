#Mandatory: List of processes
processList = {

        #centrally-produced backgrounds
        #'p8_ee_Zee_ecm91':{'chunks':100, 'fraction':0.01},
        #'p8_ee_Zbb_ecm91':{'chunks':100, 'fraction':0.005},
        #'p8_ee_Ztautau_ecm91':{'chunks':100, 'fraction':1},
        #'p8_ee_Zud_ecm91':{'chunks':100, 'fraction':1},
        #'p8_ee_Zcc_ecm91':{'chunks':100, 'fraction':1},
        #'p8_ee_Zss_ecm91':{'chunks':100, 'fraction':1},
        #'p8_ee_Zmumu_ecm91':{'chunks':100, 'fraction':1},

        #privately-produced signals
        #'HNL_Majorana_eenu_10GeV_2e-4Ve':{},
        #'HNL_Majorana_eenu_20GeV_9e-5Ve':{},
        #'HNL_Majorana_eenu_20GeV_3e-5Ve':{},
        #'HNL_Majorana_eenu_30GeV_1e-5Ve':{},
        #'HNL_Majorana_eenu_50GeV_6e-6Ve':{},

        #test
        #'p8_ee_Zee_ecm91':{'fraction':0.000001},
        #'p8_ee_Zuds_ecm91':{'chunks':10,'fraction':0.000001},
        #'filteredevents_Zbb_lifetimecut3em11':{},
        #'1000_Zbb_lifetime_3e-11':{},
        #'5e4_Zbb_lifetimecut':{},
        #'filteredevents_Zbb_lifetimecut_3em11':{},
        #'Zbb_inclusive_test':{},
        #'no_filter_test':{},
        #'main_branch_pythia_card':{},
        #'old_key4hep_stack_Zbb':{}
        #'winter23_delphes_Zbb_test':{},
        'Delphes_test':{},
}

#Production tag. This points to the yaml files for getting sample statistics
#Mandatory when running over EDM4Hep centrally produced events
#Comment out when running over privately produced events
#prodTag     = "FCCee/winter2023/IDEA/"

#Input directory
#Comment out when running over centrally produced events
#Mandatory when running over privately produced events
#inputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/spring2021/output_MadgraphPythiaDelphes"
#inputDir = "/eos/experiment/fcc/ee/generation/DelphesStandalone/Edm4Hep/pre_winter2023_tests_v2"
#inputDir = "/eos/experiment/fcc/ee/generation/DelphesEvents/spring2021/IDEA"
inputDir = "/eos/user/j/jhayward/signalGeneration/signals"
#inputDir = "/afs/cern.ch/work/w/williams/public/FCCSkimming/k4Gen/"
#Optional: output directory, default is local dir
#outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/spring2021/output_stage1/"
#outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/pre_winter2023_tests_v2/output_stage1/"
#outputDir = "/eos/user/j/jalimena/FCCeeLLP/"
outputDir = "backgroundFilterTest/new_card/output_stage1"

#outputDirEos = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNL_Majorana_eenu/spring2021/output_stage1/"
#outputDirEos = "/eos/user/j/jalimena/FCCeeLLP/"
#outputDirEos = "/eos/user/j/jhayward/analysis/winter2023_fulldataset/output_stage1_2el"
#outputDirEos = "/eos/user/j/jhayward/analysis/reclustered/winter23_2el/output_stage1"
eosType = "eosuser"

#Optional: ncpus, default is 4
nCPUS       = 6

#Optional running on HTCondor, default is False
runBatch    = False
#runBatch    = True

#Optional batch queue name when running on HTCondor, default is workday
#batchQueue = "johnHnls"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
compGroup = "group_u_FCC.local_gen"

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():
        def analysers(df):

                df2 = (df

                #Access the various objects and their properties with the following syntax: .Define("<your_variable>", "<accessor_fct (name_object)>")
		#This will create a column in the RDataFrame named <your_variable> and filled with the return value of the <accessor_fct> for the given collection/object 
		#Accessor functions are the functions found in the C++ analyzers code that return a certain variable, e.g. <namespace>::get_n(object) returns the number 
		#of these objects in the event and <namespace>::get_pt(object) returns the pt of the object. Here you can pick between two namespaces to access either
		#reconstructed (namespace = ReconstructedParticle) or MC-level objects (namespace = MCParticle). 
		#For the name of the object, in principle the names of the EDM4HEP collections are used - photons, muons and electrons are an exception, see below

		#OVERVIEW: Accessing different objects and counting them
               #.Define("GenElectron_PID", "FCCAnalyses::MCParticle::sel_pdgID(11, true)(GenParticles)")
               .Define("GenElectron_PID", "FCCAnalyses::MCParticle::sel_pdgID(11, true)(Particle)")
               .Define("FSGenElectron", "FCCAnalyses::MCParticle::sel_genStatus(1)(GenElectron_PID)")
               .Define("n_FSGenElectron", "FCCAnalyses::MCParticle::get_n(FSGenElectron)")

               #.Define("GenPhoton_PID", "FCCAnalyses::MCParticle::sel_pdgID(22, true)(Particle)")
               #.Define("FSGenPhoton", "FCCAnalyses::MCParticle::sel_genStatus(1)(GenPhoton_PID)")
               #.Define("n_FSGenPhoton", "FCCAnalyses::MCParticle::get_n(FSGenPhoton)")

               #.Define("GenBs0_PID", "FCCAnalyses::MCParticle::sel_pdgID(531, true)(GenParticles)")
               .Define("GenBs0_PID", "FCCAnalyses::MCParticle::sel_pdgID(531, true)(Particle)")
               .Define("FSGenBs0", "FCCAnalyses::MCParticle::sel_genStatus(1)(GenBs0_PID)")
               .Define("n_FSGenBs0", "FCCAnalyses::MCParticle::get_n(FSGenBs0)")

               #.Define("AllGenBs0_PID", "FCCAnalyses::MCParticle::sel_pdgID(531, false)(GenParticles)")
               .Define("AllGenBs0_PID", "FCCAnalyses::MCParticle::sel_pdgID(531, false)(Particle)")
               .Define("n_AllGenBs0", "FCCAnalyses::MCParticle::get_n(AllGenBs0_PID)")

               #.Define("AllGenBs_PID", "FCCAnalyses::MCParticle::sel_Bs(true)(GenParticles)")
               .Define("AllGenBs_PID", "FCCAnalyses::MCParticle::sel_Bs(true)(Particle)")
               .Define("n_AllGenBs", "FCCAnalyses::MCParticle::get_n(AllGenBs_PID)")

               .Define("AllGenBs_vertex_x", "FCCAnalyses::MCParticle::get_vertex_x( AllGenBs_PID )")
               .Define("AllGenBs_vertex_y", "FCCAnalyses::MCParticle::get_vertex_y( AllGenBs_PID )")
               .Define("AllGenBs_vertex_z", "FCCAnalyses::MCParticle::get_vertex_z( AllGenBs_PID )")

               .Define("AllGenBs_endpoint_x", "FCCAnalyses::MCParticle::get_endPoint_x( AllGenBs_PID )")
               .Define("AllGenBs_endpoint_y", "FCCAnalyses::MCParticle::get_endPoint_y( AllGenBs_PID )")
               .Define("AllGenBs_endpoint_z", "FCCAnalyses::MCParticle::get_endPoint_z( AllGenBs_PID )")

               .Define("AllGenBs_Lxyz", "return sqrt((AllGenBs_vertex_x-AllGenBs_endpoint_x)*(AllGenBs_vertex_x-AllGenBs_endpoint_x) + (AllGenBs_vertex_y-AllGenBs_endpoint_y)*(AllGenBs_vertex_y-AllGenBs_endpoint_y) + (AllGenBs_vertex_z-AllGenBs_endpoint_z)*(AllGenBs_vertex_z-AllGenBs_endpoint_z))")
               .Define("AllGenBs_t", "return (AllGenBs_Lxyz / (2.998e+11))")

               )
                return df2

        def output():
                branchList = [
                        ######## Monte-Carlo particles #######
                        "n_FSGenElectron",
                        #"n_FSGenPhoton",
                        "n_FSGenBs0",
                        "n_AllGenBs0",
                        "n_AllGenBs",
                        "AllGenBs_t",
                        "AllGenBs_vertex_x",
                        "AllGenBs_vertex_y",
                        "AllGenBs_vertex_z",
                        "AllGenBs_endpoint_x",
                        "AllGenBs_endpoint_y",
                        "AllGenBs_endpoint_z",
                        #"n_RecoElectrons",
                        #"n_RecoMuons",
                        #"n_RecoPhotons",
                        #"n_RecoJets",
                        #"RecoMissingEnergy_p",
                        #"RecoElectronTrack_absD0",
                        #"reclustered_missing_p",
                        #"n_antikt_jets",
                        #"n_seltracks_DVs"
                        
		]

                return branchList
