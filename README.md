## 前端运行方式
- 进入shanxi_frontend目录输入以下命令
> npm i  
> npm run dev

## 后端运行方式
- 进入shanxi_backend目录输入以下命令
> python manage.py runserver

## pycharm运行配置
- 前端配置：
    0. **确保运行配置前已经在shanxi_frontend目录下运行过npm i或npm install**
    1. 编辑配置
    2. 左上角+号
    3. 选择npm
    4. 填写配置
        - npm: npm
        - package.json: shanxi_frontend/package.json
        - 命令(command): run
        - 脚本(script): dev
    5. 保存
- 后端配置：
    1. 编辑配置
    2. 左上角+号
    3. 选择Python
    4. 填写配置
        - Python解释器(Python interpreter): python3.9(安装了Django的虚拟环境)
        - 脚本路径(Script path): shanxi_backend/manage.py
        - 形参(Parameters): runserver
        - 工作目录(Working directory): shanxi_backend
    5. 保存

## 开发流程
### 开发前：
1. 新建issue并进行任务分配
### 开发：
1. 切换到本地master分支，删除上一次开发分支 
```
    git checkout master
    git branch -D 你的分支名
```
2、拉取远端master分支
```
    git pull origin master
```
3、建立并切换到自己的分支
```
    git checkout -b 你的名字缩写_issue#序号
```
4、提交并上传代码
```
    git add .
    git commit -m "Add:your message. Ref #序号 "
    git pull --rebase origin master
    git push origin 你的分支名
```
5、自行开发

6、发起merge request
- Titles格式规范与commit message保持一致。
- Description基本格式：
    - Closes #你的issueID

## 常见问题总结
### 前端:
1. npm install报错
    - 方法1：删除node_modules文件夹，重新执行npm install
    - 方法2：检查npm镜像源, 设置成淘宝镜像源
        > npm config set registry https://registry.npm.taobao.org
    - 方法3：重新安装nodejs, 统一使用v16.16.0
2. nvm use报错
    > exit status 1: XXXXX(乱码)
    - 方法: 使用管理员运行cmd
3. npm run serve报错
    - 原因: 项目使用的是webpack, 需要用npm run dev
4. 出现 npm WARN 配置全局'–global'， '–local' 已弃用。使用“–location=global”代替。
    - > npm warn config global `--global`, `--local` are deprecated. use `--location=global` instead.
    - 原因: nodejsv16.16.0版本的问题
    - 方法: 进入nodejs文件夹，将npm和npm.cmd中的prefix -g替换为prefix --location=global

### 后端:
1. 运行manage.py时报错(django1.11.2, 现已改为4.1.2)
    1. 报错内容为TypeError: unsupported operand type(s) for /: ‘str’ and ‘str’
        - 原因: 这是由于自动生成的代码中存在语法错误（在settings.py中的错误代码为 'DIRS': [BASE_DIR / 'templates']） 
        - 解决方法: 在settings.py中修改:
        > 'DIRS': [str.format(BASE_DIR, '/templates')]
    2. 报错内容为
        > File "D:\dev\python\Python38\lib\site-packages\django\contrib\admin\options.py", line 12, in <module>from django.contrib.admin import helpers, widgets
        SyntaxError: Generator expression must be parenthesized (widgets.py, line 151)
        - 原因: 这是由于django1.11.2版本的问题
        - 解决方法: 进入django安装目录, 将site-packages\django\contrib\admin中的widgets.py文件中的第151行代码末尾的逗号去掉
