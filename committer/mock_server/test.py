from os.path import join, split, realpath
import sqlite3

body = {
    'title': '提交测试',
    'keywords': 'Test;bug',
    'product_id': '1',
    'project_id': '2',
    'module_id': '1',
    'branch_id': '1',
    'type': 'baselineedition',
    'severity': '1',
    'pri': '0',
    'assigned': '1',
    'os': 'ios',
    'browser': 'uos',
    'content': '# 提交测试\n## 测试\nHello World',
    'creator': '3'
}
path = split(realpath(__file__))[0]
conn = sqlite3.connect(join(path, 'test.db'))
cursor = conn.cursor()

print(str(tuple(body.values())))

#cursor.execute(
#    "insert into `Commit` (title,keywords) values (\'Bug B\',\'test\')")
# conn.commit()
cursor.close()
conn.close()
