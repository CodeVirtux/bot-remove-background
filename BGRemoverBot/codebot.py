import os
from rembg import remove, new_session
import concurrent.futures
from PIL import Image 
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8138120207:AAE-lDPK0ZyLGAmawcF-g-_T9xXrYpduEDQ"
# Load the ONNX model once  
session = new_session("isnet-general.onnx")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I am a background removal bot. To start, click on /start")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="To remove a background from an image, please send me the image.")

# Function to process images using rembg with ONNX acceleration
async def process_image(photo_name: str):
    name, _ = os.path.splitext(photo_name)
    output_photo_path = f"./processed/{name}.png"
    
    input_img = Image.open(f"./input_images/{photo_name}")
   
    output = remove(input_img)
    output.save(output_photo_path)
    
    os.remove(f"./input_images/{photo_name}") 
    return output_photo_path

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if filters.PHOTO.check_update(update):
        file_id = update.message.photo[-1].file_id
        unique_file_id = update.message.photo[-1].file_unique_id
        photo_name = f"{unique_file_id}.jpg" 

    elif filters.Document.IMAGE.check_update(update):
        file_id = update.message.document.file_id
        _, f_ext = os.path.splitext(update.message.document.file_name)
        unique_file_id = update.message.document.file_unique_id
        photo_name = f"{unique_file_id}.{f_ext}"

    photo_file = await context.bot.get_file(file_id)
    await photo_file.download_to_drive(custom_path=f"./input_images/{photo_name}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="We are processing your image. Please wait...")
    
    processed_image_path = await process_image(photo_name)  # Renamed variable
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open(processed_image_path, 'rb'))
    
    os.remove(processed_image_path)  # Clean up the processed file

if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()

    # Command handlers
    help_handler = CommandHandler("help", help_command)
    start_handler = CommandHandler("start", start)
    message_handler = MessageHandler(filters.PHOTO | filters.Document.IMAGE, handle_message)

    # Register commands
    application.add_handler(help_handler)
    application.add_handler(start_handler)
    application.add_handler(message_handler)

    application.run_polling()