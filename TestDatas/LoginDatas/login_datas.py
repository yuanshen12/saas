# 正常测试用例
success_data = {"name": "正常登陆用例", "username": "13558252700", "password": "admin123456"}

# 账号异常场景
error_username_data = [
    {"name": "账号为空", "username": " ", "password": "admin123456"},
    {"name": "账号错误", "username": "error", "password": "admin123456"}
]

# 密码异常场景
error_password_data = [
    {"name": "密码为空", "username": "13558252700", "password": " "},
    {"name": "密码错误", "username": "13558252700", "password": "error"}
]