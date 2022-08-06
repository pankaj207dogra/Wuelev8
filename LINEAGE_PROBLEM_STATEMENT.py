sql_script='''
SELECT
a.uid, b.uname
FROM
(select * from user) a,
(select * from user_details) b;'''

def func_col_tabs(sql_script):
    sql_script_list=sql_script.upper().replace('\n',' ').replace(',','').replace(';','').split(' ')
    # print(sql_script_list)
    sql_cols=sql_script_list[sql_script_list.index('SELECT')+1:sql_script_list.index('FROM')]
    sql_tabs=[]
    # print(sql_cols)
    prv_from=sql_script_list.index('FROM',0)
    for i in sql_cols:
        j=sql_script_list.index(str(i.split('.')[0]))
        prv_from=sql_script_list.index('FROM',prv_from+1)
        k=sql_script_list[sql_script_list.index('FROM',prv_from)+1]
        if '.' in k:
            k=k.split('.')[1]
        sql_tabs.append(k.replace(')',''))
        # print(sql_tabs)
    for i in range(len(sql_cols)):
        if '.' in sql_cols[i]:
            sql_cols[i]=sql_cols[i].split('.')[1]

    sql_enum_lst=[]
    for i in zip(sql_cols,sql_tabs):
        sql_enum_lst.append(i)
    return sql_enum_lst

if __name__=='__main__':
    #sql_script=input("Please enter the sql script:")
    sql_enum_lst=func_col_tabs(sql_script)
    print('column => table')
    for i in sql_enum_lst:
        print(i[0],'=>',i[1])