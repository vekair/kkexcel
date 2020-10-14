# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import json

import xlsxwriter


# 生成excel文件
def generate_excel(expenses, NAME, itemKey):
    workbook = xlsxwriter.Workbook('./{}.xlsx'.format(NAME))
    worksheet = workbook.add_worksheet()
    keysList = [k for k in expenses[0].keys()]
    # 设定格式，等号左边格式名称自定义，字典中格式为指定选项
    # bold：加粗，num_format:数字格式
    bold_format = workbook.add_format({'bold': True})
    # money_format = workbook.add_format({'num_format': '$#,##0'})
    # date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})
    columnList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                  'Y', 'Z']
    # 将二行二列设置宽度为15(从0开始)
    worksheet.set_column(1, 1, 15)
    for index, value in enumerate(keysList):
        worksheet.write('%s1' % columnList[index], keysList[index], bold_format)
    row = 1
    col = 0
    for index, item in enumerate(expenses):
        # 使用write_string方法，指定数据格式写入数据
        worksheet.write_string(row, col, str(item['product_id']))
        worksheet.write_string(row, col + 1, item['promotion_id'])
        worksheet.write_string(row, col + 2, str(item[itemKey]))
        row += 1
    workbook.close()
