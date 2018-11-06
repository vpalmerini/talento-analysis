import pandas as pd
from fuzzywuzzy import fuzz, process

# dataframe
df = pd.read_csv('MailingTalento2018.csv', usecols=['profile.full_name', 'profile.email', 'application.phone', 'application.school', 'application.course', 'application.enroll_year', 'application.cv', 'application.cv2'])

# renaming columns
df = df.rename(index=str, columns={
								   'application.can_move':'Pode se mudar',
								   'application.education':'Escolaridade',
								   'application.english_level':'Inglês',
								   'application.excel_level':'Excel',
								   'application.extra_courses':'Cursos Extras',
								   'application.first_timer':'Primeira Vez',
								   'application.gender':'Gênero',
								   'application.interests':'Interesses',
								   'application.other_languages':'Outros Idiomas',
								   'application.referrer':'Referência',
								   'application.state':'Estado',
								   'profile.state':'Status',
								   'profile.full_name':'NomeCompleto',
								   'application.age':'Idade',
								   'profile.email':'Email', 
								   'application.phone':'Telefone',
								   'application.city':'Cidade',
								   'application.country':'País',
								   'application.school':'Faculdade', 
								   'application.course':'Curso', 
								   'application.enroll_year':'AnoDeEntrada', 
								   'application.cv':'Currículo1', 
								   'application.cv2':'Currículo2'})

# drop null values
df = df.dropna(subset=['NomeCompleto', 'Email', 'Curso'])

# remove duplicates
df = df.drop_duplicates(subset=['Email'], keep='first')

# reordering columns
df = df[['NomeCompleto', 
		 'Email', 
		 'Telefone', 
		 'Idade', 
		 'Gênero', 
		 'Escolaridade',
		 'Currículo1', 
		 'Currículo2', 
		 'AnoDeEntrada', 
		 'Curso', 
		 'Faculdade',
		 'Cidade',
		 'Estado',
		 'País',
		 'Inglês',
		 'Excel',
		 'Cursos Extras',
		 'Outros Idiomas',
		 'Interesses',
		 'Pode se mudar',
		 'Primeira Vez',
		 'Referência',
		 'Status'
		 ]]


# string matching - courses
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

for i in range(len(df['Curso'])):
	for course in courses:
		if (fuzz.token_set_ratio(course, df['Curso'][i]) > 90):
			df['Curso'][i] = course



# string matching - universities
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

for i in range(len(df['Faculdade'])):
	for university in universities:
		if (fuzz.token_set_ratio(university, df['Faculdade'][i]) > 90):
			df['Faculdade'][i] = university


# string matching - cities
cities = ['Campinas',
		  'São Paulo',
		  'Limeira',
		  'São Carlos',
		  'Bauru',
		  'São José dos Campos',
		  'Piracicaba',
		  'Jundiaí',
		]

for i in range(len(df['Cidade'])):
	for city in cities:
		if (fuzz.token_set_ratio(city, df['Cidade'][i]) > 90):
			df['Cidade'][i] = city


# string matching - referrers
referrers = ['Facebook',
			 'Email',
			 'Amigos'
			 'Unicamp',
			 'Universidade'
		]

for i in range(len(df['Referência'])):
	for referrer in referrers:
		if (fuzz.token_set_ratio(referrer, df['Referência'][i]) > 90):
			df['Referência'][i] = referrer


# Data Analysis
# subscription data
total = len(df)
subscribed = len(df.loc[df['Idade'].notna() == True])
checkedin = len(df.loc[df['Status'] == 'checkedin'])

# Visitors data
# age
# remove weird values
age = df.loc[df['Idade'] < 75]
# get the average
age_avg = age.mean()['Idade']

# gender
male = len(df.loc[df['Gênero'] == 'M'])
female = len(df.loc[df['Gênero'] == 'F'])

# cities
cities = df.groupby('Cidade').size()
cities = cities.sort_values(ascending=False)
cities_top10 = cities[:10]

# first time as Talento's visitor
first_time = len(df.loc[df['Primeira Vez'] == 'True'])
not_first_time = total - first_time

# referrer
facebook = len(df.loc[df['Referência'] == 'Facebook'])
email = len(df.loc[df['Referência'] == 'Email'])
friends = len(df.loc[df['Referência'] == 'Amigos'])
others = total - (facebook + email + friends)

