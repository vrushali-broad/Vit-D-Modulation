## 📜 Citation

<p align="center">
  <img src="assets/cover.tif.jpg" alt="Vitamin D and TH2 Cell Plasticity Cover" width="80%">
</p>

If you use this repository, please cite the following article:

**Cover Article**  
> **Vrushali D. Fangal, Ayşe Kılıç, Hooman Mirzakhani, Augusto A. Litonjua, Marie B. Demay, Bruce D. Levy, Scott T. Weiss**  
> *Vitamin D Exerts Endogenous Control over T<sub>H</sub>2 Cell Fate and Immune Plasticity.*  
> *iScience*, Volume 28, Issue 4, 18 April 2025, Article 112117. ISSN: 2589-0042.  
> [DOI: 10.1016/j.isci.2025.112117](https://doi.org/10.1016/j.isci.2025.112117)  
> 📖 [Read online here](https://www.sciencedirect.com/science/article/pii/S2589004225003773)


---

### 🧬 Abstract

**Summary:**  
Circulating Vitamin D (Vit-D) has emerged as a potent immune modulator in asthma, yet its direct impact on T<sub>H</sub>2 cell regulation—the central effectors of allergic inflammation—remains unclear. Preliminary transcriptomic analysis of neonatal cord blood revealed that gestational Vit-D deficiency corresponds to elevated adaptive and innate immune responses, driven by T<sub>H</sub>2 immunity and antimicrobial responses related to asthma inflammation. To elucidate cell-specific molecular mechanisms of Vit-D, we differentiated murine T<sub>H</sub>2 cells *in vitro* under conditions mimicking Vit-D sufficiency and deficiency. Our findings demonstrate that Vit-D exposure promotes intracellular calcium ion homeostasis while suppressing prominent inflammatory cytokines characteristic of asthma. Conversely, Vit-D deficiency reprograms T<sub>H</sub>2 cell lineage commitment, inducing overexpression of cytolytic molecules and MHC class I molecules—traits typically associated with cytotoxicity rather than helper function. These findings underscore Vit-D’s role in stabilizing T<sub>H</sub>2 cell function and fate, offering insights into asthma and autoimmune disorders.


Effect of Vitamin D modulation on T<sub>H</sub>2 cell function 
- 

- Result 1: VDAART cohort analysis
  - Preprocess_data.ipynb - Preprocess VDAART data to generate counts and meta data.  
  - Normalize_data.ipynb - Normalize counts data to prepare for clustering based on VDR signaling genes.
  - extract_vdr_genes.py - Extract VDR pathway genes from AMIGO2 and WikiPathways.  
  - Cluster_VitD.ipynb -	Cluster counts data based on VDR pathway genes.  				 
  - VDAART_DE_analysis.ipynb - Perform DE analysis between HIGH VIT-D and Low VIT-D groups. This script also performs GO enrichment analysis.  
  - Plot_KEGG.ipynb	- Perform KEGG enrichment analysis.  
  - Plots.ipynb - Heatmap and boxplots for VDAART cohort analysis.  

- Result 2: Analysis of calcitriol-stimulated T<sub>H</sub>2 cells  
  - Calcitriol_stimulation.ipynb - Jupyter notebook for performing DE analysis and GO enrichment analysis of calcitriol stimulated T<sub>H</sub>2 cells.  

- Result 3: Modeling of Calcitriol-VDR signaling network model  
  - extract_kegg_interactions.R - Extract interactions from TCR signaling and Calcium signaling pathways from KEGG.  
  - Rules/ - Discrete dynamical modeling rules for executing different input conditions in the network model.  
  - run_sim.R - Executes simulations from network models using BoolNet.  
  - Output/ - Output files of model output after running run_sim.R.  

- Result 4: Analysis of Vit-D deficient T<sub>H</sub>2 cells   
  - VitD_deficient.ipynb - Jupyter notebook for performing DE anlaysis and GO enrichment analysis of Vit-D deficient cells.  

- Plot_KEGG_TH2.ipynb - KEGG enrichment analysis of calcitriol stimulated and Vit-D deficient cells.  
- Heatmap_Plots_TH2.ipynb - Heatmaps of differentially expressed genes from calctriol stimulated and Vit-D deficient cells.  
