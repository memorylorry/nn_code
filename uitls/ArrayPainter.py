from PIL import Image
from PIL import ImageDraw


def convertArr2IMG(arr, delta=20, bg_color=(255, 255, 255), fg_color=(0, 0, 0)):
    """
    """
    # 图片信息
    w, h = arr.shape
    # 生成背景图片
    image = Image.new('RGB', (w * delta, h * delta), bg_color)

    # 创建画刷，用来写文字到图片img上
    drawBrush = ImageDraw.Draw(image)

    for i in range(w):
        for j in range(h):
            base_pos = (i * 70, j * 20)
            drawBrush.text(base_pos, str(arr[i][j]), fill=fg_color)

    return image