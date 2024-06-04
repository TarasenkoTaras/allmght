from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
first=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ПРИВІТ Я КНОПКА НАЖМИ МЕНЕ",callback_data="button1")],
        [InlineKeyboardButton(text="шо надо!",callback_data="button2")]

    ]
)


b1=InlineKeyboardButton(text="1",callback_data="1")
b2=InlineKeyboardButton(text="2",callback_data="2")
b3=InlineKeyboardButton(text="3",callback_data="3")
b4=InlineKeyboardButton(text="4",callback_data="4")

p_n=InlineKeyboardMarkup().row(b1,b2,b3,b4)

bre1=InlineKeyboardButton(text="1",callback_data="11")
bre2=InlineKeyboardButton(text="2",callback_data="22")
bre3=InlineKeyboardButton(text="3",callback_data="33")
bre4=InlineKeyboardButton(text="4",callback_data="44")

e_n=InlineKeyboardMarkup().row(bre1,bre2,bre3,bre4)


d1=InlineKeyboardButton(text="це ягода",callback_data="c1")
c2=InlineKeyboardButton(text="це фрукт",callback_data="c1")
t3=InlineKeyboardButton(text="я не знаю",callback_data="c1")

an1=InlineKeyboardMarkup().row(d1,c2,t3)


d11=InlineKeyboardButton(text="78",callback_data="c2")
c22=InlineKeyboardButton(text="76",callback_data="c2")
t33=InlineKeyboardButton(text="67",callback_data="c2")
m44=InlineKeyboardButton(text="52",callback_data="c2")

an2=InlineKeyboardMarkup().row(d11,c22,t33,m44)

d1111=InlineKeyboardButton(text="я не знаю",callback_data="c3")
c2222=InlineKeyboardButton(text="не відомо",callback_data="c3")
t3333=InlineKeyboardButton(text="прозорий",callback_data="c3")
m4444=InlineKeyboardButton(text="резиновий",callback_data="c3")

an3=InlineKeyboardMarkup().row(d1111,c2222,t3333,m4444)


def dynamik_kb(text1,text2):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text1[0],url=text2[0])]
        ]
    )

def dynamik_kb2_3(text1):
    a=len(text1)
    return InlineKeyboardMarkup(
        inline_keyboard=[
           [ InlineKeyboardButton(text=text1[i],callback_data=str(i))for i in range(0,a)]
        ]
    )