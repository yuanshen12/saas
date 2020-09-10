# 正常测试用例
success_data = [{"name": "正常登陆用例", "username": "1562662129@qq.com", "password": "admin123456"}]

# 账号异常场景
error_username_data = [
    {"name": "账号错误", "username": "error", "password": "admin123456", "errorMsg": "邮箱/手机号格式不正确!"}
]

# 密码异常场景
error_password_data = [
    {"name": "密码错误", "username": "13558252700", "password": "1234567890", "errorMsg": "用户名或密码错误"}
]

# 登录成功用例
success_login = {"name": "登录成功用例", "username": "1562662129@qq.com", "password": "admin123456"}