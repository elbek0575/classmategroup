import os
import sys
import telebot
import time
import logging
import random
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)

# Загрузка переменных окружения
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

group_id = [-1001946744681, -1001757231258]  # ID группы

# Словарь для перевода месяцев
months_rus = {
    "January": "январь", "February": "февраль", "March": "март", "April": "апрель",
    "May": "май", "June": "июнь", "July": "июль", "August": "август",
    "September": "сентябрь", "October": "октябрь", "November": "ноябрь", "December": "декабрь"
}

# Получаем текущую дату
today = datetime.now().strftime("%d %B")  # Форматируем дату с английским названием месяца
# Переводим название месяца на русский, используя словарь month_translation
day, month_english = today.split()
month_russian = months_rus.get(month_english, month_english)
today_translated = f"{day} {month_russian}"  # Дата с русским названием месяца

logger.info(f"Проверка дней рождения на {today_translated}")


# Список с днями рождения
birthdays = [
    {"id": 1, "name": "Исроилжон", "date": "14 январь"},
    {"id": 2, "name": "Жамшид", "date": "19 январь"},
    {"id": 3, "name": "Хусниддин", "date": "28 январь"},
    {"id": 4, "name": "Санжар", "date": "08 февраль"},
    {"id": 5, "name": "Бобир", "date": "28 февраль"},
    {"id": 6, "name": "Мунаввар", "date": "15 март"},
    {"id": 7, "name": "Фаррухжон", "date": "06 март"},
    {"id": 8, "name": "Малика", "date": "24 март"},
    {"id": 9, "name": "Мохигул", "date": "25 март"},
    {"id": 10, "name": "Навбахор", "date": "29 март"},
    {"id": 11, "name": "Жасурбой", "date": "31 март"},
    {"id": 12, "name": "Гулибахор", "date": "19 май"},
    {"id": 13, "name": "Машхурахон", "date": "29 апрель"},
    {"id": 14, "name": "Лобарой", "date": "30 апрель"},
    {"id": 15, "name": "Гулнорахон", "date": "16 ноябрь"},
    {"id": 16, "name": "Мохичехра", "date": "23 июль"},
    {"id": 17, "name": "Дилшоджон", "date": "10 август"},
    {"id": 18, "name": "Сирожбой", "date": "19 август"},
    {"id": 19, "name": "Элбек", "date": "22 август"},
    {"id": 20, "name": "Наргиза", "date": "22 август"},
    {"id": 21, "name": "Отабек", "date": "30 август"},
    {"id": 22, "name": "Лобархон", "date": "31 август"},
    {"id": 23, "name": "Муроджон", "date": "30 август"},
    {"id": 24, "name": "Отабек", "date": "16 октябрь"},
    {"id": 25, "name": "Мунера", "date": "19 октябрь"},
    {"id": 26, "name": "Дилбархон", "date": "01 ноябрь"},
    {"id": 27, "name": "Нафисахон", "date": "12 ноябрь"},
    {"id": 28, "name": "Холидахон", "date": "05 декабрь"},
    {"id": 29, "name": "Элёржон", "date": "06 декабрь"},
    {"id": 30, "name": "Шахло", "date": "21 декабрь"},
    {"id": 31, "name": "Ферузахон", "date": "27 декабрь"}
]




