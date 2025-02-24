"""
@time : 2025/1/27 20:46
@auth : HuZhenyuan
@file : 补充文件名前缀.py
"""
import os


def rename_png_files(folder_path, prefix="mx_2_day3_mx_"):
    """
    修改指定文件夹下所有png文件的文件名，在文件名前加上固定前缀。

    :param folder_path: 文件夹路径
    :param prefix: 要添加的前缀
    """
    # 检查文件夹路径是否存在
    if not os.path.exists(folder_path):
        print(f"文件夹路径 '{folder_path}' 不存在！")
        return

    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)

    # 遍历文件并重命名
    for file_name in files:
        # 检查文件扩展名是否是 .png
        if file_name.lower().endswith(".png"):
            old_path = os.path.join(folder_path, file_name)
            new_name = prefix + file_name
            new_path = os.path.join(folder_path, new_name)

            # 重命名文件
            os.rename(old_path, new_path)
            print(f"文件重命名: {file_name} -> {new_name}")

    print("所有png文件已重命名！")


# 使用示例
folder = r"E:\帕金森课题\data\投稿前数据整理\heat map\Sixth\data3"  # 替换为你的文件夹路径
rename_png_files(folder)
