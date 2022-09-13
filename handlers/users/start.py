
from unittest import result
from aiogram.types import CallbackQuery
import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.languange import menuStart, check_button
from keyboards.default.menu_category import menuCategory, murojat, orqaga, my_contact
from loader import dp, bot
from data.config import CHANNELS
###########################################

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states.personData import PersonalData
#############################
from aiogram.types import ReplyKeyboardRemove

from utils.misc import obuna

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # for channel in CHANNELS:
    #     status = await obuna.check(user_id=message.from_user.id, channel=channel)
    
    await message.answer("Bo'limni tanglang",reply_markup=menuCategory)
    await PersonalData.shaxsi.set()
    # # await call.answer(cache_time=60)
    # else:
    #     channels_format = str()
    #     for channel in CHANNELS:
    #         chat =  await bot.get_chat(channel)
    #         invite_link = await chat.export_invite_link()
    #         channels_format += f" <a href='{invite_link}' >{chat.title}</a>\n"

    #     await message.answer(f"Botdan foydalanish uchun quydagi kanlga buna bo'ling\n {channels_format}", reply_markup=check_button, disable_web_page_preview=True)


# @dp.callback_query_handler(text="check")
# async def checker(call: types.CallbackQuery):
#     await call.answer()
#     result = str()
#     for channel in CHANNELS:
#         status = await obuna.check(user_id=call.from_user.id, channel=channel)
#         channel = await bot.get_chat(channel)
#         if status:
#             result += f"{channel.title} kanilga obuna bolgansiz\n\n"
#             await call.message.answer("Bo'limni Tanglang",reply_markup=menuCategory)
#             await PersonalData.shaxsi.set()
#         else:
#             invite_link = await channel.export_invite_link()
#             result += (f"{channel.title} kanailga obuna bolmagasiz\n <a href='{invite_link}' >obuna bo'ling</a>")
# #     await call.message.answer(result, disable_web_page_preview=True)
# @dp.message_handler(CommandStart())
# async def restart_bot(message: types.Message):
#     logging.info(message)
    
#     await message.answer("###########",reply_markup=menuCategory)
#     await PersonalData.shaxsi.set()
    
    

@dp.callback_query_handler(text="uzbek")
async def menu_Category(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("###########",reply_markup=menuCategory)
    await PersonalData.shaxsi.set()
    await call.answer(cache_time=60)

@dp.message_handler(state=PersonalData.shaxsi)
async def answer_shaxs(message:types.Message, state:FSMContext):
    shaxsi = message.text
    await state.update_data(
        {"shaxs":shaxsi}
    )
    

    await message.answer(f"👇👇Bo'limni Tanglang👇👇", reply_markup=murojat)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.murojat_turi)
async def answer_shaxs(message:types.Message, state:FSMContext):
    murojat_turi = message.text
    await state.update_data(
        {"murojat_turi":murojat_turi}
    )
    

    await message.answer(f"✍️Ism Familyangizni kiriting✍️:", reply_markup=ReplyKeyboardRemove())
    await PersonalData.next()
    


@dp.message_handler(state=PersonalData.full_name)
async def answer_shaxs(message:types.Message, state:FSMContext):
    full_name = message.text
    await state.update_data(
        {"full_name":full_name}
    )
    print(full_name)

    await message.answer(f"📞Telfon raqamingizni kiriting(+998 XXX-XX-XX):")
    
    await PersonalData.next()
    

@dp.message_handler(state=PersonalData.phone)
async def answer_shaxs(message:types.Message, state:FSMContext):
    phone = message.text
    await state.update_data(
        {"phone":phone}
    )
    print(phone)

    await message.answer(f"MUROJATGIZNI YUBORING", reply_markup=ReplyKeyboardRemove())
    await PersonalData.next()
    

# @dp.message_handler(state=PersonalData.contact)
# async def answer_shaxs(message:types.Message, state:FSMContext):
#     print("salom")
#     contact = str(message.contact.phone_number)
#     print(contact)
#     contact = message.text.contact.phone_number
#     print(contact)
    
#     await state.update_data(
#         {"contact":contact}
#     )
    

#     await message.answer(f"Murjatgizni yuboaring", reply_markup=orqaga)
#     await PersonalData.next()
    
@dp.message_handler(state=PersonalData.murojat)
async def answer_shaxs(message:types.Message, state:FSMContext):
    murojat = message.text
    await state.update_data(
        {"murojat":murojat}
    )
    

    
    data = await state.get_data()
    shaxs = data.get("shaxs")
    murojat_turi = data.get("murojat_turi")
    full_name = data.get("full_name")
    phone = data.get("phone")
    murojat = data.get("murojat")

    logging.info(message)
    msg = f"\0<b>{murojat_turi}</b>\n<b>👨‍💼Shaxsi:</b>{shaxs}\n<b>📝Ism Familya:</b>{full_name}\n📞 Aloqa: {phone}\n<b>🧾 Murjat sabab matni:</b>{murojat}"
    await bot.send_message(chat_id=5088991112, text=msg)
    await bot.send_message(chat_id=1858379541, text=msg)
    await bot.send_message(chat_id=85942449, text=msg)

    await state.finish()
    await message.answer(f"murojatingiz yuborildi", reply_markup=orqaga)
    print("shu yerda muomo")
    
    

        
        


    
    


#############################################
# @dp.message_handler(text="👨‍🎓 Talaba")
# async def student(message:types.Message):
#     await message.answer("Murojat yuboring", reply_markup=murojat)
    


# @dp.message_handler(text="👨‍👩‍👧 Ota ona")
# async def ota_ona(message:types.Message):
#     await message.answer("Murojat yuboring", reply_markup=murojat)


# @dp.message_handler(text="👨‍💼 Xodimlar")
# async def xodim(message:types.Message):
#     await message.answer("Murojat yuboring", reply_markup=murojat)

# @dp.message_handler(text="Boshqa")
# async def boshqa(message:types.Message):
#     await message.answer("Murojat yuboring", reply_markup=murojat)

# ###########################################
# @dp.message_handler(text="1.Shikoyat")
# async def student_m(message:types.Message):
#     await message.answer("Murojatingizni yo'lang!!!", reply_markup=orqaga)
#     matn = logging.info(message.text)
#     DATA.append("Shikoyat")
#     await message.answer(DATA)


# @dp.message_handler(text="2.Taklif")
# async def student_m(message:types.Message):
#     await message.answer("Murojatingizni yo'lang!!!", reply_markup=orqaga)


# @dp.message_handler(text="3.Ariza")
# async def student_m(message:types.Message):
#     await message.answer("Murojatingizni yo'lang!!!", reply_markup=orqaga)


# @dp.message_handler(text="4.Boshqa")
# async def student_m(message:types.Message):
#     await message.answer("Murojatingizni yo'lang!!!", reply_markup=orqaga)


#######################################################


@dp.message_handler(text="🔙Orqaga")
async def menu_category_back(message:types.Message):
    await message.answer("#############", reply_markup=menuCategory)








# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    logging.info(message.text)
    
    
    await message.answer("Qayta ishga tushirish uchun start ni bosing", reply_markup=orqaga)






    
    