congratulations_1 = f"Азиз синфдошим {{name}}!\nТаваллуд кунинг муборак бўлсин! Ёшингда янги марралар, янги ютуқлар сенга ёр бўлсин! Ҳар кунинг қувонч ва бахтга тўлсин! 😊🎉"
congratulations_2 = f"Қадрли {{name}}, бугунги таваллуд кунингда барча орзуларингга етишингни тилайман. Янги йилда янги имкониятлар ва муваффақиятлар сенга насиб этсин! 💫🌈"
congratulations_3 = f"Азиз {{name}}! Қалбингдаги орзуларингга етиб, барча режаларинг амалга ошсин! Таваллуд кунинг муборак бўлсин! 💖🎂"
congratulations_4 = f"{{name}}, сени таваллуд кунинг билан табриклайман! Ёшингда муваффақият, бахт ва соғлиқ доимий ҳамроҳинг бўлсин. Ҳар кунинг ёруғ ва бахтли бўлсин! ☀️🎈"
congratulations_5 = f"Азиз {{name}}, сенга бахт ва муваффақият ёр бўлсин! Янги ёшингда янги марраларни эгаллашда давом эт! Таваллуд кунинг муборак! 🎉🌸"
congratulations_6 = f"{{name}}, бугун сен учун энг ёрқин кун! Таваллуд кунинг муборак бўлсин! Янги йилда янги ютуқлар ва ғалабалар сенга насиб этсин! 🎂💪"
congratulations_7 = f"Қадрли синфдошим {{name}}, таваллуд кунинг муборак! Ҳар бир кунинг қувонч, бахт ва соғлиқ билан тўлсин. Сен билан бирга бахтли онларни ўтказиш — биз учун бахт! 💐😊"
congratulations_8 = f"{{name}}, таваллуд кунинг билан! Сенга ҳар қадамингда бахт ва муваффақият ёр бўлсин! Янги ёшингда ҳамма орзуларинг амалга ошсин! 🌟🎂"
congratulations_9 = f"Азиз синфдошим {{name}}! Бугунги кунда сенга энг эзгу тилакларни тилайман. Ҳар бир орзу ва мақсадларинг амалга ошсин! 🎉❤️"
congratulations_10 = f"Синфдощим {{name}}, таваллуд кунинг муборак! Соғлиқ, бахт ва ғалабалар сенга ёр бўлсин! Бизни ҳар доим илҳомлантириб тур! 🌺🌞"
congratulations_11 = f"{{name}}, таваллуд кунинг билан табриклайман! Янги ёшингда барча тўсиқларни енгиб, муваффақиятлар сари қадам ташла! Ҳар бир орзуинг рўёбга чиқсин! 🌟💪"
congratulations_12 = f"Қимматли синфдош {{name}}, бугунги кун сен учун янги бошланғич бўлсин. Ҳар бир кунингда янги имкониятлар ва қувончлар ёр бўлсин! Таваллуд кунинг муборак! 🎉🌈"
congratulations_13 = f"Сендай синфдош дўстга эга бўлиш биз учун бахт! {{name}}, таваллуд кунинг муборак бўлсин! Куч-қувват ва илҳом билан тўлиб, орзу қилаётган барча нарсаларингга етиш! 💫🎂"
congratulations_14 = f"{{name}}, ёшингда ғалабалар ва қувончлар кўп бўлсин! Ҳар бир янги кун сен учун илҳом манбаи бўлсин! Янги ёшингда барча режаларинг амалга ошсин! 🌞❤️"
congratulations_15 = f"Азиз синфдошим, дўстим {{name}}, янги йилингда янги ғоялар ва имкониятлар яратишда давом эт! Ҳар қадамиингга омад ва муваффақият ёр бўлсин! 🎂🌹"
congratulations_16 = f"Таваллуд кунинг билан, {{name}}! Орзуингга қўйган қадамларинг турли тўсиқлардан чўчимасин. Сенга янги йилда янада юксак марралар тилайман! 💖💫"
congratulations_17 = f"Қадрли синфдошим, дўстим {{name}}, бу йил сен учун энг ютуқли йил бўлсин! Бошланган йўлингда тўхтамай давом эт, барча орзуларинг амалга ошсин! 🌠🎉"
congratulations_18 = f"{{name}}, бугун сен учун бахтли кун! Янги ёшингда янги ғалабаларга эриш, янги марраларни эгалла. Таваллуд кунинг муборак! 🎈🌟"
congratulations_19 = f"Азиз дўстим, синфдошим {{name}}, орзу-қувончлар билан тўлиб-тошган йил бўлсин! Таваллуд кунинг қутлуғ бўлсин, ҳар кунингда янги имкониятлар ёр бўлсин! 🌻🌈"
congratulations_20 = f"{{name}}, ҳаётингдаги ҳар бир кунда илҳом ва ғалабалар ёр бўлсин! Таваллуд кунинг билан! Сен билан бизга куч ва қувонч бағишлайсан! 🎉❤️"
congratulations_21 = f"{{name}}, сен учун бугунги кун бахт ва қувончлар билан тўла бўлсин! Ҳаётингдаги ҳар бир қадамда омад ва бахт ёр бўлсин. Таваллуд кунинг муборак! 🎈🌺"
congratulations_22 = f"Ҳурматли {{name}}, янги йилингда янги юқориликларга эриш! Сенга бахт, соғлик ва барча орзу-мақсадларинг рўёбга чиқишини тилайман. 🎉🌞"
congratulations_23 = f"{{name}}, сен каби ғамхўр ва теран инсонга бахт ва илҳом тилайман! Таваллуд кунинг қутлуғ бўлсин! Ҳар кунингда муваффақият сени кутаётган бўлсин! 🌟🌷"
congratulations_24 = f"Қадрли дўстим, синфдошим {{name}}, ҳаётингда ҳар қадамда янги ғалабалар ва ютуқлар сени кутсин! Янги йилингда севинч ва бахтдан чарчамагин! Таваллуд кунинг муборак! 🌼💫"
congratulations_25 = f"Бугун сенинг кунинг, {{name}}! Янги йилингда ҳар қадамингда қувонч ва илҳом сени қарши олсин. Барча орзу-истакларинг амалга ошсин! 🎂🌞"
congratulations_26 = f"{{name}}, таваллуд кунинг билан табриклайман! Бу йил сен учун энг бахтли йил бўлсин, ҳар кундан янги завқ ва илҳом ол! 🎉🌈"
congratulations_27 = f"Қимматли дўстим, синфдошим {{name}}, янги йилингда ҳар кун қувонч ва ғалабаларга бой бўлсин! Барча орзуларинг тўлиқ амалга ошсин! Таваллуд кунинг муборак! 🌻❤️"
congratulations_28 = f"{{name}}, сен каби инсонинг таваллуд кунида орзу-истакларингга эришишингни тилайман! Ҳар қадамиингга омад ва муваффақият ёр бўлсин! 🌸🎂"
congratulations_29 = f"{{name}}, янги йилингда янги ғалабаларга эриш, орзу қилган марраларингга яқинлаш! Таваллуд кунинг қутлуғ бўлсин, ҳаётингда бахт бор бўлсин! 🎈🌼"
congratulations_30 = f"Қимматли дўстим, синфдошим {{name}}, янги йилингда янги юқориликларга етиш! Сенга соғлик, бахт ва доимий қувонч тилайман. Таваллуд кунинг билан! 🌟🌷"
congratulations_31 = f"{{name}}, ҳар бир кунинг бахт ва қувончга тўла бўлсин! Янги йилингда янги имкониятлар сени кутсин. Таваллуд кунинг муборак! 🎉🌹"
congratulations_32 = f"Қадрли дўстим, синфдошим {{name}}, сенга меҳр ва муҳаббат билан тўла ҳаёт тилайман. Ҳар бир орзуинг амалга ошсин! Таваллуд кунинг билан! 🎈💖"
congratulations_33 = f"{{name}}, сенинг ғоя ва мақсадларинг ёрқин бўлсин, ҳаётингда ҳар доим йўлдошингга айлансин! Таваллуд кунинг муборак! 🌞✨"
congratulations_34 = f"Бугунги кун сен учун янги орзулар ва ғалабалар эшигини очсин! Таваллуд кунинг қутлуғ бўлсин, {{name}}! 🌸🎂"
congratulations_35 = f"{{name}}, сенга бахтли ва файзли ҳаёт тилайман! Ҳар кунинг шукуҳ билан ўтсин, ҳар қадамингда қувонч бўлсин! 🌼💫"
congratulations_36 = f"Қимматли дўстим, синфдошим {{name}}, ҳаётингдаги ҳар кун янги имкониятлар ва илҳомларга тўла бўлсин! Таваллуд кунинг муборак! 🎉🌻"
congratulations_37 = f"Янги йилингда сенга янги қувончлар ва байрамлар тилайман! Ҳар бир кунингга завқ ва бахт ёр бўлсин, {{name}}! 🌺🎈"
congratulations_38 = f"{{name}}, сен каби қўрқинмас инсонга янги марралар ва муваффақиятлар тилайман! Орзу-мақсадларинг амалга ошсин! 🎂✨"
congratulations_39 = f"Таваллуд кунинг муборак бўлсин, {{name}}! Янги йилингда сени ғалабалар ва қувончлар кутаётган бўлсин! 🎉🌷"
congratulations_40 = f"{{name}}, сенга файзли ҳаёт ва доимий муваффақиятлар тилайман! Таваллуд кунинг муборак, ҳар бир кунинг омадли ўтсин! 🎈🌞"
congratulations_41 = f"{{name}}, ҳар кунингда қувонч ва завқ бўлсин! Сенга янги йилда бахт, соғлик ва кўплаб ғалабалар тилайман! 🎉💖"
congratulations_42 = f"Қадрли дўстим, синфдошим {{name}}, сенга ҳар доим орзуларингга эришиш тилайман! Ҳаётингда қувонч ва омад ёр бўлсин! Таваллуд кунинг билан! 🌹🌸"
congratulations_43 = f"Сенга бахт, омад ва муҳаббат тилайман, {{name}}! Янги йилингда ҳар қадамиингда илҳом бор бўлсин! 🎈🎂"
congratulations_44 = f"{{name}}, таваллуд кунинг билан! Ҳаётингда севинч ва қувонч бор бўлсин, ҳар бир орзуинг амалга ошсин! 🌺💫"
congratulations_45 = f"Таваллуд кунинг муборак, {{name}}! Янги йилингда янги ғоялар, янги марралар ва доимий қувонч сени кутаётган бўлсин! 🎉🌞"
congratulations_46 = f"{{name}}, сенинг ҳар бир кунингга фақат яхши ҳислар ёр бўлсин, дўстинг ва қадринг янада артишини тилайман! Таваллуд кунинг муборак! 🌺🌟"
congratulations_47 = f"Дўстим синфдошим {{name}}, сенга енгиллик ва муваффақиятлар тилайман! Ҳар бир орзуингга эришишга насиб қилсин! 🎂✨"
congratulations_48 = f"{{name}}, сен каби ёрқин инсонга ҳаётингда фақат қувонч ва бахт керак! Таваллуд кунинг муборак, ажойиб одам! 🎈💐"
congratulations_49 = f"Ҳар бир кунинг завқ билан бошлансин, ҳар қадамиинг қувончга тўлсин, {{name}}! Таваллуд кунинг муборак! 🎉🌷"
congratulations_50 = f"{{name}}, янги йилингда янги ғалабалар ва юксак марралар сени кутсин! Ҳар бир кунинг қувончли ва бахтли ўтсин! 🌺💫"
congratulations_51 = f"Янги йилингда сени фақат илиқ ҳислар, ёрқин марралар ва бахт кутсин, {{name}}! Таваллуд кунинг билан! 🎈🌞"
congratulations_52 = f"{{name}}, сен каби инсонлар орзу ва ғояларга бой бўлишга ярайди! Ҳар бир орзуинг амалга ошсин! 🎂💖"
congratulations_53 = f"Таваллуд кунинг муборак бўлсин, {{name}}! Янги йилингда орзу ва қувончлар тўла бўлсин! 🌸🌟"
congratulations_54 = f"{{name}}, сенга юксак марралар ва ишонч билан тўлдирилган йил тилайман! Таваллуд кунинг муборак! 🎉💫"
congratulations_55 = f"Янги йилинг қувончли, омадли ва муҳаббатли бўлсин, {{name}}! Таваллуд кунинг муборак! 🌼🎈"
congratulations_56 = f"{{name}}, сенга барча орзуингни амалга оширишни тилайман! Ҳар кунинг фақат яхши ҳислар ёр бўлсин! 🎉💖"
congratulations_57 = f"Сен каби дўстим борлиги учун бахтлиман, {{name}}. Сенга фақат ёрқин ва бахтли кунлар тилайман! 🌹🌸"
congratulations_58 = f"{{name}}, таваллуд кунинг муборак! Ҳар бир кунинг ўзига хос ва завқли бўлсин! 🎈💫"
congratulations_59 = f"Таваллуд кунинг муборак, {{name}}! Янги йилинг сени бахтга тўлдирсин! 🎂🌟"
congratulations_60 = f"Ҳар бир кунинг завқ ва умид билан тўлсин, {{name}}. Ҳар қадамиинг қувончли бўлсин! 🎉💐"
congratulations_61 = f"Дўстим, синфдошим {{name}}, сенга янги қувончли ва бахтли йил тилайман. Таваллуд кунинг муборак! 🌺✨"
congratulations_62 = f"{{name}}, сенинг янги йилингда фақат яхши ҳислар ва юксак марралар бўлсин! 🎂🌹"
congratulations_63 = f"Янги йилингда фақат қувонч, бахт ва муҳаббат ёр бўлсин, {{name}}! Таваллуд кунинг муборак! 🌞💫"
congratulations_64 = f"Ҳар бир кунинг қувончли ва тўла муваффақиятли бўлсин, {{name}}. Таваллуд кунинг муборак! 🎉🌸"
congratulations_65 = f"{{name}}, сен каби инсонинг янги йилида фақат яхшиликлар ва шодликлар бўлсин! Таваллуд кунинг муборак! 🎂💐"
congratulations_66 = f"{{name}}, сенга янги йилингда ҳар бир қадамингда фақат яхши ҳислар ҳамроҳ бўлсин! Таваллуд кунинг муборак! 🌟🎉"
congratulations_67 = f"Ҳар бир орзуингга эришишингга тилайман, {{name}}. Сенинг янги йилингда фақат яхши кунлар бўлсин! 🎈💐"
congratulations_68 = f"{{name}}, сен каби дўстим борлиги учун бахтлиман. Ҳар кунинг завқ ва қувонч билан тўлсин! 🌹🌺"
congratulations_69 = f"Таваллуд кунинг муборак, {{name}}! Сенга янги ғалабалар ва катта муваффақиятлар тилайман! 🎉✨"
congratulations_70 = f"Ҳар бир кунинг сен учун қувончли ва бахтли бўлсин, {{name}}! Таваллуд кунинг муборак! 🌸💫"
congratulations_71 = f"{{name}}, янги йилингда сенга орзу ва мақсадларга бой кунлар тилайман! Таваллуд кунинг муборак! 🎂🌟"
congratulations_72 = f"Сен каби ажойиб инсонга ҳаётингда фақат ёрқин кунлар бўлсин, {{name}}! 🎈🌷"
congratulations_73 = f"Ҳар қадамингда омад ва қувонч сени ёр бўлсин, {{name}}. Таваллуд кунинг муборак! 🌺🎉"
congratulations_74 = f"{{name}}, сенга янги йилингда фақат яхши кунлар, бахт ва омад тилайман! 🎂💖"
congratulations_75 = f"Сенинг янги йилингда қувонч, муҳаббат ва бахт кўп бўлсин, {{name}}! Таваллуд кунинг билан! 🎈🌞"
congratulations_76 = f"Таваллуд кунинг муборак, {{name}}! Ҳар бир кунинг сенга янги имкониятлар олиб келсин! 🌸💫"
congratulations_77 = f"{{name}}, сенга фақат яхши кунлар, юксак марралар ва бахт тилайман! Таваллуд кунинг муборак! 🎉✨"
congratulations_78 = f"Сен каби инсонга ҳар бир куни бахт ва қувонч олиб келсин, {{name}}. 🌺💐"
congratulations_79 = f"Ҳар бир кунинг сен учун завқли ва бахтли бўлсин, {{name}}! Таваллуд кунинг муборак! 🎂🌷"
congratulations_80 = f"Сенга янги йилингда фақат илиқ ҳислар ва омад тилайман, {{name}}! 🎈🌞"
congratulations_81 = f"{{name}}, янги йилингда ҳар кунинг фақат бахт ва яхши кунлар билан тўлсин! 🎉🌸"
congratulations_82 = f"Ҳар бир орзуинг амалга ошишига тилайман, {{name}}. Таваллуд кунинг муборак! 🎂💐"
congratulations_83 = f"{{name}}, янги йилингда фақат ёрқин ва бахтли кунлар бўлсин! 🎉💖"
congratulations_84 = f"Сен каби инсон ҳар бир кунидан фақат яхши ҳислар олсин, {{name}}. 🌺🌷"
congratulations_85 = f"Ҳар бир кунинг сенга қувонч, бахт ва омад олиб келсин, {{name}}! 🎈✨"
congratulations_86 = f"{{name}}, янги йилингда сенга фақат яхшиликлар, орзу ва қувончлар тилайман! 🌸💫"
congratulations_87 = f"Сен каби дўстим борлиги учун бахтлиман, {{name}}. Таваллуд кунинг муборак! 🎂🌷"
congratulations_88 = f"{{name}}, янги йилингда фақат яхши кунлар ва бахт ёр бўлсин! Таваллуд кунинг билан! 🌞💫"
congratulations_89 = f"Ҳар бир кунинг сенга бахт ва омад олиб келсин, {{name}}. Таваллуд кунинг муборак! 🎉💖"
congratulations_90 = f"{{name}}, янги йилингда ҳар кунинг ёрқин ва хотиржамлик билан тўлсин! 🎈🌹"
congratulations_91 = f"Сен каби инсонга бахт ва қувонч ёр бўлсин, {{name}}. Таваллуд кунинг муборак! 🌸✨"
congratulations_92 = f"{{name}}, сенинг янги йилингда фақат яхши кунлар ва яхши ҳислар бўлсин! 🎉🌺"
congratulations_93 = f"Таваллуд кунинг муборак, {{name}}! Сенга юксак марралар ва муваффақиятлар тилайман! 🎂💫"
congratulations_94 = f"{{name}}, сенинг янги йилинг қувонч ва орзулар билан тўлсин! Таваллуд кунинг муборак! 🌞🌹"
congratulations_95 = f"{{name}}, янги йилингда сенга фақат ёрқин кунлар ва яхши ҳислар тилайман! 🎂🌺"
congratulations_96 = f"Сен каби дўстим борлигига бахтлиман, {{name}}. Янги йилинг қувонч ва муҳаббатга тўлсин! 🌹✨"
congratulations_97 = f"{{name}}, сенинг янги йилингда фақат ёрқин ва бахтли кунлар бўлсин! Таваллуд кунинг билан! 🎈💐"
congratulations_98 = f"Ҳар кунинг сени қувончга тўлдирсин, {{name}}. Таваллуд кунинг муборак! 🌸💖"
congratulations_99 = f"{{name}}, сенинг янги йилингда фақат ёрқин ҳислар бўлсин! Ҳар бир кунинг қувончли ўтсин! 🌺🌷"
congratulations_100 = f"Сен каби инсонга фақат бахт ва қувонч тилайман, {{name}}. Таваллуд кунинг муборак! 🎂💫"



