import solr_data_control as sdc

cores = ["core_Nstop_Nstem","core_Nstop_stem","core_stop_Nstem","core_stop_stem"]
querys = ["enabling wifi it does not connect","no audio is heard on calling"]

return_core = sdc.get_data_from_solr(cores,querys)

matriz_relevancia = sdc.get_matriz_data("matriz_relevancia.csv",querys)

precisoes,coberturas = sdc.analyze_accuracy_coverage(cores,querys,return_core,matriz_relevancia)

sdc.print_graphs(precisoes,coberturas,cores,querys)