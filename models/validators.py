

db.categoria.nome.requires = IS_NOT_EMPTY()
db.categoria.posicao.requires = IS_IN_SET(range(1,30)) 
db.categoria.descricao.requires = [IS_NOT_EMPTY(), IS_LENGTH(minsize=74,maxsize=85)]

db.cliente.nome.requires = IS_NOT_EMPTY()
db.cliente.apresentacao.requires = [IS_NOT_EMPTY(), IS_LENGTH(maxsize=60)]
db.cliente.descricao.requires = IS_NOT_EMPTY()
db.cliente.foto_prin.requires = IS_NOT_EMPTY()
db.cliente.endereco.requires = IS_NOT_EMPTY()
db.cliente.endereco.requires = IS_NOT_EMPTY()
db.cliente.cidade.requires = IS_IN_SET(['Santos', 'Franca'])
db.cliente.telefone.requires = IS_NOT_EMPTY()


##Agenda
#db.agenda.empresa.requires = IS_NOT_EMPTY(error_message=
#						T("valor não pode ser nulo"))

#db.agenda.telefone.requires = [IS_NOT_EMPTY(error_message=T("o telefone deve conter de 9 a 11 números")),
#IS_NOT_IN_DB(db, 'agenda.telefone', error_message=T("este número está em uso")),
#IS_LENGTH(minsize=9, maxsize=11, error_message=T("o telefone deve conter de 9 a 11 números")),
#IS_MATCH('[0-9]+', error_message=T("somente números"))]


