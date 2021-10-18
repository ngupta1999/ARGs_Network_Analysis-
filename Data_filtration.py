import pandas as pd
a=pd.read_table("unigenes.csv", sep=",").          #
b=pd.read_table("GMGC10.card_resfam.tsv", header=1)
file = pd.read_table("GMBC10.meta.tsv")
file = file[file['genome'].str.contains(*sample_id_from df*)]

#chunk was used to read the 64gb GMGC file
for chunk in pd.read_table("GMGC10.GMBC10.tsv", chunksize =10000000):
    print(chunk)
gupta= chunk[chunk['Genome_Bin'].str.contains('GMBC10.063_230|GMBC10.081_232|GMBC10.093_198|GMBC10.005_224|GMBC10.043_046|GMBC10.049_847|GMBC10.063_644|GMBC10.091_927|GMBC10.101_151|GMBC10.101_565|GMBC10.077_912|GMBC10.038_297|GMBC10.091_977|GMBC10.147_451|GMBC10.065_119|GMBC10.026_520|GMBC10.077_211|GMBC10.082_271|GMBC10.088_049|GMBC10.088_956|GMBC10.092_199|GMBC10.062_308|GMBC10.078_037|GMBC10.039_427|GMBC10.066_728|GMBC10.049_345|GMBC10.120_189|GMBC10.005_350|GMBC10.022_881|GMBC10.029_983|GMBC10.044_164|GMBC10.045_684|GMBC10.049_176|GMBC10.070_376|GMBC10.079_242|GMBC10.090_952|GMBC10.091_300|GMBC10.028_353|GMBC10.064_544|GMBC10.065_212|GMBC10.075_944|GMBC10.114_977|GMBC10.147_450|')]
d=pd.read_table("GMGC10.card_resfam.tsv")
d.columns 

#maps unigenes in both the files
e=pd.merge(a,  b, left_on='Unigene', right_on="#Unigene", how='inner')  

#filters only Genome Bins and AROs column 
f=e[['Genome_Bin', 'AROs']]

#saves f to the local device 
f.to_csv("AROs_file.csv")
