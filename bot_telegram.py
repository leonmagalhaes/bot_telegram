from typing import Final
import random
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CommandHandler, CallbackContext, Application, ContextTypes


TOKEN: Final = '6474974078:AAG7EN_Ge8miT2fmOKDqn9tfJ9DrjyxXtNk'

augurio_lista = [
    "A Mula: -100 cn de carga",
    "O Touro: +1 BA CaC",
    "O Lobo: +1 Dano CaC",
    "O Tigre: +1 BA e Dano CaC com uma arma",
    "O Alvo: +1 BA à Distância",
    "A Flecha: +1 Dano à Distância",
    "O Arqueiro: +1 BA e Dano à dist. com uma arma",
    "O Castelo: +1 CA",
    "O Urso: +1 PV Máx por Nível",
    "O Coração: +1 PV Cura recebida",
    "O Camelo: +1 Vigor",
    "A Boca: +1 Idioma",
    "O Pentagrama: +1 Acurácia Mágica",
    "A Tocha: +1 Sanidade",
    "O Martelo: +1 Ação de Interlúdio",
    "O Relâmpago: + 1d4 Dano em magia",
    "A Flor: +1 Reação",
    "Os Gêmeos: +1 Capanga",
    "A Coroa: +1 Lealdade",
    "O Berço: +1 em Save de Morte",
    "A Águia: +1 em Save de Contato",
    "O Rio: +1 em Save de Paralisia",
    "O Sapo: +1 em Save de Irrupção",
    "A Montanha: +1 em Save de Feitiço",
    "O Escudo: +1 em Save vs Efeito Mágico",
    "O Macaco: +1 em Save vs Armadilhas",
    "A Mão Divina: +1 em todos os Saves",
    "O Leviatã: -1 nas Salvaguardas do Alvo",
    "A Ânfora: +5% XP",
    "O Grimório: +1 Espaço de Magia de Nível 1"
]

