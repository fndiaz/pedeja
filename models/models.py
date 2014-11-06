
if request.is_local:
	uploadfolder='/home/fernando/web2py/applications/pedeja/static/images/cliente'
else:
	uploadfolder='/var/www/web2py/applications/pedeja/static/images/cliente'

if request.is_local:
	galeriafolder='/home/fernando/web2py/applications/pedeja/static/images/galeria'
else:
	galeriafolder='/var/www/web2py/applications/pedeja/static/images/galeria'

Categoria = db.define_table("categoria",
	Field("nome"),
	format="%(nome)s")


Cliente = db.define_table("cliente",
	Field("nome"),
	Field("apresentacao", "text"),
    Field("descricao", "text"),
	Field("categoria", db.categoria),
	Field("foto_prin", "upload", uploadfolder=uploadfolder,),
	Field("publicado", "boolean"),
	Field("endereco"),
	Field("numero"),
	Field("cidade"),
	Field("telefone"),
	Field("foto_gal1", "upload", uploadfolder=galeriafolder,),
	Field("foto_gal2", "upload", uploadfolder=galeriafolder,),
	Field("foto_gal3", "upload", uploadfolder=galeriafolder,),
	Field("foto_gal4", "upload", uploadfolder=galeriafolder,),
	format="%(nome)s")



if db(db.auth_group.role == 'administrador').isempty():
	db.auth_group.insert(role="administrador")
if db(db.auth_group.role == 'gerenciador').isempty():
	db.auth_group.insert(role="gerenciador")

if db(db.auth_user.email == 'fndiaz02@gmail.com').isempty():
	##Inserindo user root
	root = db.auth_user.insert(first_name="fernando",last_name="root",\
	email="fndiaz02@gmail.com",\
	password=db.auth_user.password.validate("root123")[0])
	##Inserindo permissão de administrador
	group_admin = db(db.auth_group.role == 'administrador').select()
	auth.add_membership(group_admin[0].id, root)

