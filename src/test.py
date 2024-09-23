from fer import FER
import cv2
import pprint;
from PIL import Image, ImageDraw, ImageFont

img = cv2.imread("多照.jpg")
detector = FER()
result=detector.detect_emotions(img)
print(result);
# pprint.pprint(result);

# 初始化Pillow图像对象
pil_img = Image.fromarray(img)
draw = ImageDraw.Draw(pil_img)

# 字体设置
font_path = 'Action_Man.ttf'
font_size = 18
font = ImageFont.truetype(font_path, font_size)


for item in result:
    print(item);

    [x,y,w,h]=item['box'];
    emotion_label=item['emotions'];
    print(x,y,w,h);
    print(emotion_label);

    # 绘制边界框
    draw.rectangle([x, y, x + w, y + h], outline='orange', width=5)

    # 在边界框下方写上情绪标签
    text_position = (x, y + h + 15)

    # 找出最大的情绪值及其对应的标签
    max_emotion = max(emotion_label, key=emotion_label.get)
    max_emotion_value = emotion_label[max_emotion]

    # 准备情绪标签的文本
    lines = [f"{key}: {value:.2f}" for key, value in emotion_label.items()]

    # 绘制每一行文本
    for line in lines:
         # 如果当前行是最大情绪值，则使用绿色，否则使用白色
        fill_color = 'green' if line.startswith(max_emotion + ':') else 'white'
        draw.text(text_position, line, font=font, fill=fill_color)
        # 更新文本位置以绘制下一行
        text_position = (text_position[0], text_position[1] + font_size)

# 显示新图片
pil_img.show()