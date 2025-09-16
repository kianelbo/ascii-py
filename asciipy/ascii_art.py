from PIL import Image, ImageDraw, ImageFilter, ImageEnhance


class AsciiArt:
    char_map = " `'\".,:;i!~-+]{|1\\rxucoz6?UCL0O*#W&B@$$"

    def __init__(self, filename, resolution=None):
        # loading image
        img = Image.open(filename)
        if resolution is not None:
            img = img.resize((resolution * round(img.size[0] / img.size[1]), resolution))
        self.image = img
        self.width, self.height = img.size

        # enhance image for cleaner result
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.image = ImageEnhance.Contrast(self.image).enhance(2)

        # 2d array of pixel
        rgb_matrix = list(self.image.getdata())
        self.rgb_matrix = [rgb_matrix[j:j + self.width] for j in range(0, len(rgb_matrix), self.width)]
        # rgb values to intensity values
        intensity_matrix = [[.21 * p[0] + .72 * p[1] + .07 * p[2] for p in pixel_row] for pixel_row in self.rgb_matrix]
        # intensity values to characters
        self.char_matrix = [[self.char_map[int(i * (len(self.char_map) - 1) / 255)] for i in i_row] for i_row in intensity_matrix]

    def to_image(self, color=False):
        output = Image.new('RGB', (self.width * 10, self.height * 10))
        draw = ImageDraw.Draw(output)

        for y in range(self.height):
            for x in range(self.width):
                fill = self.rgb_matrix[y][x] if color else (255, 255, 255)
                draw.text((x * 10, y * 10), self.char_matrix[y][x], fill=fill)

        return output

    def to_text(self):
        return str(self)

    def __str__(self):
        string = ""
        for row in self.char_matrix:
            line = [p + p + p for p in row]
            string += ''.join(line) + '\n'
        return string
