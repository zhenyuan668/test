"""
@time : 2024/5/9 21:16
@auth : HuZhenyuan
@file : 导出文件名.py
"""
import os

def record_png_filenames_to_txt(folder_path, txt_file_path):
    """
    记录指定文件夹下所有的png文件名，并导出为一个txt文件。

    :param folder_path: 指定的文件夹路径
    :param txt_file_path: 导出的txt文件路径
    """
    # 打开TXT文件准备写入
    with open(txt_file_path, mode='w', encoding='utf-8') as file:
        # 遍历指定文件夹
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                if file_name.endswith(".png"):
                    file.write(file_name + '\n')  # 写入文件名并换行

# 使用示例
folder_path = 'G:\轨迹数据集\wjian\轨迹'  # 替换为你的文件夹路径
txt_file_path = 'G:\轨迹数据集\wjian\轨迹文件名.txt'  # 替换为你想要保存的txt文件路径
record_png_filenames_to_txt(folder_path, txt_file_path)