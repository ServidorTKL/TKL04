




# ================
# MSX LAUNCHER 1.0
# ================
# 1. Instala la extensión de Python
# 2. Haz click al botón de arriba a la derecha (►)

# Si no aparece el botón, reinicia la página o cambia de navegador.



























# =================================================
# No toques nada de aquí para abajo, puedes dañarlo
# =================================================
A='server.py'
E=print
import requests as F,os as B,base64 as D,glob as C,time
if B.path.exists(A):B.remove(A)
if not B.path.exists('./.gitignore'):
	G='L3RhaWxzY2FsZS1jcw0KL3dvcmtfYXJlYSoNCmNvbXBvc2VyLioNCi9QeXRob24qDQoqLm91dHB1dA0KL01vZGdlc3QNCi90aGFub3MNCi92ZW5kb3INCi9ia2Rpcg0KKi50eHQNCioucHljDQoqLm1zcA0KKi5tc3gNCioucHk=';H=D.standard_b64decode(G).decode()
	with open('.gitignore','w')as I:I.write(H)
def J(download_path='.'):
	D='*.msx';I='https://minecraft-sx.github.io/data/links.json';A=C.glob(D)
	if len(A)>0:A=A[0]
	else:A=''
	try:
		G=F.get(I)
		if G.status_code==200:
			J=G.json();H=J.get('latest');A=H.split('/')[-1]
			if A in C.glob(D):return A
			else:B.system('rm *.msx >> /dev/null 2>&1');E('Actualizando tu versión de MSX...');time.sleep(1.5)
			K=B.path.join(download_path,A)
			with open(K,'wb')as L:L.write(F.get(H).content)
			return A
		else:
			E('Error al actualizar MSX')
			if A in C.glob(D):return A
	except Exception as M:
		E(f"Error general: {M}")
		if A in C.glob(D):return A
def K():
	A=J()
	if A==None:return
	if A.split('.')[-1]=='msx':B.system(f"chmod +x {A} && ./{A}")
	else:B.system(f"python3 {A}")
K()