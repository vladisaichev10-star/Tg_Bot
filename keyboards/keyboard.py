from pyrogram.types import ReplyKeyboardMarkup
from buttons import main_btns, menu_btns, film_btns


menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[menu_btns],
    resize_keyboard=True
)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[main_btns],
    resize_keyboard=True
)

film_keyboard = ReplyKeyboardMarkup(
    keyboard=[film_btns],
    resize_keyboard=True
)
