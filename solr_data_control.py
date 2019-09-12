import plotly.graph_objects as go
import requests
import json
import csv

def generate_matriz_relevancia (json_source, matriz_directory = "matriz_relevancia.csv"):
    with open(json_source,"r") as arq_json:
        data = json.load(arq_json);

    with open(matriz_directory, mode='w', encoding='utf-8',newline='') as arq_csv:
        writer = csv.writer(arq_csv)
        writer.writerow(["#","key","summary","description","query 1","query 2"])
        for i,d in enumerate(data):
            writer.writerow([str(i+1),d["key"],d["summary"],str(d["description"]).strip().replace("\n\n","\n").replace("\n \n","\n").replace("\n\n\n","\n")])

def generate_url(core,query):
    server = "http://localhost:8983/solr/"
    pre_query = "/select?q="
    pos_query = "&rows=100"
    return server + core + pre_query + query + pos_query

def get_data_from_solr(cores,querys):
    r = {}
    for core in cores:
        r.update({core:{}})
        for query in querys:
            r[core].update({query:[]})
            solr_url = generate_url(core,query)
            results = requests.get(solr_url).json()
            for docs in results["response"]["docs"]:
                r[core][query].append(docs["key"])
    return r

def get_matriz_data(directory,querys):
    m = {}
    for query in querys:
        m.update({query:[]})
        with open(directory) as arquivocsv: 
            ler = csv.DictReader(arquivocsv, delimiter=",")
            for linha in ler:
                if linha[query] == "1" or linha[query] == 1:
                    m[query].append(linha['key'])
    return m

def analyze_accuracy_coverage(cores,querys,return_core,matriz_relevancia):
    # Precisao = total de relevantes recuperados / numero total de recuperados
    # Cobertura = total de relevantes recuperados / numero total de relevantes
    precisoes = {}
    coberturas = {}
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
    return precisoes,coberturas 

def print_graphs(precisoes,coberturas,cores,querys):
    fig = None
    for core in cores:
        print("INICIO: " +core)
        fig = go.Figure()

        for query in querys:
            print("INICIO: " +query)
            x = coberturas[core][query]
            fig.add_trace(go.Scatter(
                x=x,
                y=precisoes[core][query],
                name = "Core: "+core+" Query: "+query,
                connectgaps=True
            ))
            print("FIM: " +query)
        
        fig.update_layout(
            title=go.layout.Title(
                text="Core",
                xref="paper",
                x=0
            ),
            xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                    text="Coverage",
                    font=dict(
                        family="Courier New, monospace",
                        size=18,
                        color="#7f7f7f"
                    )
                )
            ),
            yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                    text="Accuracy",
                    font=dict(
                        family="Courier New, monospace",
                        size=18,
                        color="#7f7f7f"
                    )
                )
            )
        )
        
        fig.show()
        print("FIM: " +core)
        fig = None    

