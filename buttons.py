from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton
til = ReplyKeyboardMarkup(
	keyboard = [
		[
	      KeyboardButton(text="🇷🇺 Русский"),
	      KeyboardButton(text="🇺🇿 Узбекский")
	    ],
	    [
	      KeyboardButton(text="⬅️ Ortga")
	    ],
	 ],
	 resize_keyboard = True #адаптивность
)



ort = ReplyKeyboardMarkup(
	keyboard = [
		[
		      KeyboardButton(text="⬅️ Ortga")
	    ],
	 ],
	 resize_keyboard = True #адаптивность
)



keyb = ReplyKeyboardMarkup(
	keyboard = [
	      [
	      KeyboardButton(text="🏢 Kompaniya haqida"),
	      ],
	      [
	      KeyboardButton(text="💼 Bo'sh ish o'rinlari"),
	      ],
	      [
	       KeyboardButton(text="💬 Отзывы и предложения")
	      ],
	      [
	      KeyboardButton(text="☎️Kontaktlar/Manzili"),
	      KeyboardButton(text="🇺🇿/🇷🇺 Язык")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)


keyb2 = ReplyKeyboardMarkup(
	keyboard = [
		[
	      	KeyboardButton(text="📍 Filialimiz")
	    ],
	    [
	      	KeyboardButton(text="⬅️ Ortga")
	    ],
	 ],
	 resize_keyboard = True #адаптивность
)

keyb3 = ReplyKeyboardMarkup(
	keyboard = [
		[
	      KeyboardButton(text="📍 Geolokatsiya",request_location = True)
      	],
      	[
	      KeyboardButton(text="◀️ Ortga")
	    ],
	 ],
	 resize_keyboard = True #адаптивность
)





bosh = ReplyKeyboardMarkup(
	keyboard = [
	      [
	       	  KeyboardButton(text="🏢 Bosh ofis")
	      ],
	      [
		      KeyboardButton(text="🔼 Asosiy Menu"),
		      KeyboardButton(text="⬅️ Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
bosh1 = ReplyKeyboardMarkup(
	keyboard = [
		  [
	       	  KeyboardButton(text="Admistator"),
	       	  KeyboardButton(text="Xavfsizlik xodimi")
	      ],
	      [
	       	  KeyboardButton(text="Sotuvchi-maslahatchi"),
	       	  KeyboardButton(text="Kassir")

	      ],
	       [
	       	  KeyboardButton(text="Qo'riqchi,qo'riqchi qiz"),
	       	  KeyboardButton(text="Tozalovchi")

	      ],
	       
	      [
		      KeyboardButton(text="🔼 Asosiy Menu"),
		      KeyboardButton(text="◀️Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)

admin =  ReplyKeyboardMarkup(
	keyboard = [
	      [
		      KeyboardButton(text="👨‍🦱 Erkak"),
		      KeyboardButton(text="👩‍🦰 Ayol")
	      ],
	      [
	       	  KeyboardButton(text="🔼 Asosiy Menu"),
	       	  KeyboardButton(text="⬅️Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
admin1 =  ReplyKeyboardMarkup(
	keyboard = [
			[
	       	  KeyboardButton(text="🔼 Asosiy Menu"),
	       	  KeyboardButton(text="↩️ Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
# admin2 =  ReplyKeyboardMarkup(
# 	keyboard = [
# 			[
# 	       	  KeyboardButton(text="🔼 Asosiy Menu"),
# 	       	  KeyboardButton(text="Ortga ↩️")
# 	      ],
# 	 ],
# 	 resize_keyboard = True #адаптивность
# )
xavfsizlik =  ReplyKeyboardMarkup(
	keyboard = [
	      [
		      KeyboardButton(text="👨‍🦱 Erkak"),
		      KeyboardButton(text="👩‍🦰 Ayol")
	      ],
	      [
	       	  KeyboardButton(text="🔼 Asosiy Menu"),
	       	  KeyboardButton(text="⬅️Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
xavfsizlik1 =  ReplyKeyboardMarkup(
	keyboard = [
			[
	       	  KeyboardButton(text="🔼 Asosiy Menu"),
	       	  KeyboardButton(text="⬅️Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
sotuvchi =  ReplyKeyboardMarkup(
	keyboard = [
	      [
		      KeyboardButton(text="👨‍🦱 Erkak"),
		      KeyboardButton(text="👩‍🦰 Ayol")
	      ],
	      [
	       	  KeyboardButton(text="🔼 Asosiy Menu"),
	       	  KeyboardButton(text="⬅️Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
sotuvchi1 =  ReplyKeyboardMarkup(
	keyboard = [
			[
	       	  KeyboardButton(text="🔼 Asosiy Menu"),
	       	  KeyboardButton(text="⬅️Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
kassir =  ReplyKeyboardMarkup(
	keyboard = [
	      [
		      KeyboardButton(text="👨‍🦱 Erkak"),
		      KeyboardButton(text="👩‍🦰 Ayol")
	      ],
	      [
	       	  KeyboardButton(text="🔼 Asosiy Menu"),
	       	  KeyboardButton(text="⬅️Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
kassir1 =  ReplyKeyboardMarkup(
	keyboard = [
			[
	       	  KeyboardButton(text="🔼 Asosiy Menu"),
	       	  KeyboardButton(text="⬅️Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
qoriqchi =  ReplyKeyboardMarkup(
	keyboard = [
	      [
		      KeyboardButton(text="👨‍🦱 Erkak"),
		      KeyboardButton(text="👩‍🦰 Ayol")
	      ],
	      [
	       	  KeyboardButton(text="🔼 Asosiy Menu"),
	       	  KeyboardButton(text="⬅️Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
qoriqchi1 =  ReplyKeyboardMarkup(
	keyboard = [
			[
	       	  KeyboardButton(text="🔼 Asosiy Menu"),
	       	  KeyboardButton(text="⬅️Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
tozalovchi =  ReplyKeyboardMarkup(
	keyboard = [
	      [
		      KeyboardButton(text="👨‍🦱 Erkak"),
		      KeyboardButton(text="👩‍🦰 Ayol")
	      ],
	      [
	       	  KeyboardButton(text="🔼 Asosiy Menu"),
	       	  KeyboardButton(text="⬅️Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
tozalovchi1 =  ReplyKeyboardMarkup(
	keyboard = [
			[
	       	  KeyboardButton(text="🔼 Asosiy Menu"),
	       	  KeyboardButton(text="↩️ Ortga")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)

###  Telefonni yuborish
# tel = ReplyKeyboardMarkup(
# 	keyboard = [
# 		  [
# 	      	KeyboardButton(text="Telefon raqamni yuborish",request_contact = True)
# 	      ],
# 	 ],
# 	 resize_keyboard = True #адаптивность
# )


r_keyb = ReplyKeyboardMarkup(
	keyboard = [
	      [
	      KeyboardButton(text="🏢 О компании"),
	      ],
	      [
	      KeyboardButton(text="💼  Вакансии"),
	      ],
	      [
	       KeyboardButton(text="💬Отзывы и предложения")
	      ],
	      [
	      KeyboardButton(text="☎️ Контакты/Адрес"),
	      KeyboardButton(text="🇺🇿/🇷🇺 Язык")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)

r_keyb2 = ReplyKeyboardMarkup(
	keyboard = [
		[
	      	KeyboardButton(text="📍 Наш филиал")
	    ],
	    [
	      	KeyboardButton(text="⬅️ Назад")
	    ],
	 ],
	 resize_keyboard = True #адаптивность
)
r_keyb3 = ReplyKeyboardMarkup(
	keyboard = [
		[
	      KeyboardButton(text="📍 Отправить геолокацию",request_location = True)
      	],
      	[
	      KeyboardButton(text="◀️ Назад")
	    ],
	 ],
	 resize_keyboard = True #адаптивность
)


r_bosh = ReplyKeyboardMarkup(
	keyboard = [
	      [
	       	  KeyboardButton(text="🏢 Головной Офис")
	      ],
	      [
		      KeyboardButton(text="🔼 Главное Меню"),
		      KeyboardButton(text="⬅️ Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
r_bosh1 = ReplyKeyboardMarkup(
	keyboard = [
		  [
	       	  KeyboardButton(text="Администратор"),
	       	  KeyboardButton(text="Охранник")
	      ],
	      [
	       	  KeyboardButton(text="Продавец-консультант"),
	       	  KeyboardButton(text="Кассир")

	      ],
	       [
	       	  KeyboardButton(text="Охранник, охранница"),
	       	  KeyboardButton(text="Уборщица")

	      ],
	       
	      [
		      KeyboardButton(text="🔼 Главное Меню"),
		      KeyboardButton(text="◀️Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)

r_admin =  ReplyKeyboardMarkup(
	keyboard = [
	      [
		      KeyboardButton(text="👨‍🦱 Мужчина"),
		      KeyboardButton(text="👩‍🦰 Женщина")
	      ],
	      [
	       	  KeyboardButton(text="🔼 Главное Меню"),
	       	  KeyboardButton(text="⬅️Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
r_admin1 =  ReplyKeyboardMarkup(
	keyboard = [
			[
	       	  KeyboardButton(text="🔼 Главное Меню"),
	       	  KeyboardButton(text="↩️ Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)

r_xavfsizlik =  ReplyKeyboardMarkup(
	keyboard = [
	      [
		      KeyboardButton(text="👨‍🦱 Мужчина"),
		      KeyboardButton(text="👩‍🦰 Женщина")
	      ],
	      [
	       	  KeyboardButton(text="🔼 Главное Меню"),
	       	  KeyboardButton(text="⬅️Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
r_xavfsizlik1 =  ReplyKeyboardMarkup(
	keyboard = [
			[
	       	  KeyboardButton(text="🔼 Главное Меню"),
	       	  KeyboardButton(text="⬅️Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)

r_sotuvchi =  ReplyKeyboardMarkup(
	keyboard = [
	      [
		      KeyboardButton(text="👨‍🦱 Мужчина"),
		      KeyboardButton(text="👩‍🦰 Женщина")
	      ],
	      [
	       	  KeyboardButton(text="🔼 Главное Меню"),
	       	  KeyboardButton(text="⬅️Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
r_sotuvchi1 =  ReplyKeyboardMarkup(
	keyboard = [
			[
	       	  KeyboardButton(text="🔼 Главное Меню"),
	       	  KeyboardButton(text="⬅️Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
r_kassir =  ReplyKeyboardMarkup(
	keyboard = [
	      [
		      KeyboardButton(text="👨‍🦱 Мужчина"),
		      KeyboardButton(text="👩‍🦰 Женщина")
	      ],
	      [
	       	  KeyboardButton(text="🔼 Главное Меню"),
	       	  KeyboardButton(text="⬅️Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
r_kassir1 =  ReplyKeyboardMarkup(
	keyboard = [
			[
	       	  KeyboardButton(text="🔼 Главное Меню"),
	       	  KeyboardButton(text="⬅️Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
r_qoriqchi =  ReplyKeyboardMarkup(
	keyboard = [
	      [
		      KeyboardButton(text="👨‍🦱 Мужчина"),
		      KeyboardButton(text="👩‍🦰 Женщина")
	      ],
	      [
	       	  KeyboardButton(text="🔼 Главное Меню"),
	       	  KeyboardButton(text="⬅️Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
r_qoriqchi1 =  ReplyKeyboardMarkup(
	keyboard = [
			[
	       	  KeyboardButton(text="🔼 Главное Меню"),
	       	  KeyboardButton(text="⬅️Назадa")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
r_tozalovchi =  ReplyKeyboardMarkup(
	keyboard = [
	      [
		      KeyboardButton(text="👨‍🦱 Мужчина"),
		      KeyboardButton(text="👩‍🦰 Женщина")
	      ],
	      [
	       	  KeyboardButton(text="🔼 Главное Меню"),
	       	  KeyboardButton(text="⬅️Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)
r_tozalovchi1 =  ReplyKeyboardMarkup(
	keyboard = [
			[
	       	  KeyboardButton(text="🔼 Главное Меню"),
	       	  KeyboardButton(text="↩️ Назад")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)

r_ort = ReplyKeyboardMarkup(
	keyboard = [
		[
		      KeyboardButton(text="⬅️ Назад")
	    ],
	 ],
	 resize_keyboard = True #адаптивность
)