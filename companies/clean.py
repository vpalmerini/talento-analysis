import pandas as pd
from google import google

# dataframe
df = pd.read_csv('Empresas.csv')

# drop null values of 'Empresa' column
df = df.dropna(subset=['Empresa'])

# drop null values of 'Telefone' and 'Email'
df = df.dropna(subset=['Telefone', 'Email'], how='all')

# remove duplicates of 'Email' column
df = df.drop_duplicates(subset=['Email'], keep='first')


# filling the website column
num_page = 1
for i in range(len(df)):
	try:
		search_results = google.search(df['Empresa'][i], num_page)
		df.at['Site', i] = str(search_results[0].link)
		print(search_results[0].link)
	else:
		df.at['Site', i] = 'Site não encontrado'

filling the LinkedIn column
for i in range(len(df)):
	search_results = google.search(df['Empresa'][i], num_page)
	df['LinkedIn'][i] = search_results[0].link


# defining if the company have already participated of any Talento edition
COMPANY_PARTICIPATED = (
	'99 Táxis',
	'Accenture',
	'Aiesec',
	'Arcor',
	'Astra',
	'BIC'
	'BTC',
	'Caterpillar',
	'Companhia de Estágios',
	'Companhia de Talentos',
	'CIEE',
	'Cielo',
	'CNPEM',
	'Conductor',
	'Cooper Standard',
	'CPFL',
	'Deloitte',
	'Dow',
	'Duratex',
	'Eldorado',
	'EMS',
	'Ensina Brasil',
	'Everis',
	'Faurecia',
	'Flex',
	'GE',
	'Gradus',
	'GymPass',
	'Henkel',
	'Honda',
	'Itaú',
	'KraftHeinz'
	'Mars',
	'Microsoft',
	'Motorola',
	'Natura',
	'P&G',
	'Porto Seguro',
	'Raízen',
	'Rhodia'
	'Royal Canin',
	'Saint Gobain',
	'Santander',
	'Schaeffler',
	'Suzano'
	'Tetra Pak',
	'Maker Factory',
	'Halge',
	'Wall Jobs',
	'DHL',
	'Roca Brasil',
	'Villares Metals',
	'AgroPalma',
	'TE Connectivity',
	'West Rock',
	'A.T. Kearney',
	'AmstedMaxion',
	'CI&T',
	'CITI',
	'DPaschoal',
	'Falconi',
	'Kurita',
	'Movile',
	'Shell',
	'Ultra',
	'Experimento',
	'Monsanto',
	'Oracle',
	'Ambev',
	'International Paper',
	'AkzoNobel',
	'MWV',
	'Bosch',
	'Avon',
	'UL',
	'Elekeiroz',
	'Denso',
	'All Logística',
	'Embraer',
	'iFood',
	'3M',
	'SG4 Soluções',
	'Provider',
	'John Deere',
	'Viva Real',
	'BorgWarner',
	'Sensedia',
	'ADTsys',
	'Loreal',
	'Ypê',
	'Mazak',
	'Valeo',
	'CPQD',
	'Cargill',
	'Oxiteno',
	'IEL',
	'Cummins',
	'Eaton',
	'Integration Consulting',
	'EF Intercâmbio',
	'Andrade Gutierrez',
	'Medley',
	'KPMG',
	'Maxion Wheels',
	'Reckitt Benckiser',
	'Daitan'
)


# filling the field 'Já participou da Talento?'
for i in range(len(df)):
	if df['Empresa'][i] in COMPANY_PARTICIPATED:
		df['Já Participou da Talento?'] = True
	else:
		df['Já Participou da Talento?'] = False


# export csv
df.to_csv('Cleaned/CSV/Empresas.csv', encoding='utf-8')