ocupacao_lista = [
    "(H) Acólito(a) / (A) Açougueiro(a) / (E) Alquimétrico(a) / (P) Abatedor(a) de galinha",
    "(H) Açougueiro(a) / (A) Açougueiro(a) / (E) Alquimétrico(a) / (P) Abatedor(a) de galinha",
    "(H) Agricultor(a) / (A) Açougueiro(a) / (E) Alquimétrico(a) / (P) Abatedor(a) de galinha",
    "(H) Alquimista / (A) Agiota / (E) Alquimétrico(a) / (P) Abatedor(a) de galinha",
    "(H) Apicultor(a) / (A) Agiota / (E) Apicultor(a) / (P) Agiota",
    "(H) Apostador(a) / (A) Agiota / (E) Apicultor(a) / (P) Agiota",
    "(H) Apotecário(a) / (A) Alquimista / (E) Apicultor(a) / (P) Agiota",
    "(H) Aprendiz de mago / (A) Alquimista / (E) Apicultor(a) / (P) Agiota",
    "(H) Armadilheiro / (A) Alquimista / (E) Artesã(o) / (P) Armadilheiro",
    "(H) Armeiro(a) / (A) Apicultor(a) / (E) Artesã(o) / (P) Armadilheiro",
    "(H) Artesã(o) de Argila / (A) Apicultor(a) / (E) Artesã(o) / (P) Armadilheiro",
    "(H) Astrólogo(a) / (A) Apicultor(a) / (E) Artesã(o) / (P) Armadilheiro",
    "(H) Atendente / (A) Apotecário(a) / (E) Astrônomo / (P) Armadilheiro",
    "(H) Ator ou Atriz / (A) Apotecário(a) / (E) Astrônomo / (P) Barqueiro(a)",
    "(H) Bandido(a) / (A) Apotecário(a) / (E) Astrônomo / (P) Barqueiro(a)",
    "(H) Barbeiro(a) / (A) Armeiro(a) / (E) Astrônomo / (P) Barqueiro(a)",
    "(H) Barqueiro(a) / (A) Armeiro(a) / (E) Ator ou Atriz / (P) Barqueiro(a)",
    "(H) Bauzeiro / (A) Armeiro(a) / (E) Ator ou Atriz / (P) Barqueiro(a)",
    "(H) Bufão / (A) Bauzeiro(a) / (E) Ator ou Atriz / (P) Bom vivant",
    "(H) Caçador de Recompensas / (A) Bauzeiro(a) / (E) Ator ou Atriz / (P) Bom vivant",
    "(H) Caçador(a) ou Bauzeiro(a) / (A) Bauzeiro(a) / (E) Bandoleiro(a) / (P) Bom vivant",
    "(H) Cafetão(ina) / (A) Burocrata / (E) Bandoleiro(a) / (P) Bom vivant",
    "(H) Capanga valentão / (A) Burocrata / (E) Bandoleiro(a) / (P) Bom vivant",
    "(H) Carrasco / (A) Cantor(a) de velório / (E) Bandoleiro(a) / (P) Caçador(a)",
    "(H) Carroceiro(a) / (A) Cantor(a) de velório / (E) Cantor(a) / (P) Caçador(a)",
    "(H) Cartomante / (A) Cantor(a) de velório / (E) Cantor(a) / (P) Caçador(a)",
    "(H) Carvoeiro(a) / (A) Carvoeiro(a) / (E) Cantor(a) / (P) Caçador(a)",
    "(H) Cavador(a) / (A) Carvoeiro(a) / (E) Cantor(a) / (P) Caçador(a) de recompensa",
    "(H) Cavalariço(a) / (A) Carvoeiro(a) / (E) Cortesão(ã) / (P) Caçador(a) de recompensa",
    "(H) Cervejeiro(a) / (A) Cervejeiro(a) / (E) Cortesão(ã) / (P) Caçador(a) de recompensa",
    "(H) Chaveiro(a) / (A) Cervejeiro(a) / (E) Cortesão(ã) / (P) Caçador(a) de recompensa",
    "(H) Cocheiro(a) / (A) Chaveiro(a) / (E) Escultor(a) / (P) Cervejeiro(a)",
    "(H) Coletor(a) de impostos / (A) Chaveiro(a) / (E) Escultor(a) / (P) Cervejeiro(a)",
    "(H) Contador(a) / (A) Chaveiro(a) / (E) Cozinheiro(a) / (P) Escultor(a) / (P) Cervejeiro(a)",
    "(H) Contrabandista / (A) Cozinheiro(a) / (E) Étermante / (P) Cervejeiro(a)",
    "(H) Coveiro / (A) Cozinheiro(a) / (E) Engenheiro(a) / (P) Étermante / (P) Construtor(a)",
    "(H) Cozinheiro(a) / (A) Engenheiro(a) / (E) Étermante / (P) Construtor(a)",
    "(H) Criador(a) de Animais / (A) Escavador(a) / (E) Étermante / (P) Construtor(a)",
    "(H) Cultista / (A) Escavador(a) / (E) Exilado(a) / (P) Construtor(a)",
    "(H) Curandeiro(a) / (A) Escavador(a) / (E) Exilado(a) / (P) Construtor(a)",
    "(H) Curtidor(a) / (A) Escavador(a) / (E) Exilado(a) / (P) Cozinheiro(a)",
    "(H) Dançarino(a) / (A) Escriba de runas / (E) Exilado(a) / (P) Cozinheiro(a)",
    "(H) Diácono(a) / (A) Escriba de runas / (E) Falcoeiro(a) / (P) Cozinheiro(a)",
    "(H) Eremita / (A) Escriba de runas / (E) Falcoeiro(a) / (P) Cozinheiro(a)",
    "(H) Escravo(a) recém liberto / (A) Exilado(a) / (E) Falcoeiro(a) / (P) Cozinheiro(a)",
    "(H) Escriba / (A) Exilado(a) / (E) Falcoeiro(a) / (P) Fazendeiro(a)",
    "(H) Escudeiro(a) / (A) Exilado(a) / (E) Filósofo(a) / (P) Fazendeiro(a)",
    "(H) Estivador(a) / (A) Exterminador de pragas / (E) Filósofo(a) / (P) Fazendeiro(a)",
    "(H) Exterminador(a) de pragas / (A) Exterminador de pragas / (E) Filósofo(a) / (P) Fazendeiro(a)",
    "(H) Falsificador(a) / (A) Exterminador de pragas / (E) Filósofo(a) / (P) Fazendeiro(a)",
    "(H) Fazedor(a) de corda / (A) Fazendeiro(a) de cogumelo / (E) Forasteiro(a) / (P) Garçom(nete)",
    "(H) Feirante / (A) Fazendeiro(a) de cogumelo / (E) Forasteiro(a) / (P) Garçom(nete)",
    "(H) Ferreiro(a) / (A) Fazendeiro(a) de cogumelo / (E) Forasteiro(a) / (P) Garçom(nete)",
    "(H) Fora da lei / (A) Ferreiro(a) / (E) Forasteiro(a) / (P) Guarda das estradas / (P) Garçom(nete)",
    "(H) Frei medicante / (A) Ferreiro(a) / (E) Guarda das estradas / (P) Garçom(nete)",
    "(H) Garçom(nete) / (A) Ferreiro(a) / (E) Guarda das estradas / (P) Gatuno(a)",
    "(H) Garimpeiro(a) / (A) Guarda da forjaria / (E) Guarda das florestas / (P) Gatuno(a)",
    "(H) Guarda / (A) Guarda da forjaria / (E) Guarda das florestas / (P) Gatuno(a)",
    "(H) Guarda de caravana / (A) Guarda da forjaria / (E) Guarda das florestas / (P) Gatuno(a)",
    "(H) Guarda florestal / (A) Guarda dos portões / (E) Herbalista / (P) Gatuno(a)",
    "(H) Guarda-caça / (A) Guarda dos portões / (E) Herbalista / (P) Guarda das colinas",
    "(H) Cuidador de Idosos / (A) Guardiã(o) das tradições (noviço) / (E) Herbalista / (P) Guarda das colinas",
    "(H) Herbalista / (A) Guardiã(o) das tradições (noviço) / (E) Herbalista / (P) Guarda das colinas",
    "(H) Ilustrador / (A) Guardiã(o) das tradições (noviço) / (E) Lanceiro(a) Real / (P) Guarda das colinas",
    "(H) Inventor(a) / (A) Inventor(a) / (E) Lanceiro(a) Real / (P) Mensageiro(a)",
    "(H) Joalheiro(a) / (A) Inventor(a) / (E) Lanceiro(a) Real / (P) Mensageiro(a)",
    "(H) Lenhador / (A) Inventor(a) / (E) Lanceiro(a) Real / (P) Mensageiro(a)",
    "(H) Limpador(a) de chaminés / (A) Joalheiro(a) / (E) Marinheiro(a) / (P) Mensageiro(a)",
    "(H) Limpador(a) de esgoto / (A) Joalheiro(a) / (E) Marinheiro(a) / (P) Mensageiro(a)",
    "(H) Luzeiro(a) / (A) Joalheiro(a) / (E) Marinheiro(a) / (P) Negociante",
    "(H) Mágico / (A) Joalheiro(a) / (E) Marinheiro(a) / (P) Negociante",
    "(H) Malabarista / (A) Limpador(a) de chaminés / (E) Mensageiro(a) / (P) Negociante",
    "(H) Marinheiro(a) / (A) Limpador(a) de chaminés / (E) Mensageiro(a) / (P) Negociante",
    "(H) Mensageiro(a) / (A) Limpador(a) de chaminés / (E) Mensageiro(a) / (P) Negociante",
    "(H) Mercador(a) / (A) Luzeiro(a) / (E) Mensageiro(a) / (P) Sábio(a)",
    "(H) Mercenário(a) / (A) Luzeiro(a) / (E) Mensageiro(a) / (P) Sábio(a)",
    "(H) Minerador(a) / (A) Luzeiro(a) / (E) Mercador(a) / (P) Sábio(a)",
    "(H) Mordomo / (A) Mercador(a) / (E) Mercador(a) / (P) Sábio(a)",
    "(H) Musicista / (A) Mercador(a) / (E) Mercador(a) / (P) Tintureiro(a)",
    "(H) Nobre emancipado / (A) Mercador(a) / (E) Mercador(a) / (P) Tintureiro(a)",
    "(H) Noviço(a) / (A) Mercenário(a) / (E) Musicista / (P) Tintureiro(a)",
    "(H) Parteira(o) / (A) Mercenário(a) / (E) Musicista / (P) Tintureiro(a)",
    "(H) Pastor(a) / (A) Mercenário(a) / (E) Musicista / (P) Tintureiro(a)",
    "(H) Pedinte / (A) Minerador / (E) Musicista / (P) Vagabundo(a)",
    "(H) Pedreiro / (A) Minerador / (E) Navegador(a) / (P) Vagabundo(a)",
    "(H) Peixeiro(a) / (A) Minerador / (E) Navegador(a) / (P) Vagabundo(a)",
    "(H) Pescador(a) / (A) Ourives / (E) Navegador(a) / (P) Vagabundo(a)",
    "(H) Pregoeiro(a) / (A) Ourives / (E) Navegador(a) / (P) Vagabundo(a)",
    "(H) Queijeiro(a) / (A) Ourives / (E) Viajante / (P) Vice-Xerife",
    "(H) Sapateiro(a) / (A) Pastor(a) / (E) Viajante / (P) Vice-Xerife",
    "(H) Selvagem / (A) Pastor(a) / (E) Viajante / (P) Vice-Xerife",
    "(H) Soldado / (A) Pastor(a) / (E) Viajante / (P) Vice-Xerife",
    "(H) Taxidermista / (A) Pedreiro(a) / (E) Vinhateiro(a) / (P) Vice-Xerife",
    "(H) Tecelão(ã) / (A) Pedreiro(a) / (E) Vinhateiro(a) / (P) Vigia da fronteira",
    "(H) Torturador(a) / (A) Pedreiro(a) / (E) Vinhateiro(a) / (P) Vigia da fronteira",
    "(H) Treinador(a) de Animal / (A) Exterminador de pragas / (E) Vinhateiro(a) / (P) Vigia da fronteira",
    "(H) Trombadinha / (A) Exterminador de pragas / (E) Xamã / (P) Vigia da fronteira",
    "(H) Vigarista / (A) Runomante / (E) Xamã / (P) Vigia da fronteira",
    "(H) Vigia noturno / (A) Runomante / (E) Xamã / (P) Cervejeiro(a)",
    "(H) Xamã / (A) Runomante / (E) Xamã / (P) Guarda das colinas"]

