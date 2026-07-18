from pyrogram import Client, filters
from pyrogram.types import ForceReply
from pyrogram.types import Message, CallbackQuery
import config
from keyboards import (
    kb_main, main_menu, ppt_menu, historia_inicio,
    capitulo1_menu, capitulo2_guerra_menu,
    capitulo2_aldea_menu, final_menu, btn_image, ppt_menu, btn_start, btn_info, btn_date, btn_menu, numero_menu
)
import random
from datetime import datetime
from FusionBrain_AI import generate
import base64

bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="my_bot"
)

def button_filter(button):
    async def func(_, __, msg):
        return msg.text == button.text
    return filters.create(func, "ButtonFilter", button=button)

# --- Comando /start ---
@bot.on_message(filters.command('start'))
@bot.on_message (button_filter(btn_start))
async def start_command(bot, message: Message):
    # Enviar mensaje con saludo
    await message.reply_text(
        "👋 ¡Hola, bienvenido!\n\n"
        "Comando de inicio:\n"
        "• /info — Ver información del bot\n\n",
        reply_markup=kb_main
    )
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker="CAACAgIAAxkBAAEPXp5oxeHBDvoGKvNx5L7ki7bEPkROdAACBQADwDZPE_lqX5qCa011NgQ")

# --- Comando /info ---
@bot.on_message(filters.command('info'))
@bot.on_message (button_filter(btn_info))
async def info_command(bot, message: Message):
        await message.reply(
            "Aquí tienes una descripción de lo que puede hacer este bot y una lista de comandos:\n\n"
            "• /start - Muestra mensaje de bienvenida\n"
            "• /info - Información del bot\n"
            "• /date - Hora y fecha actual\n"
            "• /image - Genera una imagen\n"
            "• /menu - Juegos e historias interactivas\n"
        )

# --- Comando /menu ---
@bot.on_message(filters.command("menu"))
@bot.on_message (button_filter(btn_menu))
async def menu_command(bot, message: Message):
    await message.reply_text(
         "Elige una opción del menú para comenzar:\n",
            reply_markup=main_menu
    )

# --- Comando /date ---
@bot.on_message(filters.command("date"))
@bot.on_message (button_filter(btn_date))
async def date_command(bot, message: Message):
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    await message.reply_text(f"🕒 Fecha y hora actual:\n{ahora}")

# --- Generador imagenes ---
query_text = "Introduce una solicitud para generar una imágen:"
@bot.on_message(filters.command("image"))
@bot.on_message(button_filter(btn_image))
async def image_command(bot, message):
    await message.reply(query_text, reply_markup=ForceReply(True))

@bot.on_message(filters.reply)
async def reply(bot, message):
    if message.reply_to_message.text == query_text:
        query = message.text
        await message.reply_text(f"Generando una imagen a petición '{query}'. Espera un momento...")

        images = await generate(query)
        if images:
            image_data = base64.b64decode(images[0])
            img_num = random.randint(1, 99)
            with open(f"images/image{img_num}.jpg", "wb") as file:
                file.write(image_data)
            await bot.send_photo(message.chat.id, f'images/image{img_num}.jpg',
                                 reply_to_message_id=message.id,
                                 reply_markup=kb_main)
        else:
            await message.reply_text("Surgió un error, prueba otra vez",
                                     reply_to_message_id=message.id,
                                     reply_markup=kb_main)

# --- Callbacks ---
@bot.on_callback_query()
async def callback_handler(bot, callback: CallbackQuery):
    data = callback.data

    # --- PPT ----
    if data == data == "juego":
        await callback.message.edit_text(
            "🎮 ¡Juguemos Piedra, Papel o Tijeras!\nElige una opción:",
            reply_markup=ppt_menu
        )

    elif data in ["piedra", "papel", "tijeras"]:
        opciones = ["piedra", "papel", "tijeras"]
        bot_choice = random.choice(opciones)
        resultado = "🤝 ¡Empate!" if data == bot_choice else (
            "🏆 ¡Ganaste!" if
            (data == "piedra" and bot_choice == "tijeras") or
            (data == "papel" and bot_choice == "piedra") or
            (data == "tijeras" and bot_choice == "papel")
            else "😿 Perdiste..."
        )

        await callback.message.edit_text(
            f"Tú elegiste: {data}\nYo elegí: {bot_choice}\n\n{resultado}",
            reply_markup=ppt_menu
        )
    #--- Adivina número ---
    if data == data == "numero":
        numero_secreto = random.randint(1, 10)
        await callback.message.edit_text(
            "He pensado en un número del 1 al 10 🤔\n¡Toca uno para intentar adivinarlo!",
            reply_markup=numero_menu
        )

    elif data in ["num_1", "num_2", "num_3", "num_4", "num_5", "num_6", "num_7", "num_8", "num_9", "num_10"]:
        numeros = ["num_1", "num_2", "num_3", "num_4", "num_5", "num_6", "num_7", "num_8", "num_9", "num_10"]
        bot_choice = random.choice(numeros)
        resultado = "🎯 ¡Correcto! Me leíste la mente." if data == bot_choice else (
            "😝 No tienes certeza de lo que pasa en mi cabeza"
        )

        await callback.message.edit_text(
            f"🧠 Pensé en: {bot_choice}\n 👆 Tú presionaste: {data}\n\n{resultado}",
            reply_markup=numero_menu
        )

    # --- Historia: Introducción ---
    if data == "historia":
        await callback.message.edit_text(
            "📜 *Saga del Guerrero del Norte*\n\n"
            "¡Saludos, joven vikingo! ⚔️\n"
            "Los dioses observan desde Asgard mientras las nubes anuncian guerra.\n"
            "¿Estás listo para escribir tu destino?",
            reply_markup=historia_inicio
        )

    # --- Capítulo 1 ---
    elif data == "capitulo1":
        await callback.message.edit_text(
            "🌊 *Capítulo I: El llamado del destino*\n\n"
            "El cuerno de guerra resuena desde el fiordo. Tu clan se prepara para el combate.\n"
            "Los ancianos te miran en silencio, esperando tu decisión...\n\n"
            "¿Responderás al llamado del combate o protegerás tu hogar?",
            reply_markup=capitulo1_menu
        )

    # --- Capítulo 2A: Camino de la guerra ---
    elif data == "capitulo2_guerra":
        await callback.message.edit_text(
            "🔥 *Capítulo II: Camino de la guerra*\n\n"
            "Marchas hacia la batalla bajo una tormenta de nieve. El enemigo se aproxima...\n"
            "Los dioses miran desde el Valhalla.\n\n"
            "¿Atacas con furia o esperas una oportunidad táctica?",
            reply_markup=capitulo2_guerra_menu
        )

    # --- Capítulo 2B: Proteger la aldea ---
    elif data == "capitulo2_aldea":
        await callback.message.edit_text(
            "🏠 *Capítulo II: El guardián del norte*\n\n"
            "Mientras los guerreros parten, tú reúnes a los aldeanos.\n"
            "El enemigo puede llegar en cualquier momento...\n\n"
            "¿Lucharás hasta el final o evacuarás a tu gente?",
            reply_markup=capitulo2_aldea_menu
        )

    # --- Capítulo 3 finales ---
    elif data == "capitulo3_valhalla":
        await callback.message.edit_text(
            "⚔️ *Final: Gloria en el Valhalla*\n\n"
            "Tu espada brilla en el campo de batalla. Caen enemigos a tu paso.\n"
            "Una flecha atraviesa el cielo… y tu destino está sellado.\n\n"
            "Los dioses te reciben con honor en el Valhalla. 🕯️",
            reply_markup=final_menu
        )

    elif data == "capitulo3_tactico":
        await callback.message.edit_text(
            "🧠 *Final: El estratega del norte*\n\n"
            "Esperaste el momento perfecto. Tus aliados llegaron justo a tiempo.\n"
            "La victoria es tuya, joven vikingo. Pero recuerdas que el precio del honor es la soledad.",
            reply_markup=final_menu
        )

    elif data == "capitulo3_heroico":
        await callback.message.edit_text(
            "🔥 *Final: El héroe de la aldea*\n\n"
            "Luchaste hasta el último aliento para proteger tu hogar.\n"
            "Tu nombre será recordado por generaciones como el mejor de todos. 🐺",
            reply_markup=final_menu
        )

    elif data == "capitulo3_sabio":
        await callback.message.edit_text(
            "🌄 *Final: El sabio protector*\n\n"
            "Guiaste a tu gente hacia las montañas y sobrevivieron al invierno.\n"
            "A veces, la verdadera valentía es saber cuándo no luchar. 🌿",
            reply_markup=final_menu
        )

    # --- Volver al menú principal ---
    elif data == "back_main":
        await callback.message.edit_text(
            "🏠 Menú principal:",
            reply_markup=main_menu
        )

    # --- Cerrar ---
    if data == "close":
        await callback.message.edit_text("👋 ¡Hasta luego, guerrero del norte! 🌌")

# --- Función Echo ---
@bot.on_message(filters.text & ~filters.command(["start", "info", "date", "image","menu"]))
async def echo_message(bot, message: Message):
    user_text = message.text
    await message.reply_text(f"📩 Lo recibí: {user_text}")

# ---------------- Ejecutar bot ----------------
print("🤖 Bot en marcha...")
bot.run()