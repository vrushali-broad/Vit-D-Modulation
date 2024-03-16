Effect of Vitamin D modulation on TH2 cell function 
- 

1. Result 1: VDAART cohort analysis
  1. Preprocess_data.ipynb - Preprocess VDAART data to generate counts and meta data.  
  2. Normalize_data.ipynb - Normalize counts data to prepare for clustering based on VDR signaling genes.
  3. extract_vdr_genes.py - Extract VDR pathway genes from AMIGO2 and WikiPathways.  
  4. Cluster_VitD.ipynb -	Cluster counts data based on VDR pathway genes.  				 
  5. VDAART_DE_analysis.ipynb - Perform DE analysis between HIGH VIT-D and Low VIT-D groups. This script also performs GO enrichment analysis.  
  6. Plot_KEGG.ipynb	- Perform KEGG enrichment analysis.  
  7. Plots.ipynb - Heatmap and boxplots for VDAART cohort analysis.  

2. Result 2: Analysis of calcitriol-stimulated TH2 cells  
  1. Result_2/Calcitriol_stimulation.ipynb - Jupyter notebook for performing DE analysis and GO enrichment analysis of calcitriol stimulated TH2 cells.  

3. Result 3: Modeling of Calcitriol-VDR signaling network model  
  1. extract_kegg_interactions.R - Extract interactions from TCR signaling and Calcium signaling pathways from KEGG.  
  2. Rules/ - Discrete dynamical modeling rules for executing different input conditions in the network model.  
  3. run_sim.R - Executes simulations from network models using BoolNet.  
  4. Output/ - Output files of model output after running run_sim.R.  

4. Result 4: Analysis of Vit-D deficient TH2 cells   
  1. /VitD_deficient.ipynb - Jupyter notebook for performing DE anlaysis and GO enrichment analysis of Vit-D deficient cells.  

5. Plot_KEGG_TH2.ipynb - KEGG enrichment analysis of calcitriol stimulated and Vit-D deficient cells.  
6. Heatmap_Plots_TH2.ipynb - Heatmaps of differentially expressed genes from calctriol stimulated and Vit-D deficient cells.  
