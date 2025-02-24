"""
@time : 2025/2/15 22:59
@auth : HuZhenyuan
@file : 重命名.py
"""
import os
import csv

def find_files_by_name(root_folder):
    """ 遍历给定的根目录及其所有子目录，返回文件名到完整路径的映射。
    :param root_folder: 根目录路径
    :return: {文件名: [文件路径1, 文件路径2, ...]} 形式的字典 """
    file_dict = {}
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if filename in file_dict:
                file_dict[filename].append(full_path)
            else:
                file_dict[filename] = [full_path]
    return file_dict

def save_mapping_to_csv(mapping, csv_file):
    """ 将文件名映射保存到CSV文件中
    :param mapping: 文件名映射字典 {原始文件名: 新文件名}
    :param csv_file: CSV文件路径 """
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['原始文件名', '重命名后文件名'])
        for old_name, new_name in mapping.items():
            writer.writerow([old_name, new_name])

def rename_common_files(folder1, folder2, prefix):
    """ 递归查找两个文件夹及其子文件夹中相同的文件，并重命名。
    :param folder1: 第一个文件夹路径
    :param folder2: 第二个文件夹路径
    :param prefix: 重命名的前缀 """
    # 获取两个文件夹的文件映射
    files1 = find_files_by_name(folder1)
    files2 = find_files_by_name(folder2)

    # 找到两个文件夹中都有的文件名
    common_files = sorted(set(files1.keys()) & set(files2.keys()))
    if not common_files:
        print("没有找到两个文件夹中名称相同的文件。")
        return

    counter = 1
    rename_mapping = {}  # 用于存储文件名映射

    for filename in common_files:
        # 解析文件名和扩展名
        name, ext = os.path.splitext(filename)
        new_name = f"{prefix}{counter}{ext}"
        rename_mapping[filename] = new_name  # 记录映射关系

        # 获取文件路径
        paths1 = files1[filename]  # 文件夹1中所有该文件的路径
        paths2 = files2[filename]  # 文件夹2中所有该文件的路径

        # 进行重命名
        for path in paths1:
            new_path = os.path.join(os.path.dirname(path), new_name)
            try:
                os.rename(path, new_path)
                print(f"重命名: {path} -> {new_path}")
            except Exception as e:
                print(f"重命名 {path} 失败: {e}")

        for path in paths2:
            new_path = os.path.join(os.path.dirname(path), new_name)
            try:
                os.rename(path, new_path)
                print(f"重命名: {path} -> {new_path}")
            except Exception as e:
                print(f"重命名 {path} 失败: {e}")

        counter += 1

    # 保存映射关系到CSV文件
    csv_file = 'E:\帕金森课题\data\投稿前数据整理215\Control_rename_mapping.csv'
    save_mapping_to_csv(rename_mapping, csv_file)
    print(f"文件名映射已保存到: {csv_file}")

if __name__ == "__main__":
    # 获取用户输入的文件夹路径和文件名前缀
    folder1 = r"E:\帕金森课题\data\投稿前数据整理215\Trajectories\Control"
    folder2 = r"E:\帕金森课题\data\投稿前数据整理215\heat map\Control"
    prefix = "Con_"
    rename_common_files(folder1, folder2, prefix)
