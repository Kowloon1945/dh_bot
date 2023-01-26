from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from create_bot import bot, dp, p2p
from keyboards import kb_client, vibor_merch, tov_line_fut_uch, tov_line_fut_pent, tov_line_fut_stal, tov_line_tol_uch, tov_line_tol_pent, cb, korzina_kb, size_kb
import string
import sqlite3


items={'fut_uch':{'name':'Футболка Учение', 'price':1937}, 'fut_pent':{'name':'Футболка Пентаграмма', 'price':1937},
       'fut_stal':{'name':'Футболка Сталинеш', 'price':1937}, 'tol_uch':{'name':'Худи Учение', 'price':4000}, 'tol_pent':{'name':'Худи Пентаграмма', 'price':4000}}
# size = {'xs':'XS', 's':'S', 'm':'M', 'l':'L', 'xl':'XL', '2xl':'2XL', '3xl':'3XL', '4xl':'4XL', '5xl':'5XL'}

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    # connect = sqlite3.connect('korzina_dh.db')
    # cursor = connect.cursor()
    # # cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE, name TEXT)')
    # # cursor.execute('CREATE TABLE IF NOT EXISTS cart(user_id INTEGER, product_id INTEGER)')
    # # cursor.execute('CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER)')
    # cursor.execute('INSERT INTO korzina(user_id, item) VALUES (?, ?)', [message.from_user.id, message.chat.first_name])
    # cursor.close()
    # connect.commit()
    # connect.close()
    await bot.send_photo(message.from_user.id, types.InputFile(r'src\photo_menu.jpg'), caption='Привет! Это бот для заказа футболок и худи от издательства DHARMA1937. Перед заказом прочти, пожалуйста, дисклеймер', reply_markup=kb_client)


# @dp.message_handler(commands=['Открыть_каталог'])
async def katalog(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выбери мерч', reply_markup=vibor_merch)

# @dp.message_handler(commands=['Обратная_связь'])
async def obr_svyaz(message : types.Message):
    await bot.send_message(message.from_user.id, 'Контакты обратной связи')

# @dp.message_handler(commands=['Корзина'])
async def korzina(message : types.Message):
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    tovari = cursor.execute('SELECT item FROM korzina WHERE user_id=(?)', [message.from_user.id]).fetchall()
    ceni = cursor.execute('SELECT price FROM korzina WHERE user_id=(?)', [message.from_user.id]).fetchall()
    ItemsWithoutTuple = [i[0] for i in tovari]
    toviki = ', '.join(ItemsWithoutTuple)
    CeniWithoutTuple = [i[0] for i in ceni]
    cennik = [int(item) for item in CeniWithoutTuple]
    global sum_cennik
    sum_cennik = sum(cennik)
    cursor.close()
    connect.commit()
    await bot.send_message(message.from_user.id, f'Ваши товары: {toviki}\nЦены: {sum_cennik}руб.', reply_markup=korzina_kb)


@dp.callback_query_handler(cb.filter(id='1'))
async def kupit_fut_uch(callback_query : types.CallbackQuery, callback_data : dict):
    await callback_query.answer(cache_time=10)
    product = items['fut_uch']['name']
    product_price = items['fut_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', (user_id, product, product_price))
    cursor.close()
    connect.commit()
    connect.close()
    await callback_query.message.answer('Выберите размер', reply_markup=size_kb)
    # await callback_query.message.answer('Футболка Учение добавлена в корзину')




@dp.callback_query_handler(cb.filter(id='2'))
async def kupit_fut_uch(callback_query : types.CallbackQuery, callback_data : dict):
    await callback_query.answer(cache_time=10)

    product = items['fut_pent']['name']
    product_price = items['fut_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', [user_id, product, product_price])
    cursor.close()
    connect.commit()
    connect.close()

    await callback_query.message.answer('Футболка Пентаграмма добавлена в корзину')



@dp.callback_query_handler(cb.filter(id='3'))
async def kupit_fut_uch(callback_query : types.CallbackQuery, callback_data : dict):
    await callback_query.answer(cache_time=10)

    product = items['fut_stal']['name']
    product_price = items['fut_stal']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', [user_id, product, product_price])
    cursor.close()
    connect.commit()
    connect.close()

    await callback_query.message.answer('Футболка Сталинеш добавлена в корзину')

@dp.callback_query_handler(cb.filter(id='4'))
async def kupit_fut_uch(callback_query : types.CallbackQuery, callback_data : dict):
    await callback_query.answer(cache_time=10)

    product = items['tol_uch']['name']
    product_price = items['tol_uch']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', [user_id, product, product_price])
    cursor.close()
    connect.commit()
    connect.close()

    await callback_query.message.answer('Худи Учение добавлена в корзину')

@dp.callback_query_handler(cb.filter(id='5'))
async def kupit_fut_uch(callback_query : types.CallbackQuery, callback_data : dict):
    await callback_query.answer(cache_time=10)

    product = items['tol_pent']['name']
    product_price = items['tol_pent']['price']
    user_id = callback_query.from_user.id
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO korzina(user_id, item, price) VALUES(?, ?, ?)', [user_id, product, product_price])
    cursor.close()
    connect.commit()
    connect.close()

    await callback_query.message.answer('Худи Пентаграмма добавлена в корзину')




# @dp.message_handler(Command('Kupit'))
# async def kupit(message : types.Message):
#     connect = sqlite3.connect('korzina.db')
#     cursor = connect.cursor()
#     data = cursor.execute('SELECT * FROM cart WHERE user_id=(?)', [message.from_user.id]).fetchall()
#     data_tovary = cursor.execute('SELECT product_id FROM cart WHERE user_id=(?)', [message.from_user.id]).fetchall()
#     cursor.close()
#     connect.commit()
#     cursor = connect.cursor()
#     new_data = []
#     for i in range(len(data)):
#         new_data.append(cursor.execute('SELECT * FROM products WHERE id=(?)', [data[i][1]]).fetchall())
#     cursor.close()
#     connect.commit()
#     connect.close()
#     new_data = [new_data[i][0] for i in range(len(new_data))]
#     prices = [types.labeled_price.LabeledPrice(label=i[1], amount=i[2]) for i in new_data]
#     await bot.send_message(message.from_user.id, f'{data_tovary}')


@dp.callback_query_handler(text='razmer_fut')
async def razmer_fut(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\razmer_fut.jpg'))

@dp.callback_query_handler(text='razmer_tol')
async def razmer_tol(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\razmer_tol.jpg'))



@dp.callback_query_handler(text='fut_uch')
async def fut_uch(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\fut_uch.jpg'), caption='Футболка Учение\n\nФутболка прямого кроя с цитатой В. Ленина из работы «Три источника и три составных части марксизма». 100% хлопок. Унисекс\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны', reply_markup=tov_line_fut_uch)

@dp.callback_query_handler(text='fut_pent')
async def fut_uch(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\fut_pent.jpg'), caption='Футболка Пентаграмма\n\nФутболка с портретами Маркса, Ленина, Мао, Сталина и цитатой Ленина «Учение Маркса всесильно, потому что оно верно». 100% хлопок. Унисекс\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны', reply_markup=tov_line_fut_pent)


@dp.callback_query_handler(text='fut_stal')
async def fut_uch(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\fut_stal.jpg'), caption='Футболка Сталинеш\n\nФутболка прямого кроя с принтом И. Сталина в образе Ганеши. 100% хлопок. Унисекс\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны', reply_markup=tov_line_fut_stal)


@dp.callback_query_handler(text='tol_uch')
async def fut_uch(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\tol_uch.jpg'), caption='Худи Учение\n\nХуди с цитатой В. Ленина из работы «Три источника и три составных части марксизма». Унисекс 100% хлопок.\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны', reply_markup=tov_line_tol_uch)


@dp.callback_query_handler(text='tol_pent')
async def fut_uch(callback_query : types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\tol_pent.jpg'), caption='Худи Пентаграмма\n\nХуди с портретами Маркса, Ленина, Мао, Сталина и цитатой Ленина «Учение Маркса всесильно, потому что оно верно». Унисекс. 100% хлопок\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны', reply_markup=tov_line_tol_pent)

@dp.callback_query_handler(text='Ochistit_korzinu')
async def ochistit_korzinu(callback_query : types.CallbackQuery):
    connect = sqlite3.connect('korzina_dh.db')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM korzina WHERE user_id=(?)', [callback_query.from_user.id])
    cursor.close()
    connect.commit()
    connect.close()
    await bot.send_message(callback_query.from_user.id, 'Ваша корзина очищена')

@dp.callback_query_handler(text='Oformit_zakaz')
async def oformit_zakaz(callback_query : types.CallbackQuery):
    new_bill = await p2p.bill(amount=sum_cennik, lifetime=45)
    await bot.send_message(callback_query.from_user.id, new_bill.pay_url)
    if (await p2p.check(bill_id=new_bill.bill_id)).status is True:
        await bot.send_message(callback_query.from_user.id, 'Ваш заказ оплачен')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(katalog, commands=['Открыть_каталог'])
    dp.register_message_handler(obr_svyaz, commands=['Обратная_связь'])
    dp.register_message_handler(korzina, commands=['Корзина'])





