from celery import shared_task
from integracao.models import UsuarioRecebido

@shared_task
def processar_usuario(dados):
    try:
       
        usuario = UsuarioRecebido(
            nome=dados['nome'],
            email=dados['email'],
            senha=dados['senha']
        )
        usuario.save()
        print(f"Dados do usuário {dados['nome']} processados com sucesso!")
    except Exception as e:
        print(f"Erro ao processar o usuário: {e}")
