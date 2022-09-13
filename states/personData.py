from aiogram.dispatcher.filters.state import StatesGroup, State



class PersonalData(StatesGroup):
    shaxsi =State()
    murojat_turi = State()
    full_name = State()
    phone = State()
    
    murojat = State()