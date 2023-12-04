#from typing import Union
from fastapi import FastAPI, Request, HTTPException
from controladores.jogador_controlador import JogadorControlador
from controladores.autenticacao_controlador import AutenticacaoControlador
from controladores.fila_controlador import FilaControlador
from controladores.partida_controlador import PartidaControlador
import uvicorn


app = FastAPI()

# ========================== 

if __name__ == "__main__":
  uvicorn.run("URLs:app", host="0.0.0.0", port=8000, reload=True)
  

@app.get("/", tags=["Root"])
async def read_root():
  return { 
    "hello world"
   }

# ========================== Jogador

@app.get("/jogadores/lista_de_jogadores")
async def listar_jogadores():
    return JogadorControlador.listar_todos_os_jogadores()

@app.get("/jogadores/ranking")
async def listar_jogadores():
    return JogadorControlador.listar_ranking()

@app.get("/jogadores/ranking/top3")
async def ranking_top3():
    return JogadorControlador.listar_ranking_top_3()

@app.put("/jogadores/registro/{nome}/{email}/{senha}")
async def adicionar_jogador(nome: str, email: str, senha: str):
    return JogadorControlador.adicionar_jogador(nome, email, senha)

@app.patch("/jogadores/edição/{nome}/{email}")
async def editar_jogador_por_nome(nome: str, email: str, token: str):
    checagem = AutenticacaoControlador.checar_chave(token, nome)
    if (checagem == True):
        return JogadorControlador.editar_jogador_por_nome(nome, email)
    else:
        return {"message": "Não autenticado"}

@app.patch("/jogadores/nova_senha/{nome}/{nova_senha}")
async def editar_senha_do_jogador(nome: str, nova_senha: str, token: str):
    checagem = AutenticacaoControlador.checar_chave(token, nome)
    if (checagem == True):
        return JogadorControlador.editar_senha_do_jogador(nome, nova_senha)
    else:
        return {"message": "Não autenticado"}

@app.delete("/jogadores/remoção/{nome}")
async def remover_jogador_por_nome(nome: str, token: str):
    checagem = AutenticacaoControlador.checar_chave(token, nome)
    if (checagem == True):
        return JogadorControlador.remover_jogador_por_nome(nome)
    else:
        return {"message": "Não autenticado"}

# ========================== Auth

@app.post("/autenticacao/{nome}/{senha}/")
def autenticar(nome: str, senha: str):
    return AutenticacaoControlador.autenticar(nome, senha)

# ========================== Fila

@app.post("/fila/entrar/{nome_jogador}")
async def entrar_na_fila(nome_jogador: str, token: str):
    checagem = AutenticacaoControlador.checar_chave(token, nome_jogador)
    if (checagem == True):
        return FilaControlador.inscrever_na_fila(nome_jogador)
    else:
        return {"message": "Não autenticado"}

@app.post("/fila/sair/{nome_jogador}")
async def sair_da_fila(nome_jogador: str, token: str):
    checagem = AutenticacaoControlador.checar_chave(token, nome_jogador)
    if (checagem == True):
        return FilaControlador.desinscrever_da_fila(nome_jogador)
    else:
        return {"message": "Não autenticado"}

@app.get("/fila/jogadores_na_fila")
async def mostrar_jogadores_na_fila():
    return FilaControlador.mostrar_jogadores_na_fila()

@app.get("/fila/checagem/{nome_jogador}")
async def checar_começo_de_partida(nome_jogador: str, token: str):
    checagem = AutenticacaoControlador.checar_chave(token, nome_jogador)
    if (checagem == True):
        return FilaControlador.checar_confirmacao_da_partida(nome_jogador)
    else:
        return {"message": "Não autenticado"}

# ========================== Partida

@app.get("/partida/tabuleiro/{id}/{nome_jogador}")
async def pegar_representacao_tabuleiro_partida(id: int, nome_jogador: str, token: str):
    checagem = AutenticacaoControlador.checar_chave(token, nome_jogador)
    if (checagem == True):
        return PartidaControlador.pegar_representacao_tabuleiro_partida(id, nome_jogador)
    else:
        return {"message": "Não autenticado"}

@app.get("/partida/embarcacoes/peças/{id}/{nome_jogador}")
async def checar_embarcacoes_disponiveis(id: int, nome_jogador: str, token: str):
    checagem = AutenticacaoControlador.checar_chave(token, nome_jogador)
    if (checagem == True):
        return PartidaControlador.checar_embarcacoes_disponiveis(id, nome_jogador)
    else:
        return {"message": "Não autenticado"}

@app.patch("/partida/tabuleiro/peças/{id}/{nome_jogador}/{embarcacao}/{coord_x}/{coord_y}/{orientacao}")
async def colocar_embarcacao_tabuleiro(id: int, nome_jogador: str, embarcacao: str, coord_x: str, coord_y: int, orientacao: str, token: str):
    checagem = AutenticacaoControlador.checar_chave(token, nome_jogador)
    if (checagem == True):
        return PartidaControlador.colocar_embarcacao_tabuleiro(id, nome_jogador, embarcacao, coord_x, coord_y, orientacao)
    else:
        return {"message": "Não autenticado"}

@app.get("/partida/tabuleiro/disparo/{id}/{nome_jogador}/{coord_x}/{coord_y}")
async def realizar_disparo(id: int, nome_jogador: str, coord_x: str, coord_y: int, token: str):
    checagem = AutenticacaoControlador.checar_chave(token, nome_jogador)
    if (checagem == True):
        return PartidaControlador.realizar_disparo(id, nome_jogador, coord_x, coord_y)
    else:
        return {"message": "Não autenticado"}
    