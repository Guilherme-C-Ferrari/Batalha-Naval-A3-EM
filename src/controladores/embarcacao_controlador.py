from src.modelos.embarcacao import FabricaEmbarcacao

class EmbarcacoesControlador():
    
    @classmethod
    def criar_embarcacoes(cls):
        embarcacoes = [
            FabricaEmbarcacao.instance().fabrica('Submarino'),
            FabricaEmbarcacao.instance().fabrica('Submarino'),
            FabricaEmbarcacao.instance().fabrica('Submarino'),
            FabricaEmbarcacao.instance().fabrica('Navio Pequeno'),
            FabricaEmbarcacao.instance().fabrica('Navio Pequeno'),
            FabricaEmbarcacao.instance().fabrica('Navio Médio'),
            FabricaEmbarcacao.instance().fabrica('Navio Grande'),
            FabricaEmbarcacao.instance().fabrica('Porta Aviões')
        ]
        return embarcacoes