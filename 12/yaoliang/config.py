# coding:utf-8

class MysqlConfig():
    SQL_HOST='localhost'
    SQL_USER='root'
    SQL_PASSWD='123456'
    SQL_DB='reboot10'

class Table():
    FIELDS_USER=['id','name','name_cn','password','email','mobile','role','status']
    FIELDS_IDC=['id','name','name_cn','address','adminer','phone','num']
    FIELDS_CABINET=['id','name','idc_id','u_num','power']
    FIELDS_SERVER=['id','hostname','lan_ip','wan_ip','cabinet_id','op','phone']
    FIELDS_WORK=['id','des_name','work','work_status','handle_name','operate','des_time','handle_time']

class MyEmail():
    # 运维组邮箱账号
    LOCAL_EMAIL='yaoliang83@yeah.net'
    LOCAL_PASSWD='******'
