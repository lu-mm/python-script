#!/usr/bin/python
# -*- coding: utf-8 -*-


import optparse
from slow_log import Connection


class main():
    send_mail=''
    instanceid=''
    aliyun_access_key=''
    aliyun_access_secret=''
    aliyun_region=''
    parser = optparse.OptionParser()
    parser.add_option('-i','--instanceid',dest='instanceid',default=instanceid ,help="RDS instance id")
    parser.add_option('--date',dest='date', default=None, help="slowlog endtime.The default is now time.example：2019-09-25")
    parser.add_option('--day',dest='day',default=1, help="How many days of slow log,The default is one day")
    parser.add_option('--mail', dest='mail', default=send_mail, help="send mail address，delimiter \",\",Don't send mail input \"None\" ")
    (options, args) = parser.parse_args()

    connect=Connection(aliyun_access_key=aliyun_access_key,aliyun_access_secret=aliyun_access_secret,aliyun_region=aliyun_region)
    # a=connect.get_db_instances()
    connect.get_slow_logs(db_instance_id=options.instanceid,endtime=options.date,day=options.day,send_mail=options.mail)

