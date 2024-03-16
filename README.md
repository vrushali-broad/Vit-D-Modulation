Effect of Vitamin D modulation on TH2 cell function 
- 

- Result 1: VDAART cohort analysis
  - Preprocess_data.ipynb - Preprocess VDAART data to generate counts and meta data.  
  - Normalize_data.ipynb - Normalize counts data to prepare for clustering based on VDR signaling genes.
  - extract_vdr_genes.py - Extract VDR pathway genes from AMIGO2 and WikiPathways.  
  - Cluster_VitD.ipynb -	Cluster counts data based on VDR pathway genes.  				 
  - VDAART_DE_analysis.ipynb - Perform DE analysis between HIGH VIT-D and Low VIT-D groups. This script also performs GO enrichment analysis.  
  - Plot_KEGG.ipynb	- Perform KEGG enrichment analysis.  
  - Plots.ipynb - Heatmap and boxplots for VDAART cohort analysis.  

- Result 2: Analysis of calcitriol-stimulated TH2 cells  
  - Calcitriol_stimulation.ipynb - Jupyter notebook for performing DE analysis and GO enrichment analysis of calcitriol stimulated TH2 cells.  

- Result 3: Modeling of Calcitriol-VDR signaling network model  
  - extract_kegg_interactions.R - Extract interactions from TCR signaling and Calcium signaling pathways from KEGG.  
  - Rules/ - Discrete dynamical modeling rules for executing different input conditions in the network model.  
  - run_sim.R - Executes simulations from network models using BoolNet.  
  - Output/ - Output files of model output after running run_sim.R.  

- Result 4: Analysis of Vit-D deficient TH2 cells   
  - VitD_deficient.ipynb - Jupyter notebook for performing DE anlaysis and GO enrichment analysis of Vit-D deficient cells.  

- Plot_KEGG_TH2.ipynb - KEGG enrichment analysis of calcitriol stimulated and Vit-D deficient cells.  
- Heatmap_Plots_TH2.ipynb - Heatmaps of differentially expressed genes from calctriol stimulated and Vit-D deficient cells.  
