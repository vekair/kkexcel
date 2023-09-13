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
    columnList = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
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