congratulations_list = [
    congratulations_1, congratulations_2, congratulations_3, congratulations_4,
    congratulations_5, congratulations_6, congratulations_7, congratulations_8,
    congratulations_9, congratulations_10, congratulations_11, congratulations_12,
    congratulations_13, congratulations_14,congratulations_15, congratulations_16,
    congratulations_17, congratulations_18,congratulations_19, congratulations_20,
    congratulations_21, congratulations_22, congratulations_23, congratulations_24,
    congratulations_25, congratulations_26, congratulations_27, congratulations_28,
    congratulations_29, congratulations_30, congratulations_31, congratulations_32,
    congratulations_33, congratulations_34, congratulations_35, congratulations_36,
    congratulations_37, congratulations_38, congratulations_39, congratulations_40,
    congratulations_41, congratulations_42, congratulations_43, congratulations_44,
    congratulations_45, congratulations_46, congratulations_47, congratulations_48,
    congratulations_49, congratulations_50, congratulations_51, congratulations_52,
    congratulations_53, congratulations_54, congratulations_55, congratulations_56,
    congratulations_57, congratulations_58, congratulations_59, congratulations_60,
    congratulations_61, congratulations_62, congratulations_63, congratulations_64,
    congratulations_65, congratulations_66, congratulations_67, congratulations_68,
    congratulations_69, congratulations_70, congratulations_71, congratulations_72,
    congratulations_73, congratulations_74, congratulations_75, congratulations_76,
    congratulations_77, congratulations_78, congratulations_79, congratulations_80,
    congratulations_81, congratulations_82, congratulations_83, congratulations_84,
    congratulations_85, congratulations_86, congratulations_87, congratulations_88,
    congratulations_89, congratulations_90, congratulations_91, congratulations_92,
    congratulations_93, congratulations_94, congratulations_95, congratulations_96,
    congratulations_97, congratulations_98, congratulations_99, congratulations_100
]

# Словарь для перевода месяцев
months_rus = {
    "January": "январь", "February": "февраль", "March": "март", "April": "апрель",
    "May": "май", "June": "июнь", "July": "июль", "August": "август",
    "September": "сентябрь", "October": "октябрь", "November": "ноябрь", "December": "декабрь"
}

# Список для отслеживания уже отправленных сообщений в течение дня
sent_messages = []


# Функция для отправки поздравления
def send_congratulation_message(name):
    message = random.choice(congratulations_list).format(name=name)
    for chat_id in group_id:
        try:
            bot.send_message(chat_id=chat_id, text=message)
            logger.info(f"Отправлено поздравление {name} в группу {chat_id}: {message}")
        except telebot.apihelper.ApiTelegramException as e:
            logger.error(f"Ошибка при отправке в группу {chat_id}: {e}")

# Функция для проверки, у кого сегодня день рождения
def get_today_birthdays():
    today = datetime.now().strftime("%d %B").split()
    month_russian = months_rus.get(today[1], today[1])
    today_translated = f"{today[0]} {month_russian}".lower()
    today_birthdays = [person for person in birthdays if person["date"].lower() == today_translated]
    return today_birthdays

# Функция для отправки поздравлений каждый час, если сегодня день рождения
def send_hourly_congratulations():
    today_birthdays = get_today_birthdays()
    if not today_birthdays:
        logger.info("Сегодня нет именинников.")
        return

    # Поздравляем каждого именинника каждый час
    logger.info(f"Сегодня день рождения у {', '.join(person['name'] for person in today_birthdays)}.")
    for _ in range(24):  # Запускаем цикл на 24 часа
        for person in today_birthdays:
            send_congratulation_message(person["name"])
        time.sleep(5400)  # Ждём один час 30 минут

# Функция check_birthdays, которая запускает проверку и отправку поздравлений
def check_birthdays():
    today_birthdays = get_today_birthdays()
    if today_birthdays:
        logger.info("Сегодня день рождения у:")
        for person in today_birthdays:
            logger.info(f"- {person['name']}")
        send_hourly_congratulations()
    else:
        logger.info("Сегодня нет именинников.")

# Основная функция
def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_birthdays":
            check_birthdays()
        else:
            logging.warning(f"Неизвестный аргумент: {sys.argv[1]}")
    else:
        logger.info("Бот запущен и готов к проверке дней рождения.")
        check_birthdays()



if __name__ == "__main__":
    main()