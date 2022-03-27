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
1. Use the sample metadata to get a list of wastewater sapmles. 

   **File**: GMGC10.sample.meta.tsv.gz
   
   **Source**: [Sample Metadata](http://gmgc.embl.de/downloads/v1.0/metadata/GMGC10.sample.meta.tsv.gz.metadata/GMGC10.sample.meta.tsv.gz)

2. Filter the genome bins table to get the MAGs from the wastewater samples. 
   
   **File**: GMBC10.meta.tsv

   **Source**: [MAGs](http://gmgc.embl.de/downloads/v1.0/GMBC10.meta.tsv.GMBC10.meta.tsv)
   
3. Filter the MAG <-> Unigene table for only the MAGs identified in step #3 and keep high-quality (>90% complete & <5% contamination) and medium-quality    (>50% complete & <10% contamination) genome bins.

   **File**: GMGC10.GMBC10.tsv.gz

   **Source**: [Unigenes](http://gmgc.embl.de/downloads/v1.0/GMGC10.GMBC10.tsv.gz.GMGC10.GMBC10.tsv.gz)
   
 4. Filter this further to get only the unigenes that are ARGs.
 
    **File**: AROs_file.csv
    
    **Code**: Data_filteration.py
    
5. Map [unigenes to AROs](http://gmgc.embl.de/downloads/v1.0/GMGC10.card_resfam.tsv.gz)
   
   **File**: GMGC10.card_resfam.tsv.gz
   
   **Code**: Data_extraction..ipynb
   
 6. Construct a size matrix denoting the number of common AROs between each pair of genome bins
 
    **File**: AROs_co-occurence.csv 
    
    **Code**: AROs_co-occurence.ipynb
    
 7. Construct a matrix denoting the number of times a pair of ARO occurred in all genome bins
 
    **File**: Genome_bin_matrix.csv
    
    **Code**: Genome_bin_matrix.ipynb
    
 8. Network analysis
      
    **Code**: Network_building.py