# main courses
courses = df.groupby('Curso').size()
courses = courses.sort_values(ascending=False)
courses_top10 = courses[:10]

# enroll year
enroll_year = df.groupby('AnoDeEntrada').size()
enroll_year = enroll_year.sort_values(ascending=False)
enroll_year_top5 = enroll_year[:5]

# universities
universities = df.groupby('Faculdade').size()
universities = universities.sort_values(ascending=False)
universities_top10 = universities[:10]

# english level
basic_english = len(df.loc[df['Inglês'] == 'basic'])
intermediate_english = len(df.loc[df['Inglês'] == 'intermediate'])
advanced_english = len(df.loc[df['Inglês'] == 'advanced'])

# excel level
basic_excel = len(df.loc[df['Excel'] == 'basic'])
intermediate_excel = len(df.loc[df['Excel'] == 'intermediate'])
advanced_excel = len(df.loc[df['Excel'] == 'advanced'])

# education
undergraduate = len(df.loc[df['Escolaridade'] == 'Graduação'])
masters = len(df.loc[df['Escolaridade'] == 'Mestrado'])
phd = len(df.loc[df['Escolaridade'] == 'Doutorado'])
high = len(df.loc[df['Escolaridade'] == 'Ensino Médio'])
elementary = len(df.loc[df['Escolaridade'] == 'Ensino Fundamental'])

# resumé
one_resume = len(df.loc[df['Currículo1'].notna() == True])
two_resume = len(df.loc[df['Currículo2'].notna() == True])



# Visitors that have done checkin
checkedin = df.loc[df['Status'] == 'checkedin']
total = len(checkedin)
# age
# remove weird values
age = checkedin.loc[checkedin['Idade'] < 75]
# get the average
age_avg = age.mean()['Idade']

# gender
male = len(checkedin.loc[checkedin['Gênero'] == 'M'])
female = len(checkedin.loc[checkedin['Gênero'] == 'F'])

# cities
cities = checkedin.groupby('Cidade').size()
cities = cities.sort_values(ascending=False)
cities_top10 = cities[:10]

# first time as Talento's visitor
first_time = len(checkedin.loc[checkedin['Primeira Vez'] == 'True'])
not_first_time = total - first_time

# referrer
facebook = len(checkedin.loc[checkedin['Referência'] == 'Facebook'])
email = len(checkedin.loc[checkedin['Referência'] == 'Email'])
friends = len(checkedin.loc[checkedin['Referência'] == 'Amigos'])
others = total - (facebook + email + friends)

# main courses
courses = checkedin.groupby('Curso').size()
courses = courses.sort_values(ascending=False)
courses_top10 = courses[:10]

# enroll year
enroll_year = checkedin.groupby('AnoDeEntrada').size()
enroll_year = enroll_year.sort_values(ascending=False)
enroll_year_top5 = enroll_year[:5]

# universities
universities = checkedin.groupby('Faculdade').size()
universities = universities.sort_values(ascending=False)
universities_top10 = universities[:10]

# english level
basic_english = len(checkedin.loc[checkedin['Inglês'] == 'basic'])
intermediate_english = len(checkedin.loc[checkedin['Inglês'] == 'intermediate'])
advanced_english = len(checkedin.loc[checkedin['Inglês'] == 'advanced'])

# excel level
basic_excel = len(checkedin.loc[checkedin['Excel'] == 'basic'])
intermediate_excel = len(checkedin.loc[checkedin['Excel'] == 'intermediate'])
advanced_excel = len(checkedin.loc[checkedin['Excel'] == 'advanced'])

# education
undergraduate = len(checkedin.loc[checkedin['Escolaridade'] == 'Graduação'])
masters = len(checkedin.loc[checkedin['Escolaridade'] == 'Mestrado'])
phd = len(checkedin.loc[checkedin['Escolaridade'] == 'Doutorado'])
high = len(checkedin.loc[checkedin['Escolaridade'] == 'Ensino Médio'])
elementary = len(checkedin.loc[checkedin['Escolaridade'] == 'Ensino Fundamental'])

# resumé
one_resume = len(checkedin.loc[checkedin['Currículo1'].notna() == True])
two_resume = len(checkedin.loc[checkedin['Currículo2'].notna() == True])


# export to csv
df.to_csv('Cleaned/CSV/MailingTalento2018.csv', encoding='utf-8')