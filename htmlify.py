file=open("themes.txt","r")
a=open("themeHTML.txt","w")
for theme in file:
	theme=theme.split("\n")
	i = "<option value=\""+theme[0]+"\">"+theme[0]+"</option>"
	a.write(i+"\n")
file.close()
a.close()