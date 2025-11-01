from PIL import Image, ImageDraw, ImageFont

# Load the image you want to add the watermark to
image = Image.open(r"C:\Desktop\input.jpg")  # absolute path for your image to be watermarked; Rename your image (to be watermarked) to input.jpg
width, height = image.size

# Create a drawing context
draw = ImageDraw.Draw(image)

# Define the watermark text and font
watermark_text = "StrictlyFor________Purpose"  # Change this to whatever text you want for the watermark

# Load the Verdana font from the system
# Update the path below to the location of Verdana.ttf on your computer
font_path = r"C:\Windows\Fonts\Verdana.ttf"  # Path to Verdana font file
font_size = 50  # Adjust the font size as needed
font = ImageFont.truetype(font_path, font_size)

# Calculate the text width and height
text_width, text_height = draw.textsize(watermark_text, font)

# Set the transparency level for the watermark (RGBA)
watermark_color = (238, 75, 43, 45)  # Red color with transparency

# Create an image for the watermark text
watermark_image = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))  # Transparent background
watermark_draw = ImageDraw.Draw(watermark_image)

# Draw the text on the watermark image
watermark_draw.text((0, 0), watermark_text, font=font, fill=watermark_color)

# Rotate the watermark image by 45 degrees
rotated_watermark = watermark_image.rotate(45, expand=True)

# Get the dimensions of the rotated watermark
rot_width, rot_height = rotated_watermark.size

# Increase the spacing (double the space compared to the previous version)
horizontal_spacing = rot_width + 100  # 100px space between two consecutive watermarks in the same vertical/column
vertical_spacing = rot_height + 150   # 150px space between two consecutive watermarks in the same sentence/line/row

# Now, repeat the rotated watermark across the entire image with increased spacing
for y_pos in range(0, height, vertical_spacing):  # Increase vertical spacing
    for x_pos in range(0, width, horizontal_spacing):  # Increase horizontal spacing
        # Paste the rotated watermark at the calculated position
        image.paste(rotated_watermark, (x_pos, y_pos), rotated_watermark)

# Save the image with the watermark
output_path = r"C:\Desktop\output.jpg"  # absolute path for saving the output
image.save(output_path)

# Print a confirmation message
print("Watermark added and image saved at:", output_path)
