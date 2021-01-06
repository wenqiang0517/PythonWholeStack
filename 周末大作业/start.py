import os
import sys
import time

py_name = sys.argv[0].split('/')[-1]
jar_dir = sys.argv[2]
jar_name = jar_dir.strip().split('/',)[-1]
workspace_dir = '/data/workspace/test'
backup_dir = '/data/backup/jar_bak'


def kill_process(type_):
    if type_ == 'deploy':
        process = os.popen("ps -ef | grep %s | grep -v grep | grep -v %s | awk '{print $2}'" % (jar_name, py_name)).read()
    else:
        process = os.popen("ps -ef | grep %s | grep -v grep | grep -v %s | awk '{print $2}'" % (jar_name.split('-', 3)[-1], py_name)).read()
    if process == '':
        print("进程不存在")
    else:
        print("进程存在，杀死进程")
        os.system(f"kill -9 {process}")


def backup_jar():
    print(f"备份jar包---{jar_name}")
    os.system(f"/bin/cp -f {jar_dir} {backup_dir}/{time.strftime('%Y-%m-%d_%X')}-{jar_name}")


def start_jar():
    os.system(f"/bin/cp -f {jar_dir} {workspace_dir}/")
    print(f"启动服务---{jar_name}")
    # os.system(f"sh {workspace_dir}/{jar_name}/bin/startup.sh")
    os.system(f"nohup java -jar {workspace_dir}/{jar_name} >> {workspace_dir}/{jar_name}.log 2>&1 &")
    time.sleep(3)


def rollback_jar():
    print(f"回滚服务---{jar_name}")
    os.system(f"/bin/cp -f {jar_dir} {workspace_dir}/{jar_name.split('-', 3)[-1]}")
    # os.system(f"sh {workspace_dir}/{jar_name.split('-', 3)[-1]}/bin/startup.sh")
    os.system(f"nohup java -jar {workspace_dir}/{jar_name.split('-', 3)[-1]} >> {workspace_dir}/{jar_name.split('-', 3)[-1]}.log 2>&1 &")
    time.sleep(5)


def run():
    if sys.argv[1] == 'deploy':
        kill_process(sys.argv[1])
        start_jar()
        backup_jar()
        exit()
    elif sys.argv[1] == 'rollback':
        kill_process(sys.argv[1])
        rollback_jar()
        exit()
    else:
        print("输入错误,退出程序")
        exit()


run()
