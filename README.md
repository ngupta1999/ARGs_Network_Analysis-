# Exploration of co-occurrence patterns of antibiotic resistance genes from metagenome assembled genomes from wastewater samples
Exploration of co-occurrence patterns of ARGs from MAGs from wastewater samples
## Data
Data was downloaded from [GMGC](https://git.embl.de/coelho/GMGC10.data)
#### Installiing Git_Annex
Run the following command


    conda create -n gmgc.data
    conda install -c conda-forge git-annex

#### Getting Data
     
     
     Git-annex get “file_name”

## Workflow
1. Use the sample metadata(metadata/GMGC10.sample.meta.tsv.gz) to get a list of wastewater sapmles. 
File: 

