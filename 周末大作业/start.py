import os
import sys
import time
import datetime

# authority_server = '/data/jenkins/workspace/test/tenyuns-parent/authority-server/target/authority-server-0.0.1.jar'
# certification_server = '/data/jenkins/workspace/test/tenyuns-parent/certification-server/target/certification-server-0.0.1.jar'
# gateway_server = '/data/jenkins/workspace/test/gateway-server/target/gateway-server-1.0-SNAPSHOT.jar'

# gateway_server = 'gateway-server'
# gateway_server = sys.argv[1]
jar_dir = '/data/jenkins/workspace/test/gateway-server/target/gateway-server-1.0-SNAPSHOT.jar'
backup_dir = '/data/backup/'
jar_name = jar_dir.strip().split('/')[-1]


def kill_process():
    process = os.popen("ps -ef | grep %s | grep -v grep | grep -v start.py | awk '{print $2}'" % jar_name).read()
    # print(process)
    if process == '':
        print("进程不存在")
    else:
        print("进程已存在，杀死进程")
        os.popen(f"kill -9 {process}")


def backup_jar():
    os.system(f"cp {jar_dir} {backup_dir}/{jar_name}-{time.strftime('%Y-%m-%d_%X')}")


def start_jar():
    kill_process()
    print(f"启动服务---{jar_name}")
    os.system(f"sh /Users/luwenqiang/Downloads/tomcat-{jar_name}/bin/startup.sh")
    # os.system(f"nohup java -jar {gateway_server1} > /data/workspace/{jar_name}.log 2>&1 &")
    time.sleep(1)
    backup_jar()


def rollback_jar():
    kill_process()
    print(f"启动服务---{jar_name}")
    os.system(f"sh /Users/luwenqiang/Downloads/tomcat-{jar_name}/bin/startup.sh")
    # os.system(f"nohup java -jar {gateway_server1} > /data/workspace/{jar_name}.log 2>&1 &")
    time.sleep(1)


def run():
    start_jar()


run()

