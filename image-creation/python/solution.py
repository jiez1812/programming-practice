from PIL import Image

def create_image(color):
    img = Image.new('RGB', (400, 300), color=color)
    img.save('./output/basic.png')
    print(f"Image created and saved as 'output.png' with color {color}")

def create_gradient_image(color1, color2):
    width, height = 400, 300
    img = Image.new('RGB', (width, height))

    for y in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * y/height)
        g = int(color1[1] + (color2[1] - color1[1]) * y/height)
        b = int(color1[2] + (color2[2] - color1[2]) * y/height)
        
        for x in range(width):
            img.putpixel((x, y), (r, g, b))

    img.save('./output/gradient.png')
    print('Gradient image created')

if __name__ == "__main__":
    create_image((100,150,255))
    create_gradient_image((100,150,255), (200,100,255))