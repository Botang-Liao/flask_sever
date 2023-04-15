from flask import Flask
from flask_login import LoginManager, UserMixin, login_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    # 在此函数中，通过 user_id 获取该用户的信息并返回一个 User 对象
    return User(user_id)

@app.route('/')
def index():
    # 模拟用户登录，此处应该使用表单验证等方式进行真实的用户登录
    user = User('1')
    login_user(user)
    return 'Logged in as: ' + current_user.id

if __name__ == '__main__':
    app.run()