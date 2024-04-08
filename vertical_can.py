from PIL import Image

# 图片路径列表

def vertical_concat(imgid):
    image_paths = ['data/'+imgid+'/1.png',
                   'data/'+imgid+'/2.png',
                   'data/'+imgid+'/3.png',
                   'data/'+imgid+'/4.png',
                   'data/'+imgid+'/5.png',
                   'data/'+imgid+'/6.png']

    # 加载图片
    images = [Image.open(path) for path in image_paths]

    # 将所有图片高度归一化
    # 首先找到最小高度
    min_height = min(img.height for img in images)
    # 然后将所有图片按照这个高度等比例缩放
    normalized_images = [img.resize((int(img.width * min_height / img.height), min_height)) for img in
                         images]

    # 找到所有归一化后图片的最小宽度
    min_width = min(img.width for img in normalized_images)

    # 将每张图片裁剪至最小宽度，居中裁剪
    cropped_images = []
    for img in normalized_images:
        left = (img.width - min_width) // 2
        right = left + min_width
        cropped_img = img.crop((left, 0, right, min_height))
        cropped_images.append(cropped_img)

    # 纵向拼接所有图片
    # 计算拼接后的图片的总高度
    total_height = sum(img.height for img in cropped_images)
    # 创建一个新的空白图片，宽度为最小宽度，高度为所有图片高度之和
    concatenated_image = Image.new('RGB', (min_width, total_height))
    # 将图片一张接一张地粘贴上去
    current_height = 0
    for img in cropped_images:
        concatenated_image.paste(img, (0, current_height))
        current_height += img.height

    # 保存拼接后的图片
    concatenated_image.save('data/results/'+imgid+'.png')


imgid = '00391'
vertical_concat(imgid)
print('Done!')