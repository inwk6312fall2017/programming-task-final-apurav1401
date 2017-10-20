with open('running-config.cfg','r') as file:
 filedata = file.read()
 filedata = filedata.replace('172','192')
with open ('running-config.cfg','w') as file:
 file.write(filedata)
print(filedata)
