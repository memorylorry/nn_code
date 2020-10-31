from PIL import Image
from PIL import ImageDraw


def convertArr2IMG(arr, delta=20, bg_color=(255, 255, 255), fg_color=(200, 200, 200)):
    """
    """
    # 图片信息
    h, w = arr.shape
    # 生成背景图片
    image = Image.new('RGB', (w * delta, h * delta), bg_color)

    # 创建画刷，用来写文字到图片img上
    drawBrush = ImageDraw.Draw(image)
    
    df_color=(255, 0, 0)

    for i in range(h):
        for j in range(w):
            base_pos = (j * 20, i * 20)
            drawBrush.text(base_pos, str(arr[i][j]), fill=df_color if arr[i][j]>0 else fg_color)

    return image
