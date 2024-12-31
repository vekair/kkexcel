# /usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 01:01
# @Author: vekair

import xlsxwriter


def generate_excel(expenses, NAME):
    """
    自动顺序生成excel文件
    :param expenses: 列表、数组，里面是字典形式key,value 例如：[{"name":'XXX'}]
    :param NAME: new file name
    :return: XXX.xlsx
    """
    workbook = xlsxwriter.Workbook('{}.xlsx'.format(NAME))
    worksheet = workbook.add_worksheet()
    keysList = [k for k in expenses[0].keys()]
    # 设定格式，等号左边格式名称自定义，字典中格式为指定选项
    # bold：加粗，num_format:数字格式
    bold_format = workbook.add_format({'bold': True})
    columnList = get_columnList(len(keysList))
    # columnList = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    # 将二行二列设置宽度为15(从0开始)
    worksheet.set_column(1, 1, 15)
    for index, value in enumerate(keysList):
        worksheet.write('%s1' % columnList[index], keysList[index], bold_format)
    row = 1
    col = 0
    for index, item in enumerate(expenses):
        # 使用write_string方法，指定数据格式写入数据
        for i in range(len(item)):
            if i >= len(list(item.keys())):
                break
            worksheet.write_string(row, col + i, str(item[list(item.keys())[col + i]]))
        row += 1
    workbook.close()


def get_columnList(number):
    # 初始字符串
    current_str = 'A'
    columnList = [current_str]
    # 生成序列
    for _ in range(number):  # 26 (A-Z) + 26*26 (AA-ZZ) = 703
        current_str = next_letter_sequence(current_str)
        columnList.append(current_str)
    return columnList


def next_letter_sequence(current_str):
    """
    返回给定字符串的下一个字母序列。
    例如：给定 "Z"，返回 "AA"；给定 "AZ"，返回 "BA"。
    """
    # 将字符串转换为列表，方便操作
    current_list = list(current_str)

    # 从字符串末尾开始处理
    for i in range(len(current_list) - 1, -1, -1):
        # 如果当前字符不是'Z'，则增加1并返回结果
        if current_list[i] != 'Z':
            current_list[i] = chr(ord(current_list[i]) + 1)
            return ''.join(current_list)
        else:
            # 如果是'Z'，则将其替换为'A'，并继续处理前一个字符
            current_list[i] = 'A'

    # 如果所有字符都是'Z'，则在前面添加一个'A'
    return 'A' + ''.join(current_list)
