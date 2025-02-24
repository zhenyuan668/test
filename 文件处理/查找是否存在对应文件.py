"""
@time : 2025/2/15 22:33
@auth : HuZhenyuan
@file : 查找是否存在对应文件.py
"""
import os


def get_all_filenames(root_path):
    """获取路径下所有文件的文件名（不包括路径）"""
    filenames = set()
    for dirpath, _, files in os.walk(root_path):
        for file in files:
            filenames.add(file)
    return filenames


def find_missing_files(path1, path2):
    """查找在 path1 中但不在 path2 中，或在 path2 但不在 path1 中的文件"""
    files1 = get_all_filenames(path1)
    files2 = get_all_filenames(path2)

    only_in_path1 = files1 - files2
    only_in_path2 = files2 - files1

    print("存在于路径1但不存在于路径2的文件:")
    for file in sorted(only_in_path1):
        print(file)

    print("\n存在于路径2但不存在于路径1的文件:")
    for file in sorted(only_in_path2):
        print(file)


# 示例使用
path1 = "E:\帕金森课题\data\投稿前数据整理215\Trajectories"  # 替换为你的路径1
path2 = "E:\帕金森课题\data\投稿前数据整理215\heat map"  # 替换为你的路径2
find_missing_files(path1, path2)
