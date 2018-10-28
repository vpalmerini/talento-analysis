import pandas as pd
from fuzzywuzzy import fuzz, process

# dataframe
df = pd.read_csv('MailingTalento2018.csv', usecols=['profile.full_name', 'profile.email', 'application.phone', 'application.school', 'application.course', 'application.enroll_year', 'application.cv', 'application.cv2'])

# renaming columns
df = df.rename(index=str, columns={'profile.full_name':'NomeCompleto', 'profile.email':'Email', 'application.phone':'Telefone', 'application.school':'Faculdade', 'application.course':'Curso', 'application.enroll_year':'AnoDeEntrada', 'application.cv':'Currículo1', 'application.cv2':'Currículo2'})

# drop null values
df = df.dropna(subset=['NomeCompleto', 'Email', 'Curso'])

# remove duplicates
df = df.drop_duplicates(subset=['Email'], keep='first')

# reordering columns
df = df[['NomeCompleto', 'Email', 'Telefone','Currículo1', 'Currículo2', 'AnoDeEntrada', 'Curso', 'Faculdade']]

courses = 	['Administração', 
			'Análise de Sistemas', 
			'Arquitetura',
			'Artes Cênicas',
			'Artes Visuais',
			'Biologia',
			'Biomedicina',
			'Ciência da Computação',
			'Ciências Contábeis',
			'Ciências Econômicas',
			'Ciência Sociais',
			'Comunicação',
			'Dança',
			'Design',
			'Direito',
			'Economia',
			'Educação Física',
			'Enfermagem',
			'Engenharia Agrícola',
			'Engenharia Ambiental',
			'Engenharia Civil',
			'Engenharia da Computação',
			'Engenharia de Controle e Automação',
			'Engenharia de Manufatura',
			'Engenharia de Materiais',
			'Engenharia de Produção',
			'Engenharia de Software',
			'Engenharia Elétrica',
			'Engenharia Física',
			'Engenharia Mecânica',
			'Engenharia Química',
			'Estatística',
			'Farmácia',
			'Filosofia'
			'Física',
			'Fisioterapia',
			'Fonoaudiologia',
			'Geografia',
			'Geologia',
			'História',
			'Jornalismo',
			'Letras',
			'Linguística',
			'Logística',
			'Marketing',
			'Matemática',
			'Medicina',
			'Medicina Veterinária',
			'Midialogia',
			'Moda',
			'Música',
			'Nutrição',
			'Odontologia',
			'Pedagogia',
			'Psicologia',
			'Publicidade e Propaganda',
			'Química',
			'Relações Internacionais',
			'Relações Públicas',
			'Sistemas de Informação'
			]

# string matching - courses
for i in range(len(df['Curso'])):
	for course in courses:
		if (fuzz.token_set_ratio(course, df['Curso'][i]) > 90):
			df['Curso'][i] = course



universities =	['Unicamp',
				'USP',
				'Unesp',
				'Mackenzie',
				'PUCCAMP',
				'FACAMP',
				'ESAMC',
				'FATEC',
				'FGV',
				'ITA',
				'PUC',
				'UFSCAR',
				]

# string matching - universities
for i in range(len(df['Faculdade'])):
	for university in universities:
		if (fuzz.token_set_ratio(university, df['Faculdade'][i]) > 90):
			df['Faculdade'][i] = university


# export to csv
df.to_csv('Cleaned/CSV/MailingTalento2018.csv', encoding='utf-8')