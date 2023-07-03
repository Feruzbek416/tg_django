from aiogram.dispatcher.filters.state import State,StatesGroup

class FeedbackState(StatesGroup):
    body = State()
    name = State()
    surname = State()
    age = State()
    school = State()



