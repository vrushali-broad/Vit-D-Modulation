Effect of Vitamin D modulation on TH2 cell function 
- 

Result 1: VDAART cohort analysis
- 
Preprocess_data.ipynb - 
extract_vdr_genes.py - 
Normalize_data.ipynb - 
Cluster_VitD.ipynb -					 
VDAART_DE_analysis.ipynb - 
Plot_KEGG.ipynb	-
Plots.ipynb - 

Result 2: Analysis of calcitriol-stimulated TH2 cells  
- 
Result_2/Calcitriol_stimulation.ipynb - Jupyter notebook for performing DE analysis and GO enrichment analysis of calcitriol stimulated TH2 cells.  

Result 3: Modeling of Calcitriol-VDR signaling network model  
- 
extract_kegg_interactions.R - Extract interactions from TCR signaling and Calcium signaling pathways from KEGG.  
Rules/ - Discrete dynamical modeling rules for executing different input conditions in the network model.  
run_sim.R - Executes simulations from network models using BoolNet.  
Output/ - Output files of model output after running run_sim.R.  

Result 4: Analysis of Vit-D deficient TH2 cells   
- 
Result_4
/VitD_deficient.ipynb - Jupyter notebook for performing DE anlaysis and GO enrichment analysis of Vit-D deficient cells.  

Plot_KEGG_TH2.ipynb - KEGG enrichment analysis of calcitriol stimulated and Vit-D deficient cells.  
Heatmap_Plots_TH2.ipynb - Heatmaps of differentially expressed genes from calctriol stimulated and Vit-D deficient cells.  
