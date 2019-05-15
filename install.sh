# 默认安装包的清单
installation_list=('pandas' 'matplotlib' 'sklearn' 'lxml' 'tushare')
# 使用镜像的地址
mirror_url=https://mirrors.aliyun.com/pypi/simple/

if [ "$1" != "" ];then
  pip install $1 -i $mirror_url
else
  # 安装默认需要的包
  for i in ${installation_list[*]}
  do
    pip install $i -i $mirror_url
  done
fi