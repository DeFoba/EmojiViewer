from PIL import Image, ImageDraw, ImageFont
from emoji_selector import Emoji

IMAGE_NAME = 'image.png'
image = Image.new('RGBA', (240 * 4, 270), (50, 50, 50, 0))
emoji = Emoji()

# Text
# unicode_font = ImageFont.truetype("EmojiOneBW.otf", 56)

# img = ImageDraw.Draw(image)
# img.text((10, 10), emoji.get(), font=unicode_font)

count = -1
for sticker_path in emoji.get():
    count += 1

    sticker = Image.open(sticker_path)
    sticker = sticker.resize((240, 240))
    image.paste(sticker, (240 * count or 10, 10), sticker)

image.save(IMAGE_NAME, 'PNG')