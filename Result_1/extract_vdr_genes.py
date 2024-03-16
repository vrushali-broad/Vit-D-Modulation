import xml.etree.ElementTree as ET

def extract_nodes_edges(gpml_path):
    tree = ET.parse(gpml_path)
    root = tree.getroot()
    ns = {'ns': 'http://pathvisio.org/GPML/2013a'}

    # Extracting unique nodes
    nodes = set(node.attrib['TextLabel'] for node in root.findall('.//ns:DataNode', ns))

    return list(nodes)  # Convert set back to list for the output

nodes = extract_nodes_edges('WP2877.gpml')
print('Processing WP2877.gpml ...')
print("Unique Nodes:", nodes)
print("#Unique Nodes:", len(nodes))

import pandas as pd
df = pd.read_csv('Amigo2_GO0042359.txt', sep = '\t', header =None)
print('Processing Amigo2_GO0042359.txt ...')
nodes2 = list(set(df.iloc[:,1]))
print("Unique Nodes:", nodes2) 
print("#Unique Nodes:", len(nodes2))

print(len(nodes + nodes2))

# lst1 = ['VDR', 'VDRE']
# ## GO
# lst2 = ['CYP2R1','CYP24A1', 'CYP27A1', 'CYP27B1', 'ENPP1', 'FGF23','FGFR1', 'FGFR4','GC','GFI1','IFNG','LRP2','NFKB1','SNAI1','SNAI2','TNF'] 
# ## WikiPathways
# lst3 = ['ABCB1', 'ABCA11', 'ABCD1', 'ADAMTS5', 'ADGRE5', 'ADRA1B', 'ADRB2', 'ALOX5', 'ALPG', 'ALPI',
# 'ASAP2', 'ATP2B1', 'ATP2C2', 'BCL6', 'BDKRB1', 'BGLAP', 'BMP6', 'BTLA', 'CA9', 'CALB1', 'CAMP',
# 'CASP14', 'CASP5', 'CBS', 'CCNC', 'CCND1', 'CCNE1', 'CD14', 'CD200', 'CD40', 'CD9', 'CDC34', 'CDK2',
# 'CDKAL1', 'CDKN1A', 'CDKN1B', 'CDKN2A', 'CDKN2B', 'CDKN2C', 'CDKN2D', 'CDX2', 'CEACAM1', 'CEBPA',
# 'CLDN2', 'CLEC16A', 'CLMN', 'CLPTM1L', 'COLEC11', 'CRACR2A', 'CRACR2B', 'CREG2', 'CST1', 'CST6', 
# 'CTLA4', 'CYP1A1', 'CYP24A1', 'CYP27B1', 'CYP2B6', 'CYP2C9', 'CYP2D6', 'CYP2S1', 'CYP3A4', 'CYP3A5',
# 'CYP7A1', 'COL13A1', 'DACT2', 'DEFB109C', 'DEFB132', 'DEFB4A', 'DND1', 'DNER', 'DUSP10', 'EFNA5',
# 'EPHB4', 'FGF23', 'FOXO1', 'G0S2', 'G6PD', 'GADD45A', 'GXYLT2', 'HIF1A', 'HILPDA', 'HLA-DQA1', 'HLA-DRB1',
# 'HNF1A', 'HSD17B2', 'ID1', 'ID4', 'IGFBP1', 'IGFBP3', 'IGFBP5', 'IGSF9B', 'IL12A', 'IL1RL1', 'IL25', 'IRF4',
# 'IRF5', 'IRF8', 'ITGAM', 'JUNB', 'KL', 'KLF4', 'KLK6', 'KNG1', 'KRT13', 'KRT16', 'KRT34', 'KRT38', 'KRT71',
# 'KRTAP10-2', 'KRTAP10-4', 'KRTAP10-7', 'KRTAP10-9', 'KRTAP12-2', 'KRTAP4-1', 'KRTAP5-1', 'KRTAP5-4', 'KRTAP8-1',
# 'LCE1D', 'LCE1F', 'LCE2B', 'LGALS9', 'LPGAT1', 'LRP5', 'LRRC25', 'LRRC8A', 'Ligand', 'MED9', 'MEG8', 'MX2', 
# 'MXD1', 'MYC', 'MYO9B', 'NFATC2', 'NINJ1', 'NOX1', 'NRIP1', 'ORM1', 'ORM2', 'PNOC', 'PPARD', 'PRDM1', 'PRKCQ',
# 'PTGER4', 'PTH', 'PTHLH', 'RASGRP1', 'RXRA', 'S100A2', 'S100A4', 'S100A6', 'S100A8', 'S100A9', 'S100G', 'SALL4',
# 'SATB1', 'SEMA3B', 'SERPINB1', 'SFRP1', 'SLC2A4', 'SLC34A2', 'SLC37A2', 'SLC8A1', 'SOSTDC1', 'SPP1', 'SPRR1B', 'STAM', 
# 'STEAP4', 'STS', 'SULT1C2', 'SULT2A1', 'TGFB1', 'TGFB2', 'THBD', 'TIMP2', 'TIMP3', 'TNFAIP3', 'TNFRSF11B', 'TNFSF11',
# 'TNFSF4', 'TPM1', 'TRAK1', 'TREM1', 'TRPV5', 'TRPV6','VDR', 'ZNF257']

# print(len(set(lst1)), len(set(lst2)), len(set(lst3) - set(lst1) - set(lst2)))
# print(len(set(lst2+lst3)))