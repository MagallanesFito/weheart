from webapp.models import Interest

file = open("hobbies.txt",'r')
for line in file:
	p = Interest(name=str(line))
	p.save()