#Mandatory: List of processes
processList = {

        #centrally-produced backgrounds
        #'p8_ee_Zee_ecm91':{'chunks':100, 'fraction':0.01},
        #'p8_ee_Zbb_ecm91':{'chunks':100, 'fraction':1},
        #'p8_ee_Ztautau_ecm91':{'chunks':100, 'fraction':1},
        #'p8_ee_Zud_ecm91':{'chunks':100, 'fraction':1},
        #'p8_ee_Zcc_ecm91':{'chunks':100, 'fraction':1},
        #'p8_ee_Zss_ecm91':{'chunks':100, 'fraction':1},
        #'p8_ee_Zmumu_ecm91':{'chunks':100, 'fraction':1},

        #privately-produced signals
        'HNL_Majorana_eenu_10GeV_2e-4Ve':{},
        'HNL_Majorana_eenu_20GeV_9e-5Ve':{},
        'HNL_Majorana_eenu_20GeV_3e-5Ve':{},
        'HNL_Majorana_eenu_30GeV_1e-5Ve':{},
        'HNL_Majorana_eenu_50GeV_6e-6Ve':{},

        #test
        #'p8_ee_Zee_ecm91':{'fraction':0.000001},
        #'p8_ee_Zuds_ecm91':{'chunks':10,'fraction':0.000001},
        #'filteredevents_Zbb_lifetimecut3em11':{},
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
outputDir = "DVTest/1mm_tracks/output_stage1"

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
               .Alias("Electron0", "Electron#0.index")
               .Define("RecoElectrons", "ReconstructedParticle::get(Electron0, ReconstructedParticles)")
               .Define("n_RecoElectrons", "ReconstructedParticle::get_n(RecoElectrons)")

               .Alias("Muon0", "Muon#0.index")
               .Define("RecoMuons", "ReconstructedParticle::get(Muon0, ReconstructedParticles)")
               .Define("n_RecoMuons", "ReconstructedParticle::get_n(RecoMuons)")

               .Alias("Photon0", "Photon#0.index")
               .Define("RecoPhotons", "ReconstructedParticle::get(Photon0, ReconstructedParticles)")
               .Define("n_RecoPhotons", "ReconstructedParticle::get_n(RecoPhotons)")

               .Define("n_RecoJets", "ReconstructedParticle::get_n(Jet)")

               .Define("RecoMissingEnergy_p", "ReconstructedParticle::get_p(MissingET)")

               .Define("RecoElectronTrack_absD0", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(RecoElectrons ,EFlowTrack_1))")

                ###Reclustering starts here
                .Define("my_leptons", "ReconstructedParticle::merge(RecoElectrons, RecoMuons)")
                .Define("my_recoparticles", "ReconstructedParticle::remove(ReconstructedParticles, my_leptons)")

                .Define("RP_px", "ReconstructedParticle::get_px(my_recoparticles)")
                .Define("RP_py", "ReconstructedParticle::get_py(my_recoparticles)")
                .Define("RP_pz", "ReconstructedParticle::get_pz(my_recoparticles)")
                .Define("RP_e", "ReconstructedParticle::get_e(my_recoparticles)")

                .Define("pseudo_jets", "JetClusteringUtils::set_pseudoJets_xyzm(RP_px, RP_py, RP_pz, RP_e)")

                .Define("FCCAnalysesJets_antikt", "JetClustering::clustering_antikt(0.4, 0, 5., 0, 0)(pseudo_jets)")

                .Define("antikt_jets", "JetClusteringUtils::get_pseudoJets(FCCAnalysesJets_antikt)")

                .Define("jets_antikt_px", "JetClusteringUtils::get_px(antikt_jets)")
                .Define("n_antikt_jets", "jets_antikt_px.size()")

                ###Momentum after reclustering

                .Define("lepton_p", "ReconstructedParticle::get_total_p(my_leptons)")
                .Define("reclustered_p", "JetClusteringUtils::get_total_p(antikt_jets)")

                .Define("reclustered_missing_p", "sqrt((lepton_p[0]+reclustered_p[0])*(lepton_p[0]+reclustered_p[0]) + (lepton_p[1]+reclustered_p[1])*(lepton_p[1]+reclustered_p[1]) + (lepton_p[2]+reclustered_p[2])*(lepton_p[2]+reclustered_p[2]))")


                ###Filter to reduce file size and increase processing speed
                #.Filter("n_RecoElectrons==2")

                #Displaced vertex stuff
                
                #Select tracks that are reconstructed as primaries
                .Define("RecoedPrimaryTracks", "VertexFitterSimple::get_PrimaryTracks(EFlowTrack_1, true, 4.5, 20e-3, 300, 0., 0., 0.)")

                #The final primary Vertex
                .Define("PrimaryVertexObject", "VertexFitterSimple::VertexFitter_Tk(1, RecoedPrimaryTracks, true, 4.5, 20e-3, 300)")


                #select tracks with pT >1GeV
                .Define("sel_tracks_pt", "VertexingUtils::sel_pt_tracks(1)(EFlowTrack_1)")
                #select tracks with |d_0| > 2mm
                .Define("sel_tracks", "VertexingUtils::sel_d0_tracks(1)(sel_tracks_pt)")
                #find the DVs
                .Define("DV_evt_seltracks", "VertexFinderLCFIPlus::get_SV_event(sel_tracks, EFlowTrack_1, PrimaryVertexObject, true, 9., 40., 5.)")
                #find number of DVs
                .Define("n_seltracks_DVs", "VertexingUtils::get_n_SV(DV_evt_seltracks)")

                .Define("DV_Lxyz", "VertexingUtils::get_d3d_SV(DV_evt_seltracks, PrimaryVertexObject)")
                .Define("DV_Lxyz_sig", "myUtils::get_d3d_SV_Sig(DV_evt_seltracks, PrimaryVertexObject)")

               )
                return df2

        def output():
                branchList = [
                        ######## Monte-Carlo particles #######
                        "n_RecoElectrons",
                        "n_RecoMuons",
                        "n_RecoPhotons",
                        "n_RecoJets",
                        "RecoMissingEnergy_p",
                        "RecoElectronTrack_absD0",
                        "reclustered_missing_p",
                        "n_antikt_jets",
                        "n_seltracks_DVs",
                        "DV_Lxyz",
                        "DV_Lxyz_sig",
                        
		]

                return branchList
