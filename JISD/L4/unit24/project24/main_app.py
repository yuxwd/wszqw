from flask import Flask, render_template, request, redirect
import pymongo

app = Flask(__name__)


# 增加用户
def user_insert(data):
    client = pymongo.MongoClient()
    db_ybc = client['ybc']
    c_user = db_ybc['user']
    c_user.insert_one(data)


# 查询用户
def user_find(data):
    client = pymongo.MongoClient()
    db_ybc = client['ybc']
    c_user = db_ybc['user']
    user_list = []
    users = c_user.find(data)
    for i in users:
        user_list.append(i)
    return user_list


# 路由：返回"a.html"页面
@app.route('/a')
def a():
    # 【提示2】输出一句话，比如“”："很多代码"
    00000
    # 【提示1】通过render_template方法返回"a.html"
    return '00000'


# 路由：重定向到"/a"
@app.route('/b')
def b():
    # 【提示1】重定向到"/a"
    return '00000'


# 路由：重定向到"/a"
@app.route('/c')
def c():
    # 【提示2】重定向到"/a"
    return '00000'


# 路由：重定向到外部地址
@app.route('/d')
def d():
    # 【提示3】重定向到外部地址："http://www.yuanfudao.com"
    return '00000'


# -------------------------- 注册 -----------------------------

# 路由：返回“注册表页面
@app.route('/register')
def register():
    return render_template('register.html')


# 路由：实现注册功能
@app.route('/register_check', methods=['POST'])
def register_check():
    username = request.form['username']
    pwd = request.form['pwd']
    result = user_find({'username': username})
    if result == []:
        # 【提示4】将账号和密码组装成一条字典数据，
        #         然后保存在变量user_data中
        00000
        # 【提示4】使用user_insert函数将user_data增加到数据库中
        00000
        # 【提示4】重定向到"/login"
        return '00000'
    else:
        return render_template('register.html', t_error='此账号已注册')


# -------------------------- 登录 -----------------------------

# 路由：返回“登录页面
@app.route('/login')
def login():
    return render_template('login.html')

# 路由：实现登录功能
@app.route('/login_check', methods=['POST'])
def login_check():
    username = request.form['username']
    pwd = request.form['pwd']
    result = user_find({'username': username, 'pwd': pwd})
    if result == []:
        return render_template('login.html', t_error='账号或密码错误')
    else:
        # 【提示5】重定向到"/main"
        return '00000'


# 路由：返回主页面
@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)


