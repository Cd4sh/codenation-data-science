#!/usr/bin/env python
# coding: utf-8

# # Desafio 6
# 
# Neste desafio, vamos praticar _feature engineering_, um dos processos mais importantes e trabalhosos de ML. Utilizaremos o _data set_ [Countries of the world](https://www.kaggle.com/fernandol/countries-of-the-world), que contém dados sobre os 227 países do mundo com informações sobre tamanho da população, área, imigração e setores de produção.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Setup_ geral

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import sklearn as sk


from sklearn.feature_extraction.text import (
    CountVectorizer, TfidfTransformer, TfidfVectorizer
)
from sklearn.preprocessing import (KBinsDiscretizer, 
                                   OneHotEncoder, StandardScaler)

from sklearn.datasets import fetch_20newsgroups


# In[2]:


# Algumas configurações para o matplotlib.
#%matplotlib inline

from IPython.core.pylabtools import figsize


figsize(12, 8)

sns.set()


# In[3]:


countries = pd.read_csv("countries.csv")


# In[4]:


new_column_names = [
    "Country", "Region", "Population", "Area", "Pop_density", "Coastline_ratio",
    "Net_migration", "Infant_mortality", "GDP", "Literacy", "Phones_per_1000",
    "Arable", "Crops", "Other", "Climate", "Birthrate", "Deathrate", "Agriculture",
    "Industry", "Service"
]

countries.columns = new_column_names

countries.head(5)


# ## Observações
# 
# Esse _data set_ ainda precisa de alguns ajustes iniciais. Primeiro, note que as variáveis numéricas estão usando vírgula como separador decimal e estão codificadas como strings. Corrija isso antes de continuar: transforme essas variáveis em numéricas adequadamente.
# 
# Além disso, as variáveis `Country` e `Region` possuem espaços a mais no começo e no final da string. Você pode utilizar o método `str.strip()` para remover esses espaços.

# ## Inicia sua análise a partir daqui

# In[26]:


# Sua análise começa aqui.
countries['Region'] = countries['Region'].str.strip()
countries['Country'] = countries['Country'].str.strip()

n_column = [
    "Population", "Area", "Pop_density", "Coastline_ratio",
    "Net_migration", "Infant_mortality", "GDP", "Literacy", "Phones_per_1000",
    "Arable", "Crops", "Other", "Climate", "Birthrate", "Deathrate", "Agriculture",
    "Industry", "Service"
]

df = []

for col in countries:
    commadot = countries[col].astype(str).str.replace(',', '.')
    nnan = commadot.astype(str).replace('nan', np.nan)
    df.append(nnan)

df = pd.DataFrame(df).T

df[n_column] = df[n_column].astype(float)


categories = ['sci.electronics', 'comp.graphics', 'rec.motorcycles']
newsgroups = fetch_20newsgroups(subset="train", categories=categories, shuffle=True, random_state=42)


count = CountVectorizer()


# ## Questão 1
# 
# Quais são as regiões (variável `Region`) presentes no _data set_? Retorne uma lista com as regiões únicas do _data set_ com os espaços à frente e atrás da string removidos (mas mantenha pontuação: ponto, hífen etc) e ordenadas em ordem alfabética.

# In[36]:


def q1():
    # Retorne aqui o resultado da questão 1.
    # pass
    
    return list(np.sort(df['Region'].drop_duplicates()))


# ## Questão 2
# 
# Discretizando a variável `Pop_density` em 10 intervalos com `KBinsDiscretizer`, seguindo o encode `ordinal` e estratégia `quantile`, quantos países se encontram acima do 90º percentil? Responda como um único escalar inteiro.

# In[7]:


def q2():
    # Retorne aqui o resultado da questão 2.
    # pass
    pop_density = pd.DataFrame(df['Pop_density'])
    
    disc = KBinsDiscretizer(n_bins=10, encode="ordinal", strategy="quantile")
    disc.fit(pop_density)

    sbins = disc.transform(pop_density)

    abv = df[sbins >= 9]['Country']

    return abv.size


# # Questão 3
# 
# Se codificarmos as variáveis `Region` e `Climate` usando _one-hot encoding_, quantos novos atributos seriam criados? Responda como um único escalar.

# In[8]:


def q3():
    # Retorne aqui o resultado da questão 3.
    # pass

    return int(pd.get_dummies(countries[['Region', 'Climate']].fillna('NaN')).shape[1])


# ## Questão 4
# 
# Aplique o seguinte _pipeline_:
# 
# 1. Preencha as variáveis do tipo `int64` e `float64` com suas respectivas medianas.
# 2. Padronize essas variáveis.
# 
# Após aplicado o _pipeline_ descrito acima aos dados (somente nas variáveis dos tipos especificados), aplique o mesmo _pipeline_ (ou `ColumnTransformer`) ao dado abaixo. Qual o valor da variável `Arable` após o _pipeline_? Responda como um único float arredondado para três casas decimais.

# In[9]:


test_country = [
    'Test Country', 'NEAR EAST', -0.19032480757326514,
    -0.3232636124824411, -0.04421734470810142, -0.27528113360605316,
    0.13255850810281325, -0.8054845935643491, 1.0119784924248225,
    0.6189182532646624, 1.0074863283776458, 0.20239896852403538,
    -0.043678728558593366, -0.13929748680369286, 1.3163604645710438,
    -0.3699637766938669, -0.6149300604558857, -0.854369594993175,
    0.263445277972641, 0.5712416961268142
]


# In[10]:


def q4():
    # Retorne aqui o resultado da questão 4.
    pass


# ## Questão 5
# 
# Descubra o número de _outliers_ da variável `Net_migration` segundo o método do _boxplot_, ou seja, usando a lógica:
# 
# $$x \notin [Q1 - 1.5 \times \text{IQR}, Q3 + 1.5 \times \text{IQR}] \Rightarrow x \text{ é outlier}$$
# 
# que se encontram no grupo inferior e no grupo superior.
# 
# Você deveria remover da análise as observações consideradas _outliers_ segundo esse método? Responda como uma tupla de três elementos `(outliers_abaixo, outliers_acima, removeria?)` ((int, int, bool)).

# In[34]:


def q5():
    # Retorne aqui o resultado da questão 4.
    # pass
    netMigration = df['Net_migration']

    quant1 = netMigration.quantile(0.25)
    quant3 = netMigration.quantile(0.75)
    iqr = quant3 - quant1

    interval = [quant1 - 1.5 * iqr, quant3 + 1.5 * iqr]

    upperGroup = (netMigration > interval[1])
    lowerGroup = (netMigration < interval[0])

    return tuple([int(lowerGroup.sum()), int(upperGroup.sum()), False])


# ## Questão 6
# Para as questões 6 e 7 utilize a biblioteca `fetch_20newsgroups` de datasets de test do `sklearn`
# 
# Considere carregar as seguintes categorias e o dataset `newsgroups`:
# 
# ```
# categories = ['sci.electronics', 'comp.graphics', 'rec.motorcycles']
# newsgroup = fetch_20newsgroups(subset="train", categories=categories, shuffle=True, random_state=42)
# ```
# 
# 
# Aplique `CountVectorizer` ao _data set_ `newsgroups` e descubra o número de vezes que a palavra _phone_ aparece no corpus. Responda como um único escalar.

# In[27]:


def q6():
    # Retorne aqui o resultado da questão 4.
    # pass    
    countd = count.fit_transform(newsgroups.data)
    
    words = [count.vocabulary_.get(f"{word.lower()}") for word in [u"phone"]]

    return int(countd[:, words].toarray().sum())


# ## Questão 7
# 
# Aplique `TfidfVectorizer` ao _data set_ `newsgroups` e descubra o TF-IDF da palavra _phone_. Responda como um único escalar arredondado para três casas decimais.

# In[32]:


def q7():
    # Retorne aqui o resultado da questão 4.
    # pass
    tfidf = TfidfVectorizer()
    tfidfd = tfidf.fit_transform(newsgroups.data)

    words = sorted([count.vocabulary_.get(f"{word.lower()}") for word in [u"phone"]])

    return float(round(tfidfd[:, words].toarray().sum(), 3))


# In[ ]:




