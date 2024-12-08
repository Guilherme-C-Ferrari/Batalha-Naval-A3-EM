from src.backend.modelos.embarcacao import Embarcacao
import copy

# Método que representa a parte to tabuleiro
class TabuleiroParte():

    _coord_x = None
    _coord_y = None
    _area_tabuleiro : list
    _area_tabuleiro_camuflada : list
    _lista_embarcacoes_para_colocar : list[Embarcacao]
    _lista_embarcacoes_vivas: list[Embarcacao]

    def __init__(self):
        self._coord_x = "ABCDE"
        self._coord_y = range(5)
        self._area_tabuleiro = [["X" for x in range(5)] for x in self._coord_y]
        self._area_tabuleiro_camuflada = [["X" for x in range(5)] for x in self._coord_y]
        self._lista_embarcacoes_para_colocar = []
        self._lista_embarcacoes_vivas = []

    # ========================== Métodos envolvendo a área da parte do tabuleiro

    def devolver_parte_tabuleiro(self):
        return self._area_tabuleiro
    
    def devolver_parte_tabuleiro_camuflado(self):
        return self._area_tabuleiro_camuflada
    
    # ========================== Métodos envolvendo as peças da parte do tabuleiro

    # ========== Embarcações para colocar

    def definir_embarcacoes_para_colocar(self, lista : list[Embarcacao]):
        self._lista_embarcacoes_para_colocar = lista

    def devolver_embarcacoes_para_colocar(self):
        return self._lista_embarcacoes_para_colocar
    
    def remover_embarcacao_para_colocar_da_lista(self, embarcacao : Embarcacao):
        self._lista_embarcacoes_para_colocar = [e for e in self._lista_embarcacoes_para_colocar if e != embarcacao]
    
    # ========== Embarcações para vivas

    def definir_embarcacao_viva(self, embarcacao : Embarcacao):
        self._lista_embarcacoes_vivas.append(embarcacao)

    
    def devolver_embarcacoes_vivas(self):
        return self._lista_embarcacoes_vivas()
    
    def remover_embarcacao_viva_da_lista(self, embarcacao : Embarcacao):
        self._lista_embarcacoes_vivas = [e for e in self._lista_embarcacoes_vivas if e != embarcacao]
    
    # ========== Mudanças na área com as embarcações

    def colocar_embarcacao_na_area(self, embarcacao: Embarcacao, coord_x: str, coord_y: int, orientacao: str):

        coord_xx = self._coord_x.index(coord_x)
        coord_yy = coord_y - 1
        copia_de_segurança = []
        copia_de_segurança = copy.deepcopy(self._area_tabuleiro)

        if not(0 <= coord_xx < 5 and 0 <= coord_yy < 5):
            return False
        
        for i in range(len(embarcacao._formato)):
            for j in range(len(embarcacao._formato[i])):
                if orientacao == "horizontal":
                    if coord_yy + j >= 5 or self._area_tabuleiro[coord_xx + i][coord_yy + j] != 'X':
                        self._area_tabuleiro = copia_de_segurança
                        return False
                    self._area_tabuleiro[coord_xx + i][coord_yy + j] = embarcacao._formato[i][j]
                elif orientacao == "vertical":
                    if coord_xx + j >= 5 or self._area_tabuleiro[coord_xx + j][coord_yy + i] != 'X':
                        self._area_tabuleiro = copia_de_segurança
                        return False
                    self._area_tabuleiro[coord_xx + j][coord_yy + i] = embarcacao._formato[i][j]
                else:
                    return False
        
        return True
        
    # ========== Ações no tabuleiro
    
    def disparo(self, coord_x: str, coord_y: int):
        
        coord_xx = self._coord_x.index(coord_x)
        coord_yy = coord_y - 1
        pos = self._area_tabuleiro[coord_xx][coord_yy]
         
        if not(0 <= coord_xx < 5 and 0 <= coord_yy < 5):    
            return False
        
        match pos:
                case "X":
                    return False
                case "N":
                    self.revelar_embarcacao(coord_xx, coord_yy)
                    return True
    
    def revelar_embarcacao(self, coord_xx: int, coord_yy: str):
        self._area_tabuleiro_camuflada[coord_xx][coord_yy] = self._area_tabuleiro[coord_xx][coord_yy]

    def comparar_tabuleiros(self):
        if self._area_tabuleiro == self._area_tabuleiro_camuflada:
            return True
        return False              

# Método que representa o tabuleiro, possuind partes do tabuleiro.
class Tabuleiro():
    
    _parte_a : TabuleiroParte = None
    _parte_b : TabuleiroParte = None

    def __init__(self):
        self._parte_a = TabuleiroParte()
        self._parte_b = TabuleiroParte()

    # ========================== Métodos envolvendo a área da parte do tabuleiro

    def devolver_tabuleiro_por_parte(self, parte: str):
        if (parte == "a"):
            return self._parte_a.devolver_parte_tabuleiro()
        elif (parte == "b"):
            return self._parte_b.devolver_parte_tabuleiro()
        else:
            return False
        
    def devolver_tabuleiro_camuflado_por_parte(self, parte: str):
        if (parte == "a"):
            return self._parte_a.devolver_parte_tabuleiro_camuflado()
        elif (parte == "b"):
            return self._parte_b.devolver_parte_tabuleiro_camuflado()
        else:
            return False
        
    # ========================== Métodos envolvendo as peças da parte do tabuleiro

    # ========== Embarcações para colocar

    def definir_embarcacoes_tabuleiro (self, lista: list[Embarcacao]):
        self._parte_a.definir_embarcacoes_para_colocar(lista)
        self._parte_b.definir_embarcacoes_para_colocar(lista)

    def delvover_embarcacoes_para_colocar(self, parte: str):
        if (parte == "a"):
            return self._parte_a.devolver_embarcacoes_para_colocar()
        elif (parte == "b"):
            return self._parte_b.devolver_embarcacoes_para_colocar()
        else:
            return False
    
    def remover_embarcacao_para_colocar_da_parte(self, parte: str, embarcacao: Embarcacao):
        if (parte == "a"):
            return self._parte_a.remover_embarcacao_para_colocar_da_lista(embarcacao)
        elif (parte == "b"):
            return self._parte_b.remover_embarcacao_para_colocar_da_lista(embarcacao)
        else:
            return False
        
    # ========== Embarcações para vivas
        
    def definir_embarcacao_viva_na_parte(self, parte: str, embarcacao: Embarcacao):
        if (parte == "a"):
            return self._parte_a.definir_embarcacao_viva(embarcacao)
        elif (parte == "b"):
            return self._parte_b.definir_embarcacao_viva(embarcacao)
        else:
            return False
        
    def delvover_embarcacoes_vivas(self, parte: str):
        if (parte == "a"):
            return self._parte_a.devolver_embarcacoes_vivas()
        elif (parte == "b"):
            return self._parte_b.devolver_embarcacoes_vivas()
        else:
            return False
        
    def remover_embarcacao_viva(self, parte: str, embarcacao: Embarcacao):
        if (parte == "a"):
            return self._parte_a.remover_embarcacao_viva_da_lista(embarcacao)
        elif (parte == "b"):
            return self._parte_b.remover_embarcacao_viva_da_lista(embarcacao)
        else:
            return False
        
    # ========== Mudanças na área com as embarcações
        
    def colocar_embarcacao_na_parte(self, parte: str, embarcacao: Embarcacao, coord_x: str, coord_y: int, orientacao: str):
        if (parte == "a"):
            return self._parte_a.colocar_embarcacao_na_area(embarcacao, coord_x, coord_y, orientacao)
        elif (parte == "b"):
            return self._parte_b.colocar_embarcacao_na_area(embarcacao, coord_x, coord_y, orientacao)
        else:
            return False
        
    # ========== Ações no tabuleiro
    
    def disparo(self, parte: str, coord_x: str, coord_y: int):
        if (parte == "a"):
            return self._parte_a.disparo(coord_x, coord_y)
        elif (parte == "b"):
            return self._parte_b.disparo(coord_x, coord_y)
        else:
            return False
        
    def comparar_tabuleiros_por_parte(self, parte: str):
        if (parte == "a"):
            return self._parte_a.comparar_tabuleiros()
        elif (parte == "b"):
            return self._parte_b.comparar_tabuleiros()
        else:
            return False
