from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pandas as pd

data = pd.read_excel(r'input.xlsx')
df = pd.DataFrame(data)
names = (df['Name'].tolist())
for i in range(len(df)):
    img = Image.open("template.jpg")
    draw = ImageDraw.Draw(img)
    selectFont = ImageFont.truetype("arial.ttf", size=150)
    draw.text((1220, 1150), names[i], (34, 34, 34), font=selectFont)
    img.save('output/'+names[i]+'.pdf', "PDF", resolution=100.0)
