from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline import first,p_n,e_n,an1,an2,an3,dynamik_kb,dynamik_kb2_3
from loader import dp
from keyboards.default import pitanna,mobila,dvi_cnopke
from .parsing import articles,articles2,new_links,new_links2,list_h,list_h2
import random
from states import test,test2_3
@dp.message_handler(commands=["info"])
async def info (message:types.Message):
    await message.answer("що ви хочете дізнатись")

@ dp.message_handler(content_types=types.ContentTypes.STICKER)
async def sticy(message:types.Message):
    await message.answer_sticker(f"{message.sticker.file_id}")
    
@dp.message_handler(commands=["posluga"])
async def info (message:types.Message):
    await message.answer("що вам потрібно зробити")

@dp.message_handler(commands="button")
async def baton(message:types.Message):
    await message.answer("я кнопка натисни мене",reply_markup=first)
@dp.callback_query_handler(text="button1")
async def button(call:types.CallbackQuery):
    await call.message.answer("що хотів!Я казав не нажимай!!!")


@dp.message_handler(commands="button2")
async def baton(message:types.Message):
    await message.answer("не натискай",reply_markup=first)
@dp.callback_query_handler(text="button2")
async def button(call:types.CallbackQuery):
    await call.message.answer("ви кмітливі все робите навпаки")


# @dp.message_handler(commands=["test"])
# async def info (message:types.Message):
#     await message.answer("скільки крил в boing 747?",reply_markup=pitanna)

# @dp.message_handler()
# async def info (message:types.Message):
#     if message.text=="4 крила":
#         await message.answer("піде")


@dp.message_handler(commands="mobila")
async def bot_echo(message:types.Message):
    await message.answer("у вас є 10 секунд відправити номер мобіли!",reply_markup=mobila)


@dp.message_handler(commands="whattoread")
async def bot_echo(message:types.Message):
    await message.answer("які новини орендуєте",reply_markup=dvi_cnopke)

@dp.message_handler(text="політичні новини")
async def bot_echo(message:types.Message):
    await message.answer(f"натисніть для отримання новини\n"
                         f"1.{list_h[0]}\n"
                         f"2.{list_h[1]}\n"
                         f"3.{list_h[2]}\n"
                         f"4.{list_h[3]}\n",reply_markup=p_n
                        
                          )

@dp.message_handler(text="економічні новини")
async def bot_echo(message:types.Message):
    await message.answer(f"натисніть для отримання новини\n"
                         f"1.{list_h2[0]}\n"
                         f"2.{list_h2[1]}\n"
                         f"3.{list_h2[2]}\n"
                         f"4.{list_h2[3]}\n",reply_markup=e_n
                        
                          )
    
@dp.callback_query_handler(text='1')
async def second_step(call: types.CallbackQuery):
    await call.message.answer(f'{list_h[0]}\n'
                              f'{articles[0]}\n'
                              f'{new_links[0]}\n'
                              f'Чи бажаєте прочитати ще щось?',reply_markup=dvi_cnopke
    )


@dp.callback_query_handler(text='2')
async def second_step(call: types.CallbackQuery):
    await call.message.answer(f'{list_h[1]}\n'
                              f'{articles[1]}\n'
                              f'{new_links[1]}\n'
                              f'Чи бажаєте прочитати ще щось?',reply_markup=dvi_cnopke
    )

@dp.callback_query_handler(text='3')
async def second_step(call: types.CallbackQuery):
    await call.message.answer(f'{list_h[2]}\n'
                              f'{articles[2]}\n'
                              f'{new_links[2]}\n'
                              f'Чи бажаєте прочитати ще щось?',reply_markup=dvi_cnopke
    )
@dp.callback_query_handler(text='4')
async def second_step(call: types.CallbackQuery):
    await call.message.answer(f'{list_h[3]}\n'
                              f'{articles[3]}\n'
                              f'{new_links[3]}\n'
                              f'Чи бажаєте прочитати ще щось?',reply_markup=dvi_cnopke
    )
@dp.callback_query_handler(text='11')
async def second_step(call: types.CallbackQuery):
    await call.message.answer(f'{list_h2[0]}\n'
                              f'{articles2[0]}\n'
                              f'{new_links2[0]}\n'
                              f'Чи бажаєте прочитати ще щось?',reply_markup=dvi_cnopke
    )

@dp.callback_query_handler(text='22')
async def second_step(call: types.CallbackQuery):
    await call.message.answer(f'{list_h2[1]}\n'
                              f'{articles2[1]}\n'
                              f'{new_links2[1]}\n'
                              f'Чи бажаєте прочитати ще щось?',reply_markup=dvi_cnopke
    )

@dp.callback_query_handler(text='33')
async def second_step(call: types.CallbackQuery):
    await call.message.answer(f'{list_h2[2]}\n'
                              f'{articles2[2]}\n'
                              f'{new_links2[2]}\n'
                              f'Чи бажаєте прочитати ще щось?',reply_markup=dvi_cnopke
    )

@dp.callback_query_handler(text='44')
async def second_step(call: types.CallbackQuery):
    await call.message.answer(f'{list_h2[3]}\n'
                              f'{articles2[3]}\n'
                              f'{new_links2[3]}\n'
                              f'Чи бажаєте прочитати ще щось?',reply_markup=dvi_cnopke
    )

all_h=list_h+ list_h2
all_a=articles+articles2
all_l=new_links+new_links2
@dp.message_handler(commands="randomtopic")
async def bot_echo(message:types.Message):
    rand = random.choice(range(len(all_l)))
    await message.answer(f'{all_h[rand-1]}\n'
                         f'{all_a[rand-1]}\n'
                         f'Джерело: {all_l[rand-1]}\n'
                         f'Чи бажаєте прочитати ще щось?', reply_markup=dvi_cnopke
                            )
    
@dp.message_handler(commands=["starttest"])
async def bot_echo(message:types.Message):
    await test.test_start.set()
    await message.answer("напишіть старт тест щераз")



@dp.message_handler(commands=["starttest"],state=test.test_start)
async def bot_echo(message:types.Message):
    await test.p_1.set()
    await message.answer("кавун це ягода?",reply_markup=an1)


@dp.callback_query_handler(text="c1",state=test.p_1)
async def bot_echo(call:types.CallbackQuery):
    await test.p_2.set()
    await call.message.answer("скільки бійців у бравл старс?",reply_markup=an2)


@dp.callback_query_handler(text="c2",state=test.p_2)
async def bot_echo(call:types.CallbackQuery):
    await call.message.answer("який найновіший телефон?",reply_markup=an3)
    await test.tsantest.set()

@dp.callback_query_handler(text="c3",state=test.tsantest)
async def bot_echo(call:types.CallbackQuery):
    await call.message.answer("ви пройшли тест результата через тиждень")
text=[["ютуб"],["вайбер"],["гугл"],["квік"]]
text2=[["https://www.youtube.com/?authuser=0"],["https://www.viber.com/ua/download/"],["https://www.google.com.ua/"],["https://school-kviki.mata-platform.com/unit/index?course=tarasenko-nazar-2-riven"]]


@dp.message_handler(commands=["youtube"])
async def bot_echo(message:types.Message):
    await message.answer("linkyoutube.com",reply_markup=dynamik_kb(text[0],text2[0]))

@dp.message_handler(commands=["viber"])
async def bot_echo(message:types.Message):
    await message.answer("linkviber.com",reply_markup=dynamik_kb(text[1],text2[1]))

@dp.message_handler(commands=["google"])
async def bot_echo(message:types.Message):
    await message.answer("linkgoogle.com",reply_markup=dynamik_kb(text[2],text2[2]))


@dp.message_handler(commands=["КВІК"])
async def bot_echo(message:types.Message):
    await message.answer("linkkvick.com",reply_markup=dynamik_kb(text[3],text2[3]))


answers=[
["yes","no"],
["1","2","3"],
["1","2","3"],
["1","2","3"]
]

@dp.message_handler(commands=["test2_3p"])
async def bot_echo(message:types.Message):
    await test2_3.test_start.set()
    await message.answer("натисніть yes",reply_markup=dynamik_kb2_3(answers[0]))

@dp.callback_query_handler(text="0",state=test2_3.test_start)
async def bot_echo(call:types.CallbackQuery):
    await test2_3.p_1.set()
    await call.message.answer("питання:",reply_markup=dynamik_kb2_3(answers[1]))


@dp.callback_query_handler(text="0",state=test2_3.p_1)
async def bot_echo(call:types.CallbackQuery):
    await test2_3.p_2.set()
    await call.message.answer("питання:",reply_markup=dynamik_kb2_3(answers[2]))

@dp.callback_query_handler(text="2",state=test2_3.p_2)
async def bot_echo(call:types.CallbackQuery):
    await test2_3.P_3.set()
    await call.message.answer("питання:",reply_markup=dynamik_kb2_3(answers[3]))



@dp.callback_query_handler(text="1",state=test2_3.P_3)
async def bot_echo(call:types.CallbackQuery):
    await test2_3.tsantest.set()
    await call.message.answer("дякую за тест")