import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from buttons import *
from aiogram.types import CallbackQuery
from classlar import Sql
import os 
from aiogram.contrib.fsm_storage.memory import MemoryStorage 
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup 
from aiogram.dispatcher.filters import Text
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Sql()



class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    surname = State()
    number = State()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	db.baza_create()
	global user_id
	user_id = message.from_user.id
	username = message.from_user.username
	first_name = message.from_user.first_name
	fo = db.id_user(user_id)
	if fo is None:
		db.user_add(user_id,username,first_name)
		await message.answer_photo(
        photo = open('images/key.jpg','rb'),
        caption = """Бот-сайт предназначен для трудоустройства кандидатов в сеть магазинов "BUTTON"
        """,reply_markup=keyb)
	else:
		await message.answer_photo(
        photo = open('images/key.jpg','rb'),
        caption = """Бот-сайт предназначен для трудоустройства кандидатов в сеть магазинов "BUTTON"
        """,reply_markup=keyb)




@dp.message_handler(text="🏢 Kompaniya haqida")
async def send_welcome(message: types.Message):
	await message.answer_photo(
        photo = open('images/key2.jpg','rb'),
        caption = f"""Button erkaklar va ayollar kiyim do'koni!"
Button kompaniyasiga 2019 yil 21-Mart kuni asos solingan." 
Hozirgi kunda 1 ta filliali mavjud  Toshkent shahrida joylashgan.
\n
Afzalliklari:

☑️ Yuqori sifat;

☑️Keng assortiment;

☑️Hamyonbop narxlar.""",parse_mode='HTML',reply_markup = keyb2)

#####------------------------1
@dp.message_handler(text="📍 Filialimiz")
async def send_welcome(message: types.Message):
	await message.answer("Joylashuvingizni yuboring",reply_markup = keyb3)
   
@dp.message_handler(content_types = ['location'])
async def contact(message: types.Message):
	kor1 = message.location.latitude
	kor2 = message.location.longitude
	db.location_update(user_id,kor1,kor2)
	await message.answer_photo(
	photo = open('images/locat.jpg','rb'),
    caption = f"""Uzbekistan, Tashkent,  Olmazorskiy rayon, maxallya Universitet
+998951443555""")
   

##----------------------------2
@dp.message_handler(text="💼 Bo'sh ish o'rinlari")
async def send_welcome(message: types.Message):
	await message.answer("""Ushbu bot bo'limi "Button" kompaniyasida so'rovnomani to'ldirish✍️"  va ishga joylashish uchun mo'ljallangan!\n
		Bu erda siz anketani to'ldirishingiz📄 va "
		kompaniyamizdagi mavjud vakansiyalarni ko'rishingiz mumkin!""",reply_markup = bosh)

@dp.message_handler(text="🏢 Bosh ofis")
async def send_welcome(message: types.Message):
	await message.answer( f"""Manzil: Uzbekistan, Tashkent,  Olmazorskiy rayon, maxallya Universitet\nIsh vaqti 10:00-22:00(har kuni)\nMurojat uchun:+998951443555""",parse_mode='HTML',reply_markup = bosh1)
			


@dp.message_handler(commands=['ish'],state=None)
async def send_welcome(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Rezumingizni tashen rasm qib jpg yoki jpeg formatda')


@dp.message_handler(content_types=['photo'],state=FSMAdmin.photo)
async def load_photo(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id 
    await FSMAdmin.next()
    await message.reply("Ismingizni qiriting")


@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text 
    await FSMAdmin.next()
    await message.reply("Familiya kiriting")

@dp.message_handler(state=FSMAdmin.surname)
async def load_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text 
    await FSMAdmin.next()
    await message.reply("Endi telefon raqamingizni qiriting")


@dp.message_handler(state=FSMAdmin.number)
async def load_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = int(message.text) 
    async with state.proxy() as data:
        await message.answer_photo( photo = data['photo'])
        await message.answer(f" Ismi: {data['name']}\n Familiya: {data['surname']} \n Telefon raqami: {data['number']}")
    await state.finish()

			### Xavfsizlik
@dp.message_handler(text="Xavfsizlik xodimi")
async def send_welcome(message: types.Message):
	await message.answer("""Мужчина 20-30.
Знание узбекского и русского языка.
Опыт работы в охранной системе приветствуется.
Образование не ниже средне-специального.
Ответственность, внимательность, вежливость, пунктуальность, опрятный внешний вид.""",reply_markup = xavfsizlik)
	await message.answer("Jinsni tanlang",reply_markup = xavfsizlik)

			#### Sotuvchiiiiiiiiiiiii
@dp.message_handler(text="Sotuvchi-maslahatchi")
async def send_welcome(message: types.Message):
	await message.answer("""Требуемый опыт работы: от 1 года


Полная занятость, полный день

Обязанности:

- Вежливое обслуживание посетителей в торговом зале;
- Предоставление консультаций касательно продукции;
- Сопровождение покупателя к кассе;
- Предпродажная подготовка товара;
- Подготовка торгового зала к работе;
- Поддержание порядка и чистоты в магазине;
- Участие в инвентаризации

Требования:
- Грамотная речь;
- Опыт работы значения не имеет, идёт полное обучение в сфере продаж;
- Дисциплинированность, ответственность;
- Владение узбекским и русским языками""",reply_markup = sotuvchi)
	await message.answer("Jinsni tanlang",reply_markup = sotuvchi)



			### Kassir
@dp.message_handler(text="Kassir")
async def send_welcome(message: types.Message):
	await message.answer(""" Требуемый опыт работы: 1–3 года

Полная занятость, полный день

Обязанности:
- Вежливое обслуживание покупателей;
- Ведение и учет кассовых документов;
- Обеспечение сохранности денежных средств, находящихся в кассе;
- Работать с наличной и безналичной формой оплаты;
- Сверка количества наличных средств в контрольно-кассовой машине (ККМ);
- Обеспечение кассовой дисциплины.

Требования:

- Опыт работы на аналогичной позиции до 1 года;

- Грамотность, стрессоустойчивость, внимательность, точность;
- Дисциплинированность;
- Владение узбекским и русским языками.
- Умение работать с кассовым аппаратом и терминалом.

Условия:

- График работы: 6/1;
- Обед и ужин за счёт компании;
- Дружный коллектив.""",reply_markup = kassir)
	await message.answer("Jinsni tanlang",reply_markup = kassir)


				######### Qoriqchiii
@dp.message_handler(text="Qo'riqchi,qo'riqchi qiz")
async def send_welcome(message: types.Message):
	await message.answer("""ТРЕБОВАНИЯ:
опыт работы не требуется
возраст от 25-35 лет
образование - высшее или среднее-специальное
ответственность.
УСЛОВИЯ:
обед/ужин за счет работодателя;
график работы:6/1 с 10:00 до 16:00; с 16:00 до 00:00;
официальное трудоустройство;""",reply_markup = qoriqchi)
	await message.answer("Jinsni tanlang",reply_markup = qoriqchi)



#### Tozalovchi
@dp.message_handler(text="Tozalovchi")
async def send_welcome(message: types.Message):
	await message.answer(""" Обязанности:
- уборка служебных помещений;
Требования:
- чистоплотность;
- аккуратность;
- ответственность;
- вежливость.
Условия работы:
- график работы 6/1 с 10:00 до 18:00
с 14:00 до 22:00
- своевременная выплата з/п от 1 млн;
- комфортабельный офис;
- дружный коллектив;
- обед и ужин за счёт компании,""",reply_markup = tozalovchi)
	await message.answer("Jinsni tanlang",reply_markup = tozalovchi)


#####----------------------------3
@dp.message_handler(text="💬 Отзывы и предложения")
async def send_welcome(message: types.Message):
	await message.answer("""Bu yerda bizga yozing, biz albatta javob beramiz.""",reply_markup = ort)

####-----------------------------4
@dp.message_handler(text="☎️Kontaktlar/Manzili")
async def send_welcome(message: types.Message):
	await message.answer_photo(
        photo = open('images/gruppa.jpg','rb'),
        caption = """ 😊 Bizga qo'ng'iroq qiling"
 📞 +998 94 613 5555"

✉️ buttonuz@gmail.com"

⏰ Ish soatlari:"
Db-Yab: 10:00 - 22:00""")
	

	##------------1 Asosiy ortga
@dp.message_handler(text="⬅️ Ortga")
async def send_welcome(message: types.Message):
	await message.answer_photo(
        photo = open('images/key.jpg','rb'),
        caption = """Бот-сайт предназначен для трудоустройства кандидатов в сеть магазинов "BUTTON"
        """,reply_markup=keyb)

@dp.message_handler(text="◀️ Ortga")
async def send_welcome(message: types.Message):
	await message.answer_photo(
        photo = open('images/key2.jpg','rb'),
        caption = f"""Button erkaklar va ayollar kiyim do'koni!"
Button kompaniyasiga 2019 yil 21-Mart kuni asos solingan." 
Hozirgi kunda 1 ta filliali mavjud  Toshkent shahrida joylashgan.
\n
Afzalliklari:

☑️ Yuqori sifat;

☑️Keng assortiment;

☑️Hamyonbop narxlar.""",parse_mode='HTML',reply_markup = keyb2)

@dp.message_handler(text="◀️ Ortga")
async def send_welcome(message: types.Message):
	await message.answer_photo(
	photo = open('images/locat.jpg','rb'),
    caption = f"""Uzbekistan, Tashkent,  Olmazorskiy rayon, maxallya Universitet
+998951443555""")


		###-----------------2
@dp.message_handler(text="⬅️ Ortga")
async def send_welcome(message: types.Message):
	await message.answer("""Ushbu bot bo'limi "Button" kompaniyasida so'rovnomani to'ldirish✍️"  va ishga joylashish uchun mo'ljallangan!\n
		Bu erda siz anketani to'ldirishingiz📄 va "
		kompaniyamizdagi mavjud vakansiyalarni ko'rishingiz mumkin!""",reply_markup = bosh)

@dp.message_handler(text="🔼 Asosiy Menu")
async def send_welcome(message: types.Message):
	await message.answer_photo(
        photo = open('images/key.jpg','rb'),
        caption = """Бот-сайт предназначен для трудоустройства кандидатов в сеть магазинов "BUTTON"
        """,reply_markup=keyb)

@dp.message_handler(text="◀️Ortga")
async def send_welcome(message: types.Message):
	await message.answer("""Ushbu bot bo'limi "Button" kompaniyasida so'rovnomani to'ldirish✍️"  va ishga joylashish uchun mo'ljallangan!\n
		Bu erda siz anketani to'ldirishingiz📄 va "
		kompaniyamizdagi mavjud vakansiyalarni ko'rishingiz mumkin!""",reply_markup = bosh)
	
@dp.message_handler(text="⬅️Ortga")
async def send_welcome(message: types.Message):
	await message.answer( f"""Manzil: Uzbekistan, Tashkent,  Olmazorskiy rayon, maxallya Universitet\nIsh vaqti 10:00-22:00(har kuni)\nMurojat uchun:+998951443555""",parse_mode='HTML',reply_markup = bosh1)
	
@dp.message_handler(text="↩️ Ortga")
async def send_welcome(message: types.Message):
	await message.answer("Jinsni tanlang",reply_markup = admin)
				####---------------------------- TIl va Rus
@dp.message_handler(text="🇺🇿/🇷🇺 Язык")
async def send_welcome(message: types.Message):
	await message.answer("Tilni o'zgartirish",reply_markup = til)

@dp.message_handler(text="💬 Отзывы и предложения")
async def send_welcome(message: types.Message):
	await message.answer("""Bu yerda bizga yozing, biz albatta javob beramiz.""",reply_markup = ort)
	# @dp.message_handler(content_types = ['contact'])
# async def contact(message: types.Message):
# 	raqam = message.contact['phone_number']
# 	db.contact_update(user_id,raqam)
# 	await message.reply("Biz siz bilan tez orada aloqaga chiqamiz")

@dp.message_handler(text="🇺🇿 Узбекский")
async def send_welcome(message: types.Message):
	await message.answer_photo(
        photo = open('images/key.jpg','rb'),
        caption = """Бот-сайт предназначен для трудоустройства кандидатов в сеть магазинов "BUTTON"
        """,reply_markup=keyb)

@dp.message_handler(text="🇷🇺 Русский")
async def send_welcome(message: types.Message):
	await message.answer_photo(
        photo = open('images/key.jpg','rb'),
        caption = """Бот-сайт предназначен для трудоустройства кандидатов в сеть магазинов "BUTTON"
        """,reply_markup=r_keyb)
	

@dp.message_handler(text="🏢 О компании")
async def send_welcome(message: types.Message):
	await message.answer_photo(
        photo = open('images/key2.jpg','rb'),
        caption = f"""Button магазин мужской и женской одежды!
Компания Button была основана 21 марта 2019 года. В настоящее время существует 3 филиала, которые расположены в городе Ташкенте.

Преимущества:

☑️ Высокое качество;

☑️Широкий ассортимент;

☑️ Доступные цены.""",parse_mode='HTML',reply_markup = r_keyb2)

@dp.message_handler(text="📍 Наш филиал")
async def send_welcome(message: types.Message):
	await message.answer("Отправьте свое местоположение для определения ближайшего филиала",reply_markup = r_keyb3)



##----------------------------2
@dp.message_handler(text="💼  Вакансии")
async def send_welcome(message: types.Message):
	await message.answer("""Этот раздел БОТа предназначен для заполнения анкеты ✍️ и трудоустройства  в компанию Button!

Здесь Вы можете заполнить свою анкету 📄 и узнать о существующих вакансиях к нашей Компании!""",reply_markup = r_bosh)


@dp.message_handler(text="🏢 Головной Офис")
async def send_welcome(message: types.Message):
	await message.answer( f"""Адрес: Узбекистан, Ташкент,  Олмазорский район, махалля Университет

Режим работы: 10:00-22:00 (ЕЖЕДНЕВНО)""",parse_mode='HTML',reply_markup = r_bosh1)
			
			### RU-------------Admin
@dp.message_handler(text="Администратор")
async def send_welcome(message: types.Message):
	await message.answer("Выберите пол",reply_markup = r_admin)

@dp.message_handler(text="👨‍🦱 Мужчина")
async def send_welcome(message: types.Message):
	await message.answer("""👤  Введите ФИО (Иванов Иван Иванович)""",reply_markup = r_admin1)

@dp.message_handler(text="👩‍🦰 Женщина")
async def send_welcome(message: types.Message):
	await message.answer("""👤 Введите ФИО (Иванов Иван Иванович) """,reply_markup = r_admin1)

@dp.message_handler(text="Охранник")
async def send_welcome(message: types.Message):
	await message.answer("""Мужчина 20-30.
Знание узбекского и русского языка.
Опыт работы в охранной системе приветствуется.
Образование не ниже средне-специального.
Ответственность, внимательность, вежливость, пунктуальность, опрятный внешний вид.""",reply_markup = xavfsizlik)
	await message.answer("Выберите пол",reply_markup = r_xavfsizlik)

@dp.message_handler(text="👨‍🦱 Мужчина")
async def send_welcome(message: types.Message):
	await message.answer("""👤 Введите ФИО (Иванов Иван Иванович)""",reply_markup = r_xavfsizlik1)

@dp.message_handler(text="👩‍🦰 Женщина")
async def send_welcome(message: types.Message):
	await message.answer("""👤 Введите ФИО (Иванов Иван Иванович)""",reply_markup = r_xavfsizlik1)


			#### Ru---------------Sotuvchi
@dp.message_handler(text="Продавец-консультант")
async def send_welcome(message: types.Message):
	await message.answer("""Требуемый опыт работы: от 1 года


Полная занятость, полный день

Обязанности:

- Вежливое обслуживание посетителей в торговом зале;
- Предоставление консультаций касательно продукции;
- Сопровождение покупателя к кассе;
- Предпродажная подготовка товара;
- Подготовка торгового зала к работе;
- Поддержание порядка и чистоты в магазине;
- Участие в инвентаризации

Требования:
- Грамотная речь;
- Опыт работы значения не имеет, идёт полное обучение в сфере продаж;
- Дисциплинированность, ответственность;
- Владение узбекским и русским языками""",reply_markup = r_sotuvchi)
	await message.answer("Выберите пол",reply_markup = r_sotuvchi)

@dp.message_handler(text="👨‍🦱 Мужчина")
async def send_welcome(message: types.Message):
	await message.answer("""👤 Введите ФИО (Иванов Иван Иванович)""",reply_markup = sotuvchi1)

@dp.message_handler(text="👩‍🦰 Женщина")
async def send_welcome(message: types.Message):
	await message.answer("""👤 Введите ФИО (Иванов Иван Иванович)""",reply_markup = sotuvchi1)


			### Ru------------Kassir
@dp.message_handler(text="Кассир")
async def send_welcome(message: types.Message):
	await message.answer(""" Требуемый опыт работы: 1–3 года

Полная занятость, полный день

Обязанности:
- Вежливое обслуживание покупателей;
- Ведение и учет кассовых документов;
- Обеспечение сохранности денежных средств, находящихся в кассе;
- Работать с наличной и безналичной формой оплаты;
- Сверка количества наличных средств в контрольно-кассовой машине (ККМ);
- Обеспечение кассовой дисциплины.

Требования:

- Опыт работы на аналогичной позиции до 1 года;

- Грамотность, стрессоустойчивость, внимательность, точность;
- Дисциплинированность;
- Владение узбекским и русским языками.
- Умение работать с кассовым аппаратом и терминалом.

Условия:

- График работы: 6/1;
- Обед и ужин за счёт компании;
- Дружный коллектив.""",reply_markup = r_kassir)
	await message.answer("Выберите пол",reply_markup = r_kassir)

@dp.message_handler(text="👨‍🦱 Мужчина")
async def send_welcome(message: types.Message):
	await message.answer("""👤 Введите ФИО (Иванов Иван Иванович)""",reply_markup = r_kassir1)

@dp.message_handler(text="👩‍🦰 Женщина")
async def send_welcome(message: types.Message):
	await message.answer("""👤 Введите ФИО (Иванов Иван Иванович)""",reply_markup = r_kassir1)


				#########Ru---------- Qoriqchiii
@dp.message_handler(text="Охранник, охранница")
async def send_welcome(message: types.Message):
	await message.answer("""ТРЕБОВАНИЯ:
опыт работы не требуется
возраст от 25-35 лет
образование - высшее или среднее-специальное
ответственность.
УСЛОВИЯ:
обед/ужин за счет работодателя;
график работы:6/1 с 10:00 до 16:00; с 16:00 до 00:00;
официальное трудоустройство;""",reply_markup = r_qoriqchi)
	await message.answer("Выберите пол",reply_markup = r_qoriqchi)

@dp.message_handler(text="👨‍🦱 Мужчина")
async def send_welcome(message: types.Message):
	await message.answer("""👤 Введите ФИО (Иванов Иван Иванович)""",reply_markup = r_qoriqchi1)

@dp.message_handler(text="👩‍🦰 Женщина")
async def send_welcome(message: types.Message):
	await message.answer("""👤 Введите ФИО (Иванов Иван Иванович)""",reply_markup = r_qoriqchi1)



#### Ru----------------Tozalovchi
@dp.message_handler(text="Уборщица")
async def send_welcome(message: types.Message):
	await message.answer(""" Обязанности:
- уборка служебных помещений;
Требования:
- чистоплотность;
- аккуратность;
- ответственность;
- вежливость.
Условия работы:
- график работы 6/1 с 10:00 до 18:00
с 14:00 до 22:00
- своевременная выплата з/п от 1 млн;
- комфортабельный офис;
- дружный коллектив;
- обед и ужин за счёт компании,""",reply_markup = r_tozalovchi)
	await message.answer("Выберите пол",reply_markup = r_tozalovchi)

@dp.message_handler(text="👨‍🦱 Мужчина")
async def send_welcome(message: types.Message):
	await message.answer("""👤 Введите ФИО (Иванов Иван Иванович)""",reply_markup = r_tozalovchi1)

@dp.message_handler(text="👩‍🦰 Женщина")
async def send_welcome(message: types.Message):
	await message.answer("""👤 Введите ФИО (Иванов Иван Иванович)""",reply_markup = r_tozalovchi1)


#####----------------------------3
@dp.message_handler(text="💬Отзывы и предложения")
async def send_welcome(message: types.Message):
	await message.answer("""Напишите нам сюда, мы обязательно ответим.""",reply_markup = r_ort)

####-----------------------------4
@dp.message_handler(text="☎️ Контакты/Адрес")
async def send_welcome(message: types.Message):
	await message.answer_photo(
        photo = open('images/gruppa.jpg','rb'),
        caption = """😊 Позвоните нам
 📞+998 94 613 5555

✉️  buttonuz@gmail.com

⏰ Рабочие часы:
Пн-Вс: 10:00 – 22:00 

Наш сайт (https://button.uz/)
""")
	



	##------------1 RU-----------Asosiy ortga
@dp.message_handler(text="⬅️ Назад")
async def send_welcome(message: types.Message):
	await message.answer_photo(
        photo = open('images/key.jpg','rb'),
        caption = """Бот-сайт предназначен для трудоустройства кандидатов в сеть магазинов "BUTTON"
        """,reply_markup=r_keyb)

@dp.message_handler(text="◀️ Назад")
async def send_welcome(message: types.Message):
	await message.answer_photo(
        photo = open('images/key2.jpg','rb'),
        caption = f"""Button магазин мужской и женской одежды!
Компания Button была основана 21 марта 2019 года. В настоящее время существует 3 филиала, которые расположены в городе Ташкенте.

Преимущества:

☑️ Высокое качество;

☑️Широкий ассортимент;

☑️ Доступные цены.""",parse_mode='HTML',reply_markup = r_keyb2)
	

@dp.message_handler(text="◀️ Назад")
async def send_welcome(message: types.Message):
	await message.answer_photo(
	photo = open('images/locat.jpg','rb'),
    caption = f"""Uzbekistan, Tashkent,  Olmazorskiy rayon, maxallya Universitet
+998951443555""")


		###-----------------2
@dp.message_handler(text="⬅️ Назад")
async def send_welcome(message: types.Message):
	await message.answer("""Этот раздел БОТа предназначен для заполнения анкеты ✍️ и трудоустройства  в компанию Button!

Здесь Вы можете заполнить свою анкету 📄 и узнать о существующих вакансиях к нашей Компании!""",reply_markup = r_bosh)
	

@dp.message_handler(text="🔼 Главное Меню")
async def send_welcome(message: types.Message):
	await message.answer_photo(
        photo = open('images/key.jpg','rb'),
        caption = """Бот-сайт предназначен для трудоустройства кандидатов в сеть магазинов "BUTTON"
        """,reply_markup=r_keyb)

@dp.message_handler(text="◀️Назад")
async def send_welcome(message: types.Message):
	await message.answer("""Этот раздел БОТа предназначен для заполнения анкеты ✍️ и трудоустройства  в компанию Button!

Здесь Вы можете заполнить свою анкету 📄 и узнать о существующих вакансиях к нашей Компании!""",reply_markup = r_bosh)


@dp.message_handler(text="⬅️Назад")
async def send_welcome(message: types.Message):
	await message.answer( f"""Адрес: Узбекистан, Ташкент,  Олмазорский район, махалля Университет

Режим работы: 10:00-22:00 (ЕЖЕДНЕВНО)""",parse_mode='HTML',reply_markup = r_bosh1)
			
	
	
@dp.message_handler(text="↩️ Назад")
async def send_welcome(message: types.Message):
	await message.answer("Выберите пол",reply_markup = r_admin)
	


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)