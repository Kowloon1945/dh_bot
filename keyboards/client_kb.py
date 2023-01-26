from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

# первичная клавиатура
katalog_btn = KeyboardButton('/Открыть_каталог')
obr_svyaz = KeyboardButton('/Обратная_связь')
korzina = KeyboardButton('/Корзина')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(katalog_btn).add(obr_svyaz).add(korzina)


# стартовые кнопки выбора мерча
fut_uch = InlineKeyboardButton('Футболка Учение', callback_data='fut_uch')
fut_pent = InlineKeyboardButton('Футболка Пентаграмма', callback_data='fut_pent')
fut_stal = InlineKeyboardButton('Футболка Сталинеш', callback_data='fut_stal')
tol_uch = InlineKeyboardButton('Худи Учение', callback_data='tol_uch')
tol_pent = InlineKeyboardButton('Худи Пентаграмма', callback_data='tol_pent')

vibor_merch = InlineKeyboardMarkup(row_width=2)

vibor_merch.add(fut_uch).add(fut_pent).add(fut_stal).add(tol_uch).add(tol_pent)

tov_line_fut_uch = InlineKeyboardMarkup()
tov_line_fut_pent = InlineKeyboardMarkup()
tov_line_fut_stal = InlineKeyboardMarkup()
tov_line_tol_uch = InlineKeyboardMarkup()
tov_line_tol_pent = InlineKeyboardMarkup()

cb = CallbackData('kupit', 'id')
# кнопки 'купить' для каждого товара
kupit_fut_uch = InlineKeyboardButton('Купить', callback_data='kupit:1')
kupit_fut_pent = InlineKeyboardButton('Купить', callback_data='kupit:2')
kupit_fut_stal = InlineKeyboardButton('Купить', callback_data='kupit:3')
kupit_tol_uch = InlineKeyboardButton('Купить', callback_data='kupit:4')
kupit_tol_pent = InlineKeyboardButton('Купить', callback_data='kupit:5')

# размеры
razmer_fut = InlineKeyboardButton('Узнать размер', callback_data='razmer_fut')
razmer_tol = InlineKeyboardButton('Узнать размер', callback_data='razmer_tol')

tov_line_fut_uch.row(kupit_fut_uch, razmer_fut)
tov_line_fut_pent.row(kupit_fut_pent, razmer_fut)
tov_line_fut_stal.row(kupit_fut_stal, razmer_fut)

tov_line_tol_uch.row(kupit_tol_uch, razmer_tol)
tov_line_tol_pent.row(kupit_tol_pent, razmer_tol)

# кнопки для корзины
korzina_kb = InlineKeyboardMarkup(row_width=2)

Kupit = InlineKeyboardButton('Оформить заказ', callback_data='Oformit_zakaz')
Ochist_korz = InlineKeyboardButton('Очистить корзину', callback_data='Ochistit_korzinu')

korzina_kb.row(Kupit, Ochist_korz)

#
# xs = InlineKeyboardButton(text='xs', callback_data='xs')
# s = InlineKeyboardButton(text='s', callback_data='s')
# m = InlineKeyboardButton(text='m', callback_data='m')
# l = InlineKeyboardButton(text='l', callback_data='l')
# xl = InlineKeyboardButton(text='xl', callback_data='xl')
# xxl = InlineKeyboardButton(text='2xl', callback_data='xxll')
# xxxl = InlineKeyboardButton(text='3xl', callback_data='xxxl')
# xxxxl = InlineKeyboardButton(text='4xl', callback_data='xxxxl')
# xxxxxl = InlineKeyboardButton(text='5xl', callback_data='xxxxxl')
#
# size_kb = InlineKeyboardMarkup(row_width=2)
# size_kb.row(xs, s).row(m, l).row(xl, xxl).row(xxxl, xxxxl).add(xxxxxl)
