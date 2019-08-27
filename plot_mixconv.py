import matplotlib.pyplot as plt


with open('data_mixconv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    conv2d_train = []
    conv2d_val = []
    mix_train = []
    mix_val = []
    for line in lines[1:21]:
        a, b = map(float, line.split())
        conv2d_train.append(a)
        conv2d_val.append(b)
    for line in lines[22:42]:
        a, b = map(float, line.split())
        mix_train.append(a)
        mix_val.append(b)
    print(conv2d_train)
    print(conv2d_val)
    print(mix_train)
    print(mix_val)

    x = range(20)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
    # plt.rcParams['savefig.dpi'] = 300  # 图片像素
    plt.rcParams['figure.dpi'] = 300  # 分辨率
    # plt.style.use('bmh')  # ggplot
    # plt.figure(figsize=(10, 5))
    plt.title('conv2d vs mixconv')
    plt.xlabel("epoch")
    plt.ylabel("accuracy(%)")
    plt.plot(x, conv2d_train, '-o', linestyle='-', markersize=5, color='blue', label='conv2d_train')
    plt.plot(x, conv2d_val, '-o', linestyle='--', markersize=5, color='blue', label='conv2d_val')
    plt.plot(x, mix_train, '-o', linestyle='-', markersize=5, color='red', label='mix_train')
    plt.plot(x, mix_val, '-o', linestyle='--', markersize=5, color='red', label='mix_train')
    plt.legend(loc=4)
    plt.grid(True, linestyle='--')
    # plt.savefig('mixconv_acc_20epoch.png')
    plt.show()

