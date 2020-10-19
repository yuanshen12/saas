# 登录地址
get_url = {"url": "http://192.168.0.156:8905/"}
# 登录用例
login_data = {"username": "13558252700", "password": "admin123456"}

# 系统管理 > 成员管理
mb = [{"add_user": "13527610362", "add_name": "李四"}]
# 系统管理 > 组织架构
ts = [{"add_name": "测试部", "add_b": "这是备注"}]
# 系统管理 > 角色管理
rl = [{"add": "测试", "add_1": "测试01", "add_2": "测试02", "add_3": "测试03"}]
# 系统管理 > 商品信息
sp = [{"add_name": "测试商品", "add_num": "10", "add_nums": "50", "add_1": "一级", "add_bq": "标签"}]

# 采购管理 > 申购
sg = [{"add_name": "申购商品", "add_num": "2"}]
# 采购管理 > 采购
cg = [{"add_name": "测试供应商", "add_names": "测试商品", "add_num": "2"}]
# 采购管理 > 询价
xj = [{"add_name": "测试供应商", "add_mc": "测试商品", "add_sl": "2"}]
# 采购管理 > 供应商信息
gy = [{"add_name": "新供应商"}]

# 库存管理 > 验收入库
ys = [{"add_num": "1"}]
# 库存管理 > 库存
rk = [{"add_name": "测试商品", "add_num": "2"}]
# 库存管理 > 盘点
pd = [{"add_name": "默认仓库"}]
# 库存管理 > 仓库
ck = [{"add_name": "本地测试仓库"}]