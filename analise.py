# -----------------------------------------------------------------------------------------------------------------------------
# Leonardo A Carrilho
# 2021 December
# leo_carrilho@hotmail.com
# OBS1: Antes de rodar, instale: pip3 install opendatasets pandas numpy matplotlib pyjanitor unidecode.
# OBS2: Este script roda diretamente no terminal do Linux CentOS. Não foi usado Jupyter e afins neste trabalho.
#
# Fonte: https://www.xmodulo.com/matplotlib-scientific-plotting-linux.html
# Fonte: https://rogeriopradoj.com/2019/07/14/como-tirar-acentos-de-string-no-python-transliterate-unicodedata-e-unidecode/
# Fonte: https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib
#
# This is a simple analysis script to Uninove's homework
# -----------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3

import os 
import webbrowser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

path = os.getcwd() # Pega o caminho onde o script está rodando

def saida_grafico_linha(titulo_grafico, label_x, label_y, xData, yData2):
	#xData = np.arange(0, 10, 1)
	yData1 = xData.__pow__(2.0)
	#yData2 = np.arange(15, 61, 5)
	plt.figure(num=1, figsize=(8, 6))
	plt.title(f'{titulo_grafico}', size=14)
	plt.xlabel(f'{label_x}', size=14)
	plt.ylabel(f'{label_y}', size=14)
	plt.plot(xData, yData1, color='b', linestyle='--', marker='o', label='y1 data')
	plt.plot(xData, yData2, color='r', linestyle='-', label='y2 data')
	plt.legend(loc='upper left')
	plt.savefig(f"{path}/linha.png", format="png")
	# Abre a figura no browser.
	webbrowser.open(f"{path}/linha.png")

def saida_grafico_histogram():
	mu = 0.0
	sigma = 2.0
	samples = np.random.normal(loc=mu, scale=sigma, size=1000)
	plt.figure(num=1, figsize=(8, 6))
	plt.title('Plot 2', size=14)
	plt.xlabel('value', size=14)
	plt.ylabel('counts', size=14)
	plt.hist(samples, bins=40, range=(-10, 10))
	plt.text(-9, 100, r'$mu$ = 0.0, $sigma$ = 2.0', size=16)
	plt.savefig(f"{path}/histograma.png", format="png")

def saida_grafico_pizza():
	data = [33, 25, 20, 12, 10]
	plt.figure(num=1, figsize=(6, 6))
	plt.axes(aspect=1)
	plt.title('Plot 3', size=14)
	plt.pie(data, labels=('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'))
	plt.savefig(f'{path}/pizza.png', format='png')


df = pd.read_csv(f"{path}/preco-combustivel-2004-2019.csv")
#print(df.info())
#print(df.column)
saida_grafico_linha("Titulo aqui", "label do x", "Label do y", df.loc[:,5], df.loc[:,6])
#plt.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
#plt.plot(df.loc[:,5], df.loc[:,6])
#plt.show()
