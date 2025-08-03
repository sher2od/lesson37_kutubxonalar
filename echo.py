from telegram.ext import Updater,CallbackContext,CommandHandler,MessageHandler,Filters
from telegram import Update
from config import TOKEN

def start(update:Update,context:CallbackContext):
    user = update.message.from_user

    update.message.reply_text(
        f'assalomu alaykum {user.full_name}.\n\n'
        'bu bot eko bot'
    )

def help(update:Update,context:CallbackContext):
    update.message.reply_text('' \
    'Qanday yordam beraolaman'
    )

def echo(update:Update,context:CallbackContext):
    update.message.reply_text(update.message.text)


def echo_photo(update:Update,context:CallbackContext):
    photo = update.message.photo[0]

    update.message.reply_photo(photo=photo)

def echo_ctiker(update:Update,context:CallbackContext):
    ctiker = update.message.sticker

    update.message.reply_sticker(sticker=ctiker)

def echo_contact(update:Update,context:CallbackContext):
    contact = update.message.contact

    update.message.reply_contact(contact=contact)


def echo_video(update:Update,context:CallbackContext):
    video = update.message.video

    update.message.reply_video(video=video)

def echo_audi(update:Update,context:CallbackContext):
    audi = update.message.audio

    update.message.reply_audio(audio=audi)

def echo_voice(update:Update,context:CallbackContext):
    voice = update.message.voice

    update.message.reply_voice(voice)