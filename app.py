from flask import Flask 
app = Flask(__name__)

@app.route("/")


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
    </body>
    </html>"
