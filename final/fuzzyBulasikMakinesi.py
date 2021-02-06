# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:18:26 2021

@author: Abdullah Tunçer

1721012045
Bulanık mantıkda, bulaşık makinesine ne kadar detarjan konulmasını hesaplama
Giriş Değeri kısmından girdiler değiştirilebilir

"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as karar

# Girişler
miktar = karar.Antecedent(np.arange(0,101,1), 'Bulasik Miktari')
kirlilik = karar.Antecedent(np.arange(0,101,1), 'Kirlilik Derecesi')
cins = karar.Antecedent(np.arange(0,101,1), 'Bulasik Cinsi')

# Çıkış
deterjan = karar.Consequent(np.arange(0,101,1), 'Deterjan Miktari')

# Tür tanımlama
miktar['az'] = fuzz.trimf(miktar.universe, [0, 0, 35])
miktar['orta'] = fuzz.trimf(miktar.universe, [15, 50, 85])
miktar['çok'] = fuzz.trimf(miktar.universe, [65, 100, 100])

kirlilik['az'] = fuzz.trimf(kirlilik.universe, [0, 0, 35])
kirlilik['orta'] = fuzz.trimf(kirlilik.universe, [15, 50, 85])
kirlilik['çok'] = fuzz.trimf(kirlilik.universe, [65, 100, 100])

cins['hassas'] = fuzz.trimf(cins.universe, [0, 0, 35])
cins['karma'] = fuzz.trimf(cins.universe, [15, 50, 85])
cins['güçlü'] = fuzz.trimf(cins.universe, [65, 100, 100])

deterjan['çok az'] = fuzz.trimf(deterjan.universe, [0, 0, 25])
deterjan['az'] = fuzz.trimf(deterjan.universe, [17.5, 30, 42.5])
deterjan['normal'] = fuzz.trimf(deterjan.universe, [32.5, 50, 67.5])
deterjan['çok'] = fuzz.trimf(deterjan.universe, [57.5, 74, 92.5])
deterjan['çok fazla'] = fuzz.trimf(deterjan.universe, [82.5, 100, 100])

"""
#Tabloları Görüntüle
miktar.view()
kirlilik.view()
cins.view()
deterjan.view()
"""

# Kurallar
kural1 = karar.Rule(miktar['az'] | cins['hassas'], deterjan['az'])
kural2 = karar.Rule(miktar['orta'] | kirlilik['orta'] & cins['güçlü'], deterjan['normal'])
kural3 = karar.Rule(miktar['çok'] & kirlilik['çok'], deterjan['çok fazla'])
kural4 = karar.Rule(miktar['çok'] | kirlilik['çok'], deterjan['çok'])
kural5 = karar.Rule(miktar['az'] | kirlilik['az'] | cins['hassas'], deterjan['çok az'])
kural6 = karar.Rule(miktar['az'] & cins['güçlü'], deterjan['az'])
kural7 = karar.Rule(kirlilik['orta'] & cins['güçlü'], deterjan['çok'])
kural8 = karar.Rule(miktar['çok'] & kirlilik['çok'] & cins['karma'], deterjan['çok'])


# Hesapla
funding_karar = karar.ControlSystem([kural1, kural2, kural3, kural4, kural5, kural6, kural7, kural8])

funding_ = karar.ControlSystemSimulation(funding_karar)

# Giriş değerleri
funding_.input['Bulasik Miktari']=50
funding_.input['Kirlilik Derecesi']=75
funding_.input['Bulasik Cinsi']=55

# Hesap
funding_.compute()
print("Deterjan Hesabı:")
print(funding_.output['Deterjan Miktari'])
deterjan.view(sim=funding_)