motivacao_lista = [
    "Fugitivo: Por que fugiu? Como fugiu? De quem você foge.",
    "Condenado ao Ostracismo: De onde você vem? Por que foi banido?",
    "Nativo no limite da resiliência: O que você busca? O que te fez chegar nesse ponto?",
    "Aventureiro profissional: Por que esse lugar?",
    "Pagando promessa: Qual foi sua promessa? Você está aqui para cumpri-la ou pagá-la?",
    "Sonhos te trouxeram: Que sonhos foram esses?",
    "Emissário: Você vem de longe representando os anseios de seu povo. Do que seu povo precisa?",
    "Movido por curiosidade: Você quer responder a uma grande pergunta. Qual é essa pergunta?",
    "Espírito explorador: Você quer conquistar o espaço.",
    "Missão religiosa: Quem é seu deus e qual sua missão?",
    "Interesse zoológico: Pretende catalogar espécies. Por que se interessa tanto por eles. Há alguma espécie em específico?",
    "Interesse antropológico: Pretende conhecer povos humanoides e como vivem. Por que se interessa tanto por eles? Há algum povo em específico?",
    "Interesse místico: Deseja entender os segredos místicos e cosmológicos que repousam nesse lugar. Quais mistérios deseja desvendar?",
    "Interesse botânico: Deseja estudar espécies dos ermos. Se interessa por alguma planta especifica?",
    "Interesse psicotrópico: Deseja estudar substâncias alucinógenas. Alguma em especial? Qual sua relação com essas substâncias?",
    "Autoconhecimento: Busca a jornada para se conhecer melhor. Quais questões você busca resolver?",
    "Antiquário: Desejo de conhecer ou acumular relíquias de outras épocas e importância histórica. Tem alguma relíquia que busca em especial?",
    "Cronista: Quer conhecer e registrar a história dos povos e do mundo. Interesse específico em alguma lenda? O que pretende fazer com seus registros?",
    "Interesse arcano: Desejo de conhecer artefatos mágicos e conhecimentos arcanos esquecidos. Em busca de algo específico? Algum conhecimento em especial?",
    "Bardo: Pretende viver e relatar suas experiências para fins artísticos. Qual sua arte? Qual sua criação preferida?",
    "Interesse geográfico: Pretende conhecer marcos geográficos da região. Algum lugar especial que queira visitar?",
    "Cartógrafo: Você ama ler e fazer mapas. Você mapeia locais específicos ou regiões? Tem algum lugar específico que você queira mapear?",
    "Ganância: Riqueza acima de tudo é o que te move. O que pretende fazer com as riquezas que encontrar?",
    "Riqueza Altruística: Você veio para conseguir riquezas para ajudar numa causa nobre. Que causa é essa?"
]

