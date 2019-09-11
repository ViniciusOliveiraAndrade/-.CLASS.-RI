import plotly.graph_objects as go
import requests
import json
import csv

def genarete_url(c,q):
    server = "http://localhost:8983/solr/"
    query = "/select?q="
    return server + c + query + q

def get_data(cores,querys):
    r = {}
    for core in cores:
        r.update({core:{}})
        for query in querys:
            r[core].update({query:[]})
            solr_url = genarete_url(core,query)
            results = requests.get(solr_url).json()
            for docs in results["response"]["docs"]:
                r[core][query].append(docs["key"])
    return r

def genarete_matriz(directory,querys):
    m = {}
    for query in querys:
        m.update({query:[]})
        with open(directory) as arquivocsv: 
            ler = csv.DictReader(arquivocsv, delimiter=",")
            for linha in ler:
                if linha[query] == "1" or linha[query] == 1:
                    m[query].append(linha['key'])
    return m

cores = ["core_Nstop_Nstem","core_Nstop_stem","core_stop_Nstem","core_stop_stem"]
querys = ["enabling wifi it does not connect","no audio is heard on calling"]

return_core = get_data(cores,querys)
matriz_relevancia = genarete_matriz("Matriz.csv",querys)

# Precisao = total de relevantes recuperados / numero total de recuperados
# Cobertura = total de relevantes recuperados / numero total de relevantes
coberturas = {}
precisoes = {}

for core in cores:
    coberturas.update({core:{}})
    precisoes.update({core:{}})
    for query in querys:
        coberturas[core].update({query:[]})
        precisoes[core].update({query:[]})
        qt = 0
        for i,key in enumerate(return_core[core][query]):
            if key in matriz_relevancia[query]:
                qt = qt + 1
            coberturas[core][query].append(qt /  len(matriz_relevancia[query]))
            precisoes[core][query].append(qt / (i+1))
            
            
        qt = 0        

# print("Total de retorno: "+return_core[])
print("Coberturas")
print(coberturas)
print("-------"*20)
print("Precisoes")
print(precisoes)



x = coberturas[cores[2]][querys[0]]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=precisoes[cores[2]][querys[0]],
    name = querys[0],
    connectgaps=True
))



fig.show()


print (matriz_relevancia)