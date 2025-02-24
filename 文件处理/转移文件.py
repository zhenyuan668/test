"""
@time : 2025/2/15 23:32
@auth : HuZhenyuan
@file : 转移文件.py
"""
import os
import shutil

def move_files_to_parent_folder(parent_folder):
    """
    将给定文件夹下所有子文件夹中的文件转移到父文件夹下。

    :param parent_folder: 父文件夹路径
    """
    # 确保目标文件夹存在
    if not os.path.exists(parent_folder):
        print(f"指定的父文件夹 '{parent_folder}' 不存在！")
        return

    # 遍历父文件夹中的所有内容
    for dirpath, dirnames, filenames in os.walk(parent_folder, topdown=False):
        # 跳过父文件夹本身
        if dirpath == parent_folder:
            continue

        for filename in filenames:
            # 构造源文件路径和目标文件路径
            src_path = os.path.join(dirpath, filename)
            dst_path = os.path.join(parent_folder, filename)

            # 检查目标路径是否已有同名文件，如果有，重新命名
            if os.path.exists(dst_path):
                name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(dst_path):
                    dst_path = os.path.join(parent_folder, f"{name}_{counter}{ext}")
                    counter += 1

            try:
                # 移动文件
                shutil.move(src_path, dst_path)
                print(f"已将文件 '{src_path}' 移动到 '{dst_path}'")
            except Exception as e:
                print(f"移动文件 '{src_path}' 时发生错误: {e}")

        # 删除空子文件夹
        if not os.listdir(dirpath):  # 如果子文件夹为空
            try:
                os.rmdir(dirpath)
                print(f"已删除空文件夹 '{dirpath}'")
            except Exception as e:
                print(f"删除文件夹 '{dirpath}' 时发生错误: {e}")

if __name__ == "__main__":
    # 用户输入文件夹路径
    parent_folder = "E:\帕金森课题\data\投稿前数据整理215\Trajectories\Third"
    move_files_to_parent_folder(parent_folder)
