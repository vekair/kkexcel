pip相关的包

scorpiotool: excel的生成工具

#上传方式
pip install wheel # 安装wheel模块

python setup.py sdist  # 源码包
python setup.py bdist_wheel --universal # 打包为无需build的wheel。其中--universal表示py2和py3通用的pure python模块。不满足通用或pure条件的模块不需加此参数

上传项目
先在pypi注册一个账户：https://pypi.org/account/register/

然后安装上传所需模块：

pip install twine

最后上传：

twine upload dist/*