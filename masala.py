
from PIL import Image, ImageFilter

class ImageChanger:
    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(filename)

    def resize(self):
        new_image = self.image.resize((80, 80))
        new_image.save('miniphoto.jpg')
        print("Image resized and saved as newphoto.jpg")

    def crop(self, left, top, right, bottom):
        new_image = self.image.crop((left, top, right, bottom))
        new_image.save('newphoto.jpg')
        print("Image cropped and saved as newphoto.jpg")

    def passport_formatter(self):
        width, height = self.image.size
        if width > height * 1.5:
            crop_width = height * 1.5
            left = (width - crop_width) // 2
            right = left + crop_width
            new_image = self.image.crop((left, 0, right, height))
        else:
            crop_height = width / 1.5
            top = (height - crop_height) // 2
            bottom = top + crop_height
            new_image = self.image.crop((0, top, width, bottom))
        new_image.save('newphoto.jpg')
        print("Passport formatted image saved as newphoto.jpg")

    def black(self):
        new_image = self.image.convert("L")
        new_image.save('newphoto.jpg')
        print("Image converted to black and white and saved as newphoto.jpg")

    def combine(self, other_filename):
        other_image = Image.open(other_filename)
        width, height = self.image.size
        other_image = other_image.resize((width, height))
        new_image = Image.blend(self.image, other_image, alpha=0.5)
        new_image.save('modified_image.jpg')
        print("Images combined and saved as modified_image.jpg")

# Example usage:
imagechanger = ImageChanger('photo1.jpg')
imagechanger.resize()
imagechanger.crop(100, 50, 200, 250)
imagechanger.passport_formatter()
imagechanger.black()
imagechanger.combine('photo2.jpg')
































# from PIL import Image

# class ImageChanger:
#     def __init__(self, filename):
#         self.filename = filename
#         self.image = Image.open(filename)

#     def resize(self, width, height):
#         """Resizes the image to the given dimensions."""
#         self.image = self.image.resize((width, height))

#     def crop(self, left, top, right, bottom):
#         """Crops the image to the given coordinates."""
#         self.image = self.image.crop((left, top, right, bottom))



#     def passport_formatter(self):
#         """Formats the image for passport photo specifications."""
#         # 3x4 aspect ratio for passport photos
#         width, height = self.image.size
#         if width > height * 1.5:
#             # Crop from the sides
#             crop_width = height * 1.5
#             left = (width - crop_width) // 2
#             right = left + crop_width
#             self.image = self.image.crop((left, 0, right, height))
#         else:
#             # Crop from the top and bottom
#             crop_height = width / 1.5
#             top = (height - crop_height) // 2
#             bottom = top + crop_height
#             self.image = self.image.crop((0, top, width, bottom))

#         # Resize to 3x4 inches (approximately 350x470 pixels)
#         self.resize(350, 470)

#     def black(self):
#         """Converts the image to black and white."""
#         self.image = self.image.convert("L")

#     def save(self, filename):
#         """Saves the modified image to the given filename."""
#         self.image.save(filename)

#     def combine(self, other_filename):
#         """Combines the current image with another image."""
#         other_image = Image.open(other_filename)

#         # Resize both images to the same size for easier combination
#         width, height = self.image.size
#         other_image = other_image.resize((width, height))

#         # Combine the images using the 'blend' mode (other modes available)
#         self.image = Image.blend(self.image, other_image, alpha=0.5)


# image_changer = ImageChanger("photo1.jpg")

# # Apply various modifications
# image_changer.resize(500, 300)
# image_changer.crop(100, 50, 400, 250)

# image_changer.passport_formatter()
# image_changer.black()

# # Save the modified image
# image_changer.save("modified_image.jpg")

# # Combine with another image
# image_changer.combine("photo2.jpg")
# image_changer.save("combined_image.jpg")

