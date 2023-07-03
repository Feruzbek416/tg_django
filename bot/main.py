from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from buttons import *
from states import *
from api import *

API_TOKEN = '6306009998:AAH1luJB5EXbMoF6ZdHAueaPr1N6k9yMom8'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f'Salom {message.from_user.full_name}',reply_markup=keyboard,parse_mode='HTML')


@dp.message_handler(Text(startswith="Adminga ma'lumot jo'natish"))
async def feedback_1(message: types.Message):
    await message.answer('Xabarni junating')
    await FeedbackState.body.set()


@dp.message_handler(state=FeedbackState.body)
async def feedback_2(message: types.Message,state:FSMContext):
    body = message.text
    await state.update_data({'body':body})
    await message.answer("ismingizni kiriting!")
    await FeedbackState.next()


@dp.message_handler(state=FeedbackState.name)
async def feedback_3(message: types.Message,state:FSMContext):
    name = message.text
    await state.update_data({'name':name})
    await message.answer("familiyangizni kiriting!")
    await FeedbackState.next()

@dp.message_handler(state=FeedbackState.surname)
async def feedback_4(message: types.Message,state:FSMContext):
    surname = message.text
    await state.update_data({'surname':surname})
    await message.answer("yoshingizni kiriting!")
    await FeedbackState.next()

@dp.message_handler(state=FeedbackState.age)
async def get_age(message: types.Message,state:FSMContext):
    age = message.text
    await state.update_data({'age':age})
    await message.answer("sinfingizni kiriting!")
    await FeedbackState.next()

@dp.message_handler(state=FeedbackState.school)
async def get_age(message: types.Message,state:FSMContext):
    school = message.text
    await state.update_data({'school':school})
    data = await state.get_data()
    await message.answer(create_feedback(message.from_user.id,data['body'],data['age'],data['name'],data['surname'],data['school']))
    await state.finish()



if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)