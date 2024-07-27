# Explanation of analysis used in report

The initial analysis step was contained within files following the naming convention `analysis_*_stage1.py`. A final analysis stage was then run using files names `analysis_*_final.py`, and files named `analysis_*_plots.py` were used for generation of histograms.

The plots presented within the report were generated using the files named `analysis_essentials_*.py`, which contain only the parameters relevant to the report. The current `analysis_essentials_stage1.py` is formatted to run on the winter2023 edm4hep format. This was run over both the winter2023 background samples and the privately produced Majorana HNL signals. 

A second series of files names `analysis_GenVsReco_*.py` were used to generate a set of comparisons between generator level and reconstructed level variables. The variables considered here were those discussed in the final section of the report describing generator level filtering. 

For all work done including jets, the anti_kt jet reclustering algorithm was used, as can be seen in [this code snippet](https://github.com/John-Hayward/FCCAnalyses/blob/master/project_analysis/analysis_files/analysis_essentials_stage1.py#L98-L113)

Reconstruction of displaced vertices was performed using [LCFIPlus get_SV_event](https://github.com/John-Hayward/FCCAnalyses/blob/master/project_analysis/analysis_files/analysis_essentials_stage1.py#L136-L142) requiring parameters on vertexes of p_t>1GeV and d0>2mm. 
