#Vytvořte řetězec &quot;Python je jazyk programování.&quot; a vytiskněte ho s velkými písmeny.
veta = "Python je jazyk programovaní"
print(veta.upper())
#2. Spočítejte, kolik písmen je ve slově &quot;programování&quot;.
slovo = "programovaní"
print(len(slovo))
#3. Vytvořte řetězec s vaším jménem a věkem a vytiskněte ho pomocí f-string.
meno = "Denisa"
vek = "30"
print(f"Volám sa {meno} a mám {vek} rokov.")
#4. Vytvořte řetězec &quot;Mám 5 jablek, 3 pomeranče a 4 banány.&quot; a rozdělte ho podle čár a
#vytiskněte výsledný seznam.
#veta = ["Mám 5 jablek, 3 pomaranče a 4 banány"]
#rozdelenie = veta. (',')
#print(rozdelenie)
ovocie = "Mám 5 jablek, 3 pomaranže a 4 banány."
zoznam = ovocie.split(",")
print(zoznam)

#Cvičení Seznamy::
#Vytvořte seznam vašich tří oblíbených knih a vytiskněte ho.
seznam = ["Harry Potter", "90 Dní Južne", "Digitálna pevnosť"]
print(seznam)
#Přidejte do seznamu další knihu a vytiskněte upravený seznam.
seznam.append("Polonoc v Černobyli")
print(seznam)
#Odeberte ze seznamu druhou knihu a vytiskněte upravený seznam.
seznam.remove("90 Dní Južne")
print(seznam)
#Zjistěte, kolik knih je nyní v seznamu.**/
print(len(seznam))
