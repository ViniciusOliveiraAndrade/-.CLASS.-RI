#Extraia o arquivo "Solr.zip no disco "C:/".
#Abra o "CMD" na mesma pasta que este arquivo e siga os comandos abaixo.
 
#Star Solr on port 8983
> cd Solr/bin
> solr start -p 8983

#Create the Cores
> solr create -c core_Nstop_Nstem -d c:/Solr/Cores/core_Nstop_Nstem
> solr create -c core_stop_Nstem -d c:/Solr/Cores/core_stop_Nstem
> solr create -c core_Nstop_stem -d c:/Solr/Cores/core_Nstop_stem
> solr create -c core_stop_stem -d c:/Solr/Cores/core_stop_stem

#Restar Solr on port 8983
> solr restart -p 8983

#Após terminar os comandos, basta indexar o documento "eq10-wifi_call.json" em todos os cores criados.

Before running the avaliacao.py, you must install ‘requests’ library for python by running the commands on CMD:
	> pip install requests
