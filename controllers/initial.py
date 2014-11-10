# coding=UTF-8

def principal():
	response.title = 'Padrão'
	
	return response.render("initial/principal.html")

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def cadastra_categoria():
	response.title = 'Categorias'
	id_edit	= request.vars['id_edit']
	print id_edit
	
	if id_edit is None:
		form 	=	SQLFORM(Categoria)
		response.submit = 'Adicionar'
	else:
		form 	=	SQLFORM(Categoria, id_edit)
		response.submit = 'Editar'

	for input in form.elements():
		input['_class'] = 'form-control'
	form.custom.widget.nome['_placeholder'] = "nome da categoria"

	if form.process().accepted:
		redirect("cadastra_categoria")
	else:
		print 'erro form'

	con = db(Categoria).select()
	return response.render("initial/cadastra_categoria.html", form=form, con=con)


@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def cadastra_cliente():
	response.title = 'Clientes'
	id_edit = request.vars['id_edit']

	if id_edit is None:
		form = SQLFORM(Cliente)
		response.submit = 'Adicionar'
	else:
		form = SQLFORM(Cliente, id_edit)
		response.submit = 'Editar'

	for input in form.elements():
		input['_class'] = 'form-control'
	form.custom.widget.nome['_placeholder'] = "nome do cliente"
	form.custom.widget.descricao['_placeholder'] = "escreva a descrição do cliente ..."
	form.custom.widget.publicado['_style'] = "width:40px"
	form.custom.widget.apresentacao['_style'] = "height:60px"
	form.custom.widget.apresentacao['_placeholder'] = "máximo 60 caracteres"
	#form.custom.widget.endereco['_placeholder'] = "exemplo: Frei caneca"
	#form.custom.widget.numero['_placeholder'] = "somente números"

	if form.process().accepted:
		redirect("cadastra_cliente")
	else:
		print 'erro'
		response.alerta_erro="Erros no formulário"

	con = db(Cliente).select(orderby=Cliente.id)
	return response.render("initial/cadastra_cliente.html", form=form, con=con)

def guia():
	response.title = 'Restaurantes'
	query = (Cliente.publicado == True)

	#
	paginate 	=	8
	if not request.vars.page:
		redirect(URL(vars={'page':1}))
	else:
		page 	=	int(request.vars.page)
	start 	=	(page-1)*paginate
	end 	=	page*paginate
	regis 	=	db(query).count()
	#print regis
	x=1
	if regis%paginate == 0:
		x=0
	#	
	#agen =	db(query).select(limitby=(start,end))

	con = db(query).select(orderby=Cliente.id, limitby=(start,end))

	return response.render("initial/guia.html", con=con, 
			end=end, paginacao="on", regis=regis, paginate=paginate, x=x)

def guia_item():
	response.title = "Descrição"
	id_cliente = request.vars.id_cliente

	if db(Cliente.id == id_cliente).isempty():
		redirect("guia")

	return response.render("initial/guia_item.html", id_cliente=id_cliente)


def log():
	#Carrega mapa JS
	from gluon.tools import geocode
	id_cliente = request.vars.id
	lista=[]

	end = Cliente[id_cliente].endereco
	num = Cliente[id_cliente].numero
	cid = Cliente[id_cliente].cidade
	local = geocode("%s, %s, %s" %(end,num, cid) )
	if local[0] != '':
		lat = local[0]
		lista.append(lat)
		print lat
	if local[1] != '':
		lon = local[1]
		lista.append(lon)
		print lon

	return response.json(lista)

def sobre():
	response.title = "Descrição"

	return response.render("initial/sobre.html")



def delete():
	print request.vars
	funcao 	=	request.vars['tabela']
	id_tab	=	request.vars['id_tab']
	if funcao 	== "cadastra_categoria":
		tabela 	=	 Categoria.id
	if funcao 	== "cadastra_cliente":
		tabela 	=	 Cliente.id

	db(tabela == id_tab).delete()
	redirect(URL(funcao))




##Autenticação
def user():
	#	#if request.args(0) == 'register':
	#  	db.auth_user.bio.writable = db.auth_user.bio.readable = False
	print request.args(0)
	if request.args(0) == 'not_authorized':
		redirect (URL('initial', 'not_authorized'))

	if request.args(0) == 'login':
		redirect(URL('initial', 'login'))
	return response.render("initial/user.html", user=auth())

def login():
	response.title = 'Login'
	response.submit = 'login'
	form = auth.login()
	form.element(_name='email')['_class'] = "form-control"
	form.element(_name='password')['_class'] = "form-control"

	return response.render("initial/login.html", form=form)

def profile():
	response.title = 'Profile'
	response.submit = 'editar'
	form = auth.profile()
	form.element(_name='email')['_class'] = "form-control"
	form.element(_name='first_name')['_class'] = "form-control"
	form.element(_name='last_name')['_class'] = "form-control"

	return response.render("initial/profile.html", form=form)

def change_password():
	response.title = 'Alterar Senha'
	response.submit = 'alterar'
	form = auth.change_password()
	form.element(_name='old_password')['_class'] = "form-control"
	form.element(_name='new_password')['_class'] = "form-control"
	form.element(_name='new_password2')['_class'] = "form-control"

	return response.render("initial/change_password.html", form=form)



def register():
	return auth.register()

def account():
    return dict(register=auth.register(),
                login=auth.login())
	
def download():
	return response.download(request, db)


##Lista auth_users
@auth.requires(auth.has_membership('administrador'))
def usuarios():
	response.title = 'Usuários'
	grid 	= SQLFORM.grid(db.auth_user, user_signature=False)
	#editor = permissao()
	#usuarios= db(db.auth_user.first_name != 'root').select()
	#logger.debug("acesso a usuarios")
	
	return response.render("initial/show_grid.html", grid=grid)

@auth.requires(auth.has_membership('administrador'))
def grupos():
	response.title = 'Grupos'
	grid 	= SQLFORM.grid(db.auth_group, user_signature=False)
	
	return response.render("initial/show_grid.html", grid=grid)

@auth.requires(auth.has_membership('administrador'))
def membros():
	response.title = 'Membros'
	grid 	= SQLFORM.grid(db.auth_membership, user_signature=False)
	
	return response.render("initial/show_grid.html", grid=grid)


	



