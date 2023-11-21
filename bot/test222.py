from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

# Укажите ID админов, которым разрешено отправлять сообщения
admin_ids = {1377050746, 987654321}

# Укажите реальные ID ваших групп
group_chat_ids = [-1002086937947, -4080817111, -100987654321]

def is_admin(user_id):
    return user_id in admin_ids

def echo_all(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Да", callback_data='yes'),
                 InlineKeyboardButton("Нет", callback_data='no')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    user_id = update.message.from_user.id
    if user_id not in admin_ids:
        update.message.reply_text("У вас нет разрешения отправлять сообщения.")
        return

    if update.message.text:
        text = update.message.text
        for group_chat_id in group_chat_ids:
            context.bot.send_message(chat_id=group_chat_id, text=text, reply_markup=reply_markup)
    elif update.message.photo:
        caption = update.message.caption if update.message.caption else ""
        photo = update.message.photo[-1]
        for group_chat_id in group_chat_ids:
            context.bot.send_photo(chat_id=group_chat_id, photo=photo.file_id, caption=caption, reply_markup=reply_markup)
    else:
        text = "Сообщение с неизвестным типом"
        for group_chat_id in group_chat_ids:
            context.bot.send_message(chat_id=group_chat_id, text=text, reply_markup=reply_markup)

message_handler = MessageHandler(Filters.all & ~Filters.command, echo_all)

def button(update: Update, context: CallbackContext):
    query = update.callback_query

    if query.data == 'yes':
        context.bot.send_message(chat_id=query.message.chat_id, text="Отправляю в группы...")

        if query.message.text:
            for group_chat_id in group_chat_ids:
                context.bot.send_message(chat_id=group_chat_id, text=query.message.text)
        elif query.message.photo:
            photo = query.message.photo[-1]
            caption = query.message.caption if query.message.caption else ""
            for group_chat_id in group_chat_ids:
                context.bot.send_photo(chat_id=group_chat_id, photo=photo.file_id, caption=caption)

    else:
        query.edit_message_text(text="Пожалуйста, отправьте новое сообщение.")

button_handler = CallbackQueryHandler(button)

updater = Updater(token='6769072442:AAHPHW1_iqZ1D7V4hXiy0i81KW5hu1II5So')
dispatcher = updater.dispatcher

dispatcher.add_handler(message_handler)
dispatcher.add_handler(button_handler)

if __name__ == "__main__":
    try:
        print('start...')
        updater.start_polling()

    except Exception as e:
        print(f'Error: {e}')
