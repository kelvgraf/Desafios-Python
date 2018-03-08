
github = {
    'User': 'Kelvgraf' ,
    'Repositorio': '9',
    'Seguindo': '13',
    'Seguidores': '20',
}

print(github)


github['fork']= '0'
	
print(github)


for key in github:
	print(key + ":" + github[key])