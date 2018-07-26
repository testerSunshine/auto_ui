## aotu_ui 是一个集成自动化测试报告Python开发web版本，他不仅有这个漂亮的外观，还有强大的功能，集成了ui，接口测试报告，使用
简单，快速上手
#### 项目依赖
- Python版本 2.7.10-2.7.14
- django版本 1.11以上
- redis最新版本（可以不安装）
- djangorestframework 3.8.2以上
- mysql 5.7
#### 项目开始
- 安装依赖，项目根目录执行命令 pip install -r requirements.txt
- mysql建表，并设置为utf-8
    ```
    create database auto_ui DEFAULT CHARACTER set utf8;
    ```
- 根目录创建执行合表,全部ok表示成功
    ```
    python manage.py migrate
    ```
- 建连接db的配置文件
    ```
    # config_aotu_ui.yaml
    ---
    db:
    ip: localhost
    port: 3306
    table: aotu_ui
    uname: root
    passwd: 123456

    ```
- 设置文件访问路径auto_ui--Config.py 文件修改路径
    ```
    if platform.system() == "Windows":
        path = os.path.join('d:\config_aotu_ui.yaml')
    else:
        path = os.path.join('/usr/local/aotuConfig/config_aotu_ui.yaml')
    f = open(path)
    s = yaml.load(f)
    f.close()
    return s
    ```
- 启动auto_ui, 允许外网访问
    ```
    python manage.py runserver 0.0.0.0:8000
    ```

#### 功能
- 所有的自动化统计报表，囊括所有的脚本运行的历史数据和进7天的脚本成功率趋势
![image](https://github.com/testerSunshine/aotu_ui/blob/master/uml/所有的自动化统计报表.jpg)
- 单次自动化统计报表，统计了单词运行脚本的详细信息，分为失败统计和全部统计和日志复盘信息
![image](https://github.com/testerSunshine/aotu_ui/blob/master/uml/单次自动化统计报表.jpg)
- 单条自动化统计报表，单条用例的详细信息，包括检查点，执行步骤，
![image](https://github.com/testerSunshine/aotu_ui/blob/master/uml/单条自动化统计报表.jpg)