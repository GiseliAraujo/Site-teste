from flask import Flask 
app = Flask(__name__)
@app.route("/")

import requests
from bs4 import BeautifulSoup
import pandas as pd


def obter_noticias_folha():
    site_Folha = requests.get('https://www1.folha.uol.com.br/ultimas-noticias/')
    bs = BeautifulSoup(site_Folha.content,'html.parser')

    noticias = bs.find_all('div', 'c-headline__content')
    ultimas_noticias = []
    for n in noticias:
        Link = n.find('a')['href']
        Manchete = n.find('h2').text
        Data = n.find('time')['datetime']
        ultimas_noticias.append({'Manchete': Manchete, 'Link': Link, 'Data': Data})

    ultimas_folha = pd.DataFrame(ultimas_noticias)
    return ultimas_folha



def hello_world():
  return "<!DOCTYPE html>
<html>
<head>
	<title>Exemplo de tabela HTML com resultados de função Python</title>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.9.6/brython.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.9.6/brython_stdlib.min.js"></script>
	<script type="text/python" src="exemplo.py"></script>
</head>
<body onload="preencherTabela()">
	<h1>Últimas notícias</h1>
	<table id="tabela_noticias">
		<thead>
			<tr>
				<th>Manchete</th>
				<th>Link</th>
				<th>Data</th>
			</tr>
		</thead>
		<tbody>
		</tbody>
	</table>
	<script>
		function preencherTabela() {
			// Chamar a função Python e obter os resultados
			var noticias = obter_noticias_folha();

			// Obter a referência da tabela HTML
			var tabela = document.getElementById('tabela_noticias');

			// Preencher a tabela com os resultados
			for (var i = 0; i < noticias.length; i++) {
				var linha = tabela.insertRow();
				var colunaManchete = linha.insertCell();
				var colunaLink = linha.insertCell();
				var colunaData = linha.insertCell();

				colunaManchete.innerHTML = noticias[i].Manchete;
				colunaLink.innerHTML = '<a href="' + noticias[i].Link + '">' + noticias[i].Link + '</a>';
				colunaData.innerHTML = noticias[i].Data;
			}
		}
	</script>
</body>
</html>"
