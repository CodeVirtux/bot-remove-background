# # Demander à l'utilisateur de saisir les deux nombres
# N1 = float(input("Entrez le premier nombre : "))
# N2 = float(input("Entrez le deuxième nombre : "))

# # Comparer les deux nombres et affecter le plus grand à N1 et le plus petit à N2
# if N1 < N2:
#     N1, N2 = N2, N1

# # Afficher les résultats
# print("Le plus grand nombre est :", N1)
# print("Le plus petit nombre est :", N2)


# Demander à l'utilisateur de saisir un nombre entier n
n = int(input("Entrez un nombre entier n : "))

# Initialiser la somme à 0
somme = 0

# Utiliser une boucle pour calculer la somme des n premiers nombres entiers
for i in range(1, n + 1):
    somme += i

# Afficher le résultat



# async def main():
#     bot = telegram.Bot(TOKEN)

#     async with bot:
#         update = (await bot.get_updates())[-1]
#         chat_id = update.message.chat_id
#         user_name = update.message.from_user.first_name
#         await bot.send_message(text=f"hello {user_name}" , chat_id=chat_id)



# from telegram import Update
# from telegram.ext import ApplicationBuilder , CommandHandler, ContextTypes, MessageHandler, filters

# TOKEN = "8138120207:AAE-lDPK0ZyLGAmawcF-g-_T9xXrYpduEDQ"

# async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="I am a background remval bot. to start click on /start")

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="to remove a background from an image please send me the image.")

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update)
    

# if __name__=="__main__":
#     Application= ApplicationBuilder().token(TOKEN).build()

#     # command handlers
#     help_handler = CommandHandler("help",help)
#     start_handler = CommandHandler("start",start)
#     message_handler = MessageHandler(filters.All, handle_message)

#     #register command
#     Application.add_handler(help_handler)
#     Application.add_handler(start_handler)
#     Application.add_handler(message_handler)

#     Application.run_polling()  