from telebot import types
from telebot.states.asyncio.context import StateContext
from src.bot_instance import bot

def register_handlers(bot):

    @bot.message_handler(commands=['start'])
    async def start_handler(message: types.Message, state: StateContext):
        await bot.send_message(message.chat.id, text='OK')

#
#
#
#
#
#
#
#
# def register_handlers(bot):
#     @bot.message_handler(commands=["start"])
#     async def start_handler(message: types.Message, state: StateContext):
#         await handle_start(bot, message.from_user.id, state)
#
#     @bot.message_handler(commands=['show_rules'])
#     async def rules_handler(message: types.Message, state: StateContext):
#         await show_rules(bot, message, state)
#
#     @bot.message_handler(state="*", commands=["cancel"])
#     async def any_state(message: types.Message, state: StateContext):
#         await handle_any_state(bot, message, state)
#
#     @bot.message_handler(commands=["lang"])
#     async def change_language_handler(message: types.Message, state: StateContext):
#         await handle_command_selection(bot, message, state)
#
#     @bot.message_handler(commands=["cmd_input"])
#     async def cmd_input_handler(message: types.Message):
#         keyboard = await tcm.commands_inline_keyboard_menu(user_id=message.from_user.id)
#         await bot.send_message(message.chat.id, "Choose an option:", reply_markup=keyboard)
#
#
#
#     @bot.callback_query_handler(func=lambda call: call.data in tcm.menu)
#     #describe menu objects here
#     async def parcer(call: types.CallbackQuery, state: StateContext):
#         await bot.send_message(call.from_user.id, "activated")
#         if call.data == "/menu":
#             await handle_start(bot, call.from_user.id, state)
#
#
#
#
#     @bot.callback_query_handler(func=lambda call: call.data in _.ACRONYMS,
#                                 state=LanguageChanger.language)
#     async def language_command_handler(call: types.CallbackQuery, state: StateContext):
#         await handle_callback_data_language(bot, call, state)
#
#
#     @bot.callback_query_handler(func=lambda call: call.data in _.ACRONYMS,
#                                 state=RegistrateUser.waiting_for_language)
#     async def language_handler(call: types.CallbackQuery, state: StateContext):
#         await handle_language_selection(bot, call, state)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     @bot.message_handler(state=RegistrateUser.waiting_for_start)
#     async def name_get(message: types.Message, state: StateContext):
#         await handle_start(bot, message, state)
#
#     @bot.message_handler(state=RegistrateUser.waiting_for_name)
#     async def name_get(message: types.Message, state: StateContext):
#         await handle_name_input(bot, message, state)
#
#
#     @bot.message_handler(state=RegistrateUser.waiting_for_last_name)
#     async def last_name_get(message: types.Message, state: StateContext):
#         await handle_last_name_input(bot, message, state)
#
#
#     @bot.callback_query_handler(func=lambda call: call.data in ['male', 'female'],
#                                 state=RegistrateUser.waiting_for_sex)
#     async def sex_handler(call: types.CallbackQuery, state: StateContext):
#         await handle_sex_selection(bot, call, state)
#
#
#     @bot.message_handler(state=RegistrateUser.waiting_for_age, is_digit=True)
#     async def age_get(message: types.Message, state: StateContext):
#         await handle_age_input(bot, message, state)
#
#
#     @bot.message_handler(state=RegistrateUser.waiting_for_email)
#     async def email_get(message: types.Message, state: StateContext):
#         await handle_email_input(bot, message, state)

    #
    # @bot.message_handler(state=RegistrateUser.waiting_for_city)
    # async def city_get(message: types.Message, state: StateContext):
    #     await handle_city_input(bot, message, state)
    #
    #
    # @bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no'],
    #                             state=AgreementRules.waiting_for_agreement)
    # async def rules_acceptance_handler(call: types.CallbackQuery, state: StateContext):
    #     await handle_rules_acceptance(bot, call, state)
