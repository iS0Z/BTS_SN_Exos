#!/usr/bin/python3
import matplotlib.pyplot as plt
print("""
	Ce Programme calcule une suite de Syracuse 
	Depuis le nombre que vous allez entrez 
	""")
"""
Init Vars
"""
suite = [];
suite_a = [0]
done = 0;
tmp_vol_alt = 0
n_suite = int(input("	Entrez un nombre : "))
suite.append(n_suite)
"""
while calcul
"""
while done == 0:
	index = len(suite)-1;
	n_calc = suite[index]
	if (n_calc % 2) == 0:
		n_calc = n_calc/2
	else:
		n_calc = n_calc*3;
		n_calc = n_calc+1;
	suite.append(n_calc);
	suite_a.append(len(suite))
	index = len(suite)-1;
	index1 = len(suite);
	v_suite_1 = suite[index1-1];
	v_suite_2 = suite[index1-2];
	v_suite_3 = suite[index1-3];
	if v_suite_1 == 1 and v_suite_2 == 2 and v_suite_3 == 4:
		done = 1;
	if suite[index-2] < suite[index-1] and suite[index-1] > n_suite:
		tmp_vol_alt = tmp_vol_alt + 1;
"""
Print results
"""
alt_max = max(suite);
tmp_vol = len(suite)-2;
print("""
	
	Pour la suite de Syracuse de {0}
	Le temps de vol est {1}
	L'altidude Max est de {2}
	Le temps de vol en altidude est de {3}
	
	Liste de la suite : 
	----------------------------------------------------
{4}
	----------------------------------------------------
	""".format(n_suite, tmp_vol, alt_max, tmp_vol_alt, suite));
plt.plot(suite_a, suite)
plt.show()