╔══☆ WELCOME TO ☆══╗
       🎓 EDU MIRAI 🎓
╚════════════════╝

👤  Name       ⫸ {name}
🆔  ID         ⫸ {user_id}
🔗  Username   ⫸ {username}
👥  Members    ⫸ {members}

~✧~✧~✧~✧~✧~✧~✧~✧~✧~✧~
      ⚡ MADE BY : @JNNEXRIL
~✧~✧~✧~✧~✧~✧~✧~✧~✧~✧~from telegram import Update, ParseMode
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = "8211105344:AAFSbD0pZOrFLwp9twSNfx1UHITLdJ7PrY0"

def welcome(update: Update, context: CallbackContext):
    for user in update.message.new_chat_members:
        name = user.full_name
        user_id = user.id
        username = f"@{user.username}" if user.username else "No Username"
        members = context.bot.get_chat_members_count(update.effective_chat.id)

        text = f"""
✨ *WELCOME* ✨

👤 *Name* : {name}
🆔 *User ID* : `{user_id}`
🔗 *Username* : {username}
👥 *Total Members* : {members}

━━━━━━━━━━━━━━
🛠 *MADE BY* : @JnNexril
"""
        update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

updater.start_polling()
updater.idle()
