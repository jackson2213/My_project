def get_input_args(num_arg,split_str=' ',dtype=int):
    '''
    :param num_arg: 需要得到多少个参数
    :param split_str: 参数之前分隔符，默认空格
    :param dtype: 输入类型
    :return: 如果输入一个参数，则返回一个具体值，多个参数返回一个tupe类型
    '''
    row1 = list(map(dtype, input().split(split_str)))
    while True:
        if len(row1)==int(num_arg):
            break
        else:
            print('input argd invalid, please re-input')
            row1.clear()
            try:
                row1 = list(map(dtype, input().split(split_str)))
            except:
               
                continue
    return tuple(row1) if num_arg>1 else row1[0]


h,w = get_input_args(2)
print("please input array" )
row = []
img = []
col = h
for i in range(col):
    row = get_input_args(w)
    img.append(row)
print("please input m")
m = get_input_args(1)
print("please input mask")
mask = []
row1 = []
col1 = int(m)
for j in range(col1):
    row1 = get_input_args(int(m))
    mask.append(row)

def get_mask_value(img,mask,m):
    value = None
    for i in range (m):
        for j in range (m):
            value+=img[i][i]*mask[i][j]
    return value







new_img = []
for i in range(h-m+1):
    row = []
    temp_img = img[i:i+m]
    for j in range(w-m+1):
        input_img = []
        for r_img in temp_img:
            input_img.append(r_img[j:j+m])
        value = get_mask_value(input_img,mask,m)
        row.append(value)
    new_img.append(row)