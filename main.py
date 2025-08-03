from echo import Updater,CallbackContext,CommandHandler,MessageHandler,Filters
from config import TOKEN
from echo import echo,echo_audi,echo_contact,echo_ctiker,echo_photo,echo_video,echo_voice
from echo import start,help


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# command handler
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(CommandHandler('help',help))

#message hendler
dispatcher.add_handler(MessageHandler(Filters.text,echo))
dispatcher.add_handler(MessageHandler(Filters.photo,echo_photo))
dispatcher.add_handler(MessageHandler(Filters.sticker,echo_ctiker))
dispatcher.add_handler(MessageHandler(Filters.contact,echo_contact))
dispatcher.add_handler(MessageHandler(Filters.video,echo_video))
dispatcher.add_handler(MessageHandler(Filters.audio,echo_audi))
dispatcher.add_handler(MessageHandler(Filters.voice,echo_voice))


updater.start_polling()
updater.idle()