from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup
from pyrogram import emoji

btn_start= KeyboardButton(f'{emoji.ROCKET} start')
btn_info = KeyboardButton(f'{emoji.INFORMATION} info')
btn_menu = KeyboardButton(f'{emoji.ALIEN_MONSTER} menú')
btn_date = KeyboardButton(f'{emoji.ALARM_CLOCK} date')
btn_image = KeyboardButton(f'{emoji.PEN} image')

kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [btn_start, btn_info, btn_date], [btn_image], [btn_menu]
    ],
    resize_keyboard=True
)

# --- Menú principal ---
main_menu = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("🗿📄✂️ PPT", callback_data="juego")],
        [InlineKeyboardButton("🔢 Adivina el número", callback_data="numero")],
        [InlineKeyboardButton("📜 Historia", callback_data="historia")],
        [InlineKeyboardButton("❌ Cerrar", callback_data="close")]
    ]
)

# --- Menú del juego Piedra, Papel o Tijeras ---
ppt_menu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🪨 Piedra", callback_data="piedra"),
            InlineKeyboardButton("📄 Papel", callback_data="papel"),
            InlineKeyboardButton("✂️ Tijeras", callback_data="tijeras")
        ],
        [InlineKeyboardButton("⬅️ Volver", callback_data="back_main")]
    ]
)

# --- Menú de Adivina el número ---
numero_menu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("1️⃣", callback_data="num_1"),
            InlineKeyboardButton("2️⃣", callback_data="num_2"),
            InlineKeyboardButton("3️⃣", callback_data="num_3"),
            InlineKeyboardButton("4️⃣", callback_data="num_4"),
            InlineKeyboardButton("5️⃣", callback_data="num_5"),
        ],
        [
            InlineKeyboardButton("6️⃣", callback_data="num_6"),
            InlineKeyboardButton("7️⃣", callback_data="num_7"),
            InlineKeyboardButton("8️⃣", callback_data="num_8"),
            InlineKeyboardButton("9️⃣", callback_data="num_9"),
            InlineKeyboardButton("🔟", callback_data="num_10"),
        ],
        [InlineKeyboardButton("⬅️ Volver", callback_data="back_main")]
    ]
)

# --- Historia: Introducción ---
historia_inicio = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⚔️ Adelante", callback_data="capitulo1"),
            InlineKeyboardButton("🚪 No, gracias", callback_data="back_main")
        ]
    ]
)

# --- Capítulo 1: El llamado del destino ---
capitulo1_menu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🏹 Ir a la guerra", callback_data="capitulo2_guerra"),
            InlineKeyboardButton("🏠 Proteger la aldea", callback_data="capitulo2_aldea")
        ],
        [InlineKeyboardButton("⬅️ Volver al inicio", callback_data="historia")]
    ]
)

# --- Capítulo 2A: Camino de la guerra ---
capitulo2_guerra_menu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⚔️ Atacar sin miedo", callback_data="capitulo3_valhalla"),
            InlineKeyboardButton("🛡️ Esperar refuerzos", callback_data="capitulo3_tactico")
        ],
        [InlineKeyboardButton("⬅️ Volver al menú principal", callback_data="back_main")]
    ]
)

# --- Capítulo 2B: Proteger la aldea ---
capitulo2_aldea_menu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔥 Defender hasta el final", callback_data="capitulo3_heroico"),
            InlineKeyboardButton("🏃‍♂️ Evacuar a los aldeanos", callback_data="capitulo3_sabio")
        ],
        [InlineKeyboardButton("⬅️ Volver al menú principal", callback_data="back_main")]
    ]
)

# --- Finales ---
final_menu = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("🔁 Reiniciar historia", callback_data="historia")],
        [InlineKeyboardButton("🏠 Volver al menú principal", callback_data="back_main")]
    ]
)
