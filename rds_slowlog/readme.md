## rds的慢sql接口脚本

### 脚本内容

默认不传参数，获取当天00:00之前的一天的慢日志明细生成csv文件，csv文件以日期为文件名，默认发送邮件，不发送邮件传参数解决

###  脚本使用方式

1. 修改main.py里面阿里云账号信息

   ```shell
   send_mail=''
   instanceid=''
   aliyun_access_key=''
   aliyun_access_secret=''
   aliyun_region=''
   ```

   

2. 执行脚本

```shell
#帮助，都有默认值，可以不传
main.py -h
-i INSTANCEID, --instanceid=INSTANCEID
                        RDS instance id,The default is rm-2ze76t71kh0jv9689
  --date=DATE           slowlog endtime.The default is now
                        time.example：2019-09-25
  --day=DAY             How many days of slow log,The default is one day
  --mail=MAIL           send mail address，delimiter ",",Don't send mail
                        input "None"

```

