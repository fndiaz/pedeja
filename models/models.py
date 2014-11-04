
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






