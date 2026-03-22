from pyrogram.types import KeyboardButton
from pyrogram import emoji

# MAIN_MENU

main_btn = KeyboardButton(f"Основное")
films_btn = KeyboardButton(f"Кино")

menu_btns = [main_btn, films_btn]

# MAIN
date_time_btn = KeyboardButton(f"Дата/Время")
date_btn = KeyboardButton(f" {emoji.CALENDAR} Дата")
time_btn = KeyboardButton(f" {emoji.TIMER_CLOCK} Время")
help_btn = KeyboardButton("Помощь")

main_btns = [date_time_btn, date_btn, time_btn, help_btn]

# FILM_KEYBOARD

random_btn = KeyboardButton(f"Рандом")
search_btn = KeyboardButton(f"Поиск")

film_btns = [random_btn, search_btn]
