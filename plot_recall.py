import matplotlib.pyplot as plt


with open('data_recall.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    total_img = 0
    batch_size = []
    img_recall = []
    x = range(8)
    for i in range(len(lines)):
        if i == 0:
            total_img = int(lines[i].split()[0])
        else:
            batch_size.append(int(lines[i].split()[0]))
            img_recall.append(int(lines[i].split()[1]) / total_img)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
    # plt.rcParams['savefig.dpi'] = 300  # 图片像素
    plt.rcParams['figure.dpi'] = 300  # 分辨率
    # plt.style.use('bmh')  # ggplot
    # plt.figure(figsize=(10, 5))
    plt.title('不同batch_size下的样本召回率')
    plt.xlabel("batch_size")
    plt.ylabel("recall(%)")
    plt.plot(x, img_recall, '-o', linestyle='--', markersize=10, color='blue')
    plt.xticks(x, batch_size, rotation=0)
    plt.grid(True, linestyle='--')
    plt.savefig('batch_size_recall.png')
    plt.show()

