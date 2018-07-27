## auto_ui 是一个集成自动化测试报告Python开发web版本，他不仅有这个漂亮的外观，还有强大的功能，集成了ui，接口测试报告，使用简单，快速上手
#### 项目地址，觉得好用的帮忙点个小✨✨
- https://github.com/testerSunshine/auto_ui
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
        path = os.path.join('d:\config_auto_ui.yaml')
    else:
        path = os.path.join('/usr/local/aotuConfig/config_auto_ui.yaml')
    f = open(path)
    s = yaml.load(f)
    f.close()
    return s
    ```
- 启动auto_ui, 允许外网访问
    ```
    python manage.py runserver 0.0.0.0:8000
    ```

#### 如何对接appium或者接口测试结果报告
- 先来看看数据库的字段, 只要在每条用例跑完后将对应字段结果入库即可，
需注意是ReportDetail和ReportInfo为uuid关联，每次运行跑脚本需要生成一个全局的uuid
  ```
  global uuid
  uuid = uuid.uuid1()  # 生成全局唯一id
  ```
  ```
    # ReportDetail 对应字段
    precondition = models.CharField("前置条件", max_length=255, default=None)
    case_name = models.CharField("case名称", max_length=128, default=None)
    check_step = models.CharField("检查步骤", max_length=128, default=None)
    title = models.CharField("用例标题", max_length=64, default=None)
    step = models.TextField("测试步骤", max_length=2048, default=None)
    phone_name = models.CharField("机型", max_length=64, default=None)
    result = models.ImageField("测试结果", default=0)
    screenshots_path = models.ImageField("测试图片，传入图片路径即可", upload_to='upload', default=None)
    msg = models.TextField("失败原因", max_length=1024, default=None)
    case_id = models.CharField("case_id", max_length=64, default=None)
    report_uuid = models.CharField("每次运行唯一md5标识", max_length=256, default=None)
    report_create_time = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)
    report_update_time = models.DateTimeField("更新时间", auto_now=True, auto_now_add=False)
    platform_name = models.TextField("系统类型", max_length=16, default="android")
    case_step_time = models.TextField("测试步长，json格式", max_length=2048, default=None)
  ```
  ```
    # ReportInfo 对应字段
    case_sum = models.IntegerField("case总和", default=0)
    case_pass_sum = models.IntegerField("通过case总和", default=0)
    case_fail_sum = models.IntegerField("失败case总和",  default=0)
    case_date = models.DateTimeField("测试日期", auto_now=False, auto_now_add=True)
    case_run_time = models.CharField("测试总耗时", max_length=64, default="0")
    platform_name = models.TextField("系统类型", max_length=16, default="android")
    platform_env = models.TextField("运行环境", max_length=16, default="stage")
    report_uuid = models.CharField("每次运行唯一md5标识", max_length=256, default=None)
    report_info_create_time = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)
    report_info_update_time = models.DateTimeField("更新时间", auto_now=True, auto_now_add=False)
  ```
#### 功能
- 所有的自动化统计报表，囊括所有的脚本运行的历史数据和进7天的脚本成功率趋势
![image](https://github.com/testerSunshine/aotu_ui/blob/master/uml/所有的自动化统计报表.jpg)
- 单次自动化统计报表，统计了单词运行脚本的详细信息，分为失败统计和全部统计和日志复盘信息
![image](https://github.com/testerSunshine/aotu_ui/blob/master/uml/单次自动化统计报表.jpg)
- 单条自动化统计报表，单条用例的详细信息，包括检查点，执行步骤，
![image](https://github.com/testerSunshine/aotu_ui/blob/master/uml/单条自动化统计报表.jpg)