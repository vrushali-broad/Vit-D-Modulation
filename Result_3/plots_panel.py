import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set the style for seaborn
sns.set(font_scale=1.5)

# Define the list of input files
input_files = [
    "Output/output_VitD_0.txt",
    "Output/output_VitD_1_PMCA_0.txt",
    "Output/output_VitD_1_PMCA_1.txt",
    "Output/output_VitD_1_CYP24A1_1.txt"
]

runs = 100  # Number of series
cycles = 800  # Number of measurements

for input_file in input_files:
    df = pd.read_csv(input_file, sep='\t')
    df = df.T

    print(df.shape, df.head())

    df_dict = {}
    for name in df.columns:
        row = np.mean(np.array(df[name]).reshape(runs, cycles), axis=0)
        df_dict[name] = row

    data = pd.DataFrame(df_dict)
    columns = ['TCR', 'VitD', 'ZAP70', 'p38', 'VDR', 'VDRact', 'RXRA', 'VDR_RXRA', 'Blimp1', 'Il10', 'Cyp24a1', 'Ctla4',
               'Plcg1', 'PMCA', 'PIP2', 'DAG', 'IP3', 'PKC', 'CA2', 'CALM1', 'CAMKII', 'AP1', 'NFAT', 'NFKB', 'CREB',
               'IL5', 'IL4', 'IL2', 'Calcitroic']

    data_sub = data[columns]

    yticklabels = ['TCR', 'Calcitriol','ZAP70', 'p38', 'VDR', 'Calcitriol-VDR', 'RXRA','VDR-RXRA',
                    'BLIMP-1', 'IL-10', 'CYP24A1', 'CTLA4', 'PLC$\\mathrm{\\gamma}$1', 'PMCA',
                    'PIP$_\\mathrm{2}$', 'DAG','IP$_\\mathrm{3}$','PKC', 'Ca$^\\mathrm{2+}$', 'CALM1', 'CAMKII',
                   'AP-1', 'NFAT', 'NF$\\mathrm{\\kappa}$B', 'CREB', 'IL-5', 'IL-4', 'Il-2','\nVit-D\nMetabolites' 
                  ]

    plt.figure(figsize=(2.8, 12))
    cmap = sns.diverging_palette(255, 0, sep=8, n=512, as_cmap=True)
    heatmap = sns.heatmap(data_sub.T[data_sub.T.columns[::100]], vmin=0, vmax=1, cmap=cmap, linewidths=.5, cbar=False,
                          yticklabels=yticklabels)
    heatmap.set_xticklabels(np.arange(100, 900, 100), rotation=90)

    # Setting tick marks on x and y axis
    heatmap.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True)
    heatmap.tick_params(axis='y', which='both', left=True, right=False, labelleft=True)

    # Adjust the position of the x-axis ticks and labels to move them down
    heatmap.xaxis.set_tick_params(pad=10) # 'pad' controls the spacing between the ticks and their labels

    # Generate and save the plot
    output_file = f"Output/Plot_{input_file.split('/')[-1].replace('.txt', '.pdf')}"
    plt.savefig(output_file, bbox_inches='tight')
    print(f"Saved: {output_file}")

    plt.close()

# Generate and save the color bar
colors = cmap(np.arange(cmap.N))
fig, ax = plt.subplots(1, figsize=(6, 2), subplot_kw=dict(xticks=[], yticks=[]))
ax.set(frame_on=False)
ax.imshow([colors], extent=[0, 10, 2, 0.5])
xmarks = [0, 5, 10]
ax.set_xticks(xmarks)
ax.set_xticklabels(['Low', 'Normal', 'High'], fontsize=40, fontweight='bold')

plt.savefig('Output/cbar.pdf', bbox_inches='tight')

