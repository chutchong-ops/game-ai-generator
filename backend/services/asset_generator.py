from PIL import Image, ImageDraw, ImageFont
import random

class AssetGenerator:
    def __init__(self, sprite_size=(32, 32), sheet_size=(256, 256)):
        self.sprite_size = sprite_size
        self.sheet_size = sheet_size

    def generate_sprite(self, color=None):
        """Generate a single sprite with a given color."""
        if color is None:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        sprite = Image.new('RGB', self.sprite_size, color)
        draw = ImageDraw.Draw(sprite)
        draw.rectangle([5, 5, self.sprite_size[0]-5, self.sprite_size[1]-5], fill=color)
        return sprite

    def generate_sprite_sheet(self, num_sprites):
        """Generate a sprite sheet with a specified number of sprites."""
        sheet = Image.new('RGB', self.sheet_size)
        for i in range(num_sprites):
            sprite = self.generate_sprite()
            x = (i % (self.sheet_size[0] // self.sprite_size[0])) * self.sprite_size[0]
            y = (i // (self.sheet_size[0] // self.sprite_size[0])) * self.sprite_size[1]
            sheet.paste(sprite, (x, y))
        return sheet

    def save_sprite(self, sprite, file_path):
        """Save the generated sprite to a file."""
        sprite.save(file_path)

    def generate_random_sprite(self):
        """Generate a random sprite with a random color."""
        return self.generate_sprite()
