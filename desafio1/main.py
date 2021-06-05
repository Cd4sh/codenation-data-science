#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[31]:



trem = (black_friday['Purchase']-black_friday['Purchase'].mean())
black_friday_std = ( trem / trem.std())

trem = black_friday['Purchase']
black_friday_norm = (trem-trem.min() )/(trem.max()-trem.min())


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[4]:


def q1():
    # Retorne aqui o resultado da questão 1.
    # pass

    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[5]:


def q2():
    f1 = black_friday['Gender']=='F'
    f2 = black_friday['Age']=='26-35'
    # Retorne aqui o resultado da questão 2.
    # pass

    return black_friday[f1 & f2].shape[0]


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    # Retorne aqui o resultado da questão 3.
    # pass
    # black_friday['User_ID'].drop_duplicates().shape[0]

    return black_friday['User_ID'].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    # pass
    
    aux = black_friday.dtypes
    aux = aux.drop_duplicates()
    
    return aux.shape[0]


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    # Retorne aqui o resultado da questão 5.
    # pass
    # aux = black_friday.isna().sum() != 0
    # return float(aux.sum()/black_friday.isna().shape[1])
    
    #usando questão 10
    aux = black_friday.isna().sum()/len(black_friday)

    return float(aux['Product_Category_3'])


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    # Retorne aqui o resultado da questão 6.
    # pass
    
    q6 = black_friday.isna()
    q6 = q6.sum()
    
    return int(q6.max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    # pass

    return black_friday['Product_Category_3'].mode()[0]


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    # Retorne aqui o resultado da questão 8.
    # pass
    
    return float(black_friday_norm.mean())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    # Retorne aqui o resultado da questão 9.
    # pass
    
    f1 = black_friday_std<1
    f2 = black_friday_std>-1

    return black_friday_std[f1 & f2].shape[0]


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    # Retorne aqui o resultado da questão 10.
    # pass
    
    f1 = black_friday['Product_Category_2'].isna()
    aux = black_friday['Product_Category_3']

    return bool(aux[f1].isna().sum()==f1.sum())

