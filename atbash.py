#coding:utf-8
'''
La simplicité est le principe de l'art.

#On m'a dit un jour qu'on pardonnait à la hauteur que l'on aime...
La vie ne vaut pas être vécu sans la personne qu'on aime
Le problème de ce monde c'est que les gens parlent sans penser, pensent sans agir et jugent sans savoir
sois toi même, les gens ne sont pas obligés de t'aimer et t'es pas obligé de t'en soucier
'''
import string as s

x = s.ascii_letters + ' ' + s.digits + s.punctuation
y = x[::-1]

word = '$<>;?\|`Q{`Q>`.Q/\/`.u\n8é/<ï=`Q{`Q=<.Q~+`=-,/`.u\n4,>\è/`Q{~=.Q>~Q+\`u\n1={`Q{`Q{<,|`,/u\nÉ-`/=`??`Q|<>;~^=`\n💗💖💗'
#word = 'Magnifique\nAdorable\nNoble\nOriginal\nAdmirable👌👌😎'
#word = "]--;.qrr_/s;</=],}s|<>r+\`*f+\{`<s;];l+\`*@`(n;]K_~L{NN~JLO}{"

#word = "Bonjour Dorian Je m'appelle Manoa"
transformation = str.maketrans(x, y)
result = str.translate(word, transformation)

print(result)

r = [43, 43, 43, 43]
d = [chr(x) for x in r]
o = ""
for j in range(len(d)):
	o += d[j]
print(o)

t = "++++"
d = [ord(x) for x in t]
print(d)


# 0322171236 == 0388551327 == num_Ryan


def moyenne(liste):
	if len(liste) == 0:
		return 0
	else:
		return liste[0] + moyenne(liste[1:]) / len(liste)
print(moyenne([1,2,3,4]))


def moyenne(liste):
	som = 0
	for x in liste:
		som += x
	return som / len(liste)
print(moyenne([1,2,3,4]))