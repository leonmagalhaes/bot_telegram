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
    # ... (demais itens da lista)
    "(H) Xamã / (A) Runomante / (E) Xamã / (P) Guarda das colinas"
]

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

def generate_retainer(update: Update, context: CallbackContext) -> str:
    attributes = {}
    for attribute_name in ['Força', 'Destreza', 'Constituição', 'Inteligência', 'Sabedoria', 'Carisma']:
        attribute_value = roll_attribute()
        modifier = calculate_modifier(attribute_value)
        attributes[attribute_name] = {
            'Valor': attribute_value,
            'Modificador': modifier
        }
    total_modifiers = sum(attribute['Modificador'] for attribute in attributes.values())
    response = '*Aprendiz gerado:*\n'
    for attribute_name, attribute_info in attributes.items():
        response += f'*{attribute_name}:* {attribute_info["Valor"]} (Modificador: {attribute_info["Modificador"]})\n'
    response += f'\n*Total dos Modificadores:* {total_modifiers}\n'
    return response

async def dn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = generate_character(update, context)
    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)

async def for_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = generate_retainer(update, context)
    await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    print('Iniciando...')

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('dn', dn_command))
    app.add_handler(CommandHandler('for', for_command))

    print('Polling')
    app.run_polling(poll_interval=3)
