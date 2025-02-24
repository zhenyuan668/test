"""
@time : 2024/5/9 21:37
@auth : HuZhenyuan
@file : 查找存在于txt不存在于文件夹的文件名.py
"""
import os

def find_missing_files(txt_file_path, folder_path, output_txt_path):
    """
    读取TXT文件中的文件名，检查这些文件名是否存在于指定文件夹下，
    并将不存在的文件名导出到另一个TXT文件中。

    :param txt_file_path: 包含文件名的TXT文件路径
    :param folder_path: 要检查的指定文件夹路径
    :param output_txt_path: 导出不存在文件名的TXT文件路径
    """
    # 读取TXT文件中的文件名到集合中
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        file_names_in_txt = {line.strip() for line in file}

    # 获取指定文件夹下所有的文件名
    file_names_in_folder = {file for _, _, files in os.walk(folder_path) for file in files}

    # 找出存在于TXT文件中但不存在于文件夹下的文件名
    missing_files = file_names_in_txt - file_names_in_folder

    # 导出这些不存在的文件名到另一个TXT文件
    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        for file_name in missing_files:
            output_file.write(file_name + '\n')

# 使用示例
txt_file_path = "/data/zhenyuan/pretrain/轨迹文件名.txt"  # 替换为你的输入TXT文件路径
folder_path = "/data/zhenyuan/pretrain/trajectory/"  # 替换为你要检查的文件夹路径
output_txt_path = "/data/zhenyuan/pretrain/轨迹文件名2.txt"  # 替换为你想要保存的输出TXT文件路径
find_missing_files(txt_file_path, folder_path, output_txt_path)


# import os
#
# def count_files_in_directory(directory):
#     return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
#
# # 使用方法
# directory = "/data/zhenyuan/pretrain/heatmap/"  # 指定你的文件夹路径
# file_count = count_files_in_directory(directory)
# print('文件数量:', file_count)