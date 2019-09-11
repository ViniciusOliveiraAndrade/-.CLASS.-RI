# This is a framework made to use Solr in the RI Class

## Requirements

This Framework needs the Python version 3.7.* , "plotly" version 0.4.0 and "requests"   libraries  for Python, and Solr version 7.3.1.


## Setup

#### Python

Install Python 3.7.* from:

> "https://www.python.org/downloads/".

Upadate the pip by:

> pip install --upgrade pip

Install the libraries that are listed in the "requirements.txt" by:

> pip install -r requirements.txt


#### Solr

Download the zip file of the Solr 7.3.1 from:

> https://archive.apache.org/dist/lucene/solr/

Unzip the file in the same directory of this file and rename the folder from "solr-7.3.1" to "Solr".
Open the "CMD" at this directory and follow the below commands.
 

###### Star Solr on port 8983

> cd Solr/bin

> solr start -p 8983


###### Create the Cores

> solr create -c core_Nstop_Nstem -d ../../Cores/core_Nstop_Nstem

> solr create -c core_stop_Nstem -d ../../Cores/core_stop_Nstem

> solr create -c core_Nstop_stem -d ../../Cores/core_Nstop_stem

> solr create -c core_stop_stem -d ../../Cores/core_stop_stem


###### Restar Solr on port 8983
> solr restart -p 8983

##### After the solr restart index the documentos manually on each core you want to be indexed.

## Code

