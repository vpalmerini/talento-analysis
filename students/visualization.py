import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from fuzzywuzzy import fuzz, process


# load dataset
df = pd.read_csv('MailingTalento2018Cleaned.csv')


# if you want only checkedin visitor data
# df = df.loc[df['Status'] == 'checkedin']


# set the plot background to white
sns.set(style='whitegrid')


# age
age = df['Idade']
ax = sns.countplot(x='Idade', data=age)
plt.show()


# gender
labels = 'M', 'F'
M = df.loc[df['Gênero'] == 'M']
F = df.loc[df['Gênero'] == 'F']
sizes = [len(M), len(F)]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',startangle=90, colors=['#009FB7', '#912F40'])
ax1.axis('equal')
plt.show()


# cities
ax = sns.countplot(y='Cidade', data=df, order=df['Cidade'].value_counts().index[:10])


# courses
ax = sns.countplot(y='Curso', data=df, order=df['Curso'].value_counts().index[:10])


# enroll year
ax = sns.countplot(y='AnoDeEntrada', data=df, order=df['AnoDeEntrada'].value_counts().index[:5])


# universities
ax = sns.countplot(y='Faculdade', data=df, order=df['Faculdade'].value_counts().index[:10])


# english level
labels = ['Básico', 'Intermediário', 'Avançado']
basico = df.loc[df['Inglês'] == 'basic']
intermediario = df.loc[df['Inglês'] == 'intermediate']
avancado = df.loc[df['Inglês'] == 'advanced']
sizes = [len(basico), len(intermediario), len(avancado)]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#58A4B0', '#FA9F42', '#6CC551'])
ax1.axis('equal')


# excel level
labels = ['Básico', 'Intermediário', 'Avançado']
basico = df.loc[df['Excel'] == 'basic']
intermediario = df.loc[df['Excel'] == 'intermediate']
avancado = df.loc[df['Excel'] == 'advanced']
sizes = [len(basico), len(intermediario), len(avancado)]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#58A4B0', '#FA9F42', '#6CC551'])
ax1.axis('equal')

# referencies
ax = sns.countplot(y='Referência', data=df, order=df['Referência'].value_counts().index[:5])


# education
df = df.loc[df['Escolaridade'] != '']
df = df.loc[df['Escolaridade'] != 'Brazil']
df = df.loc[df['Escolaridade'] != 'Ensino Fundamental']
ax = sns.countplot(y='Escolaridade', data=df, order=df['Escolaridade'].value_counts().index[:5])


# companies
labels = ['Financeiro', 'Consultoria', 'Indústria', 'Assessoria/Recrutamento']
sizes = [1, 5, 27, 5]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#58A4B0', '#FA9F42', '#6CC551', '#F1BF98'])
ax1.axis('equal')


# first time?
labels = ['Sim', 'Não']
sim = df.loc[df['Primeira Vez'] == True]
nao = df.loc[df['Primeira Vez'] == False]
sizes = [len(sim), len(nao)]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',startangle=90, colors=['#FA9F42', '#58A4B0'])
ax1.axis('equal')
plt.show()