def roll_attribute() -> int:
    return sum(random.randint(1, 6) for _ in range(3))

def calculate_modifier(attribute_value: int) -> int:
    if attribute_value == 3:
        return -3
    elif 4 <= attribute_value <= 5:
        return -2
    elif 6 <= attribute_value <= 8:
        return -1
    elif 9 <= attribute_value <= 12:
        return 0
    elif 13 <= attribute_value <= 15:
        return 1
    elif 16 <= attribute_value <= 17:
        return 2
    elif attribute_value == 18:
        return 3
    else:
        return 0

def generate_character(update: Update, context: CallbackContext) -> str:
    while True:
        attributes = {}

        for attribute_name in ['Força', 'Destreza', 'Constituição', 'Inteligência', 'Sabedoria', 'Carisma']:
            attribute_value = roll_attribute()
            modifier = calculate_modifier(attribute_value)
            ocu = random.choice(ocupacao_lista)
            aug = random.choice(augurio_lista)
            po = sum(random.randint(1, 6) for _ in range(3)) * 10
            mo = random.choice(motivacao_lista)
            attributes[attribute_name] = {
                'Valor': attribute_value,
                'Modificador': modifier
            }
        total_modifiers = sum(attribute['Modificador'] for attribute in attributes.values())

        if total_modifiers > 0:
            response = '*Personagem gerado:*\n'
            for attribute_name, attribute_info in attributes.items():
                response += f'*{attribute_name}:* {attribute_info["Valor"]} (Modificador: {attribute_info["Modificador"]})\n'

            response += f'\n*Total dos Modificadores:* {total_modifiers}\n'
            response += f'\n*Ouro:* {po}\n\n*Ocupação:* _{ocu}_\n\n*Augúrio:* _{aug}_\n\n*Motivação:* _{mo}_\n'

            return response
            break


async def dn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = generate_character(update, context)
    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    print('Iniciando...')

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('dn', dn_command))

    print('Polling')
    app.run_polling(poll_interval=3)
