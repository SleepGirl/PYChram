# coding =utf-8
import re
print(re.search('www', 'www.w3cschool.cn').span())


def count_price():
    logistics = 160  # 门到门国际物流费
    volume1 = 0.0609  # 商品的箱体积
    package_num = 6  # 每箱的双数（外包装体积）
    price = 123  # 企发售价
    tariff = 0.34  # 进口关税，与清关面料编码相关
    rate = 0.12  # 加价率，根据当前商品品牌和面料的真皮非真皮 得到的值
    addRate = 0.18  # 增值税率 根据商品是童鞋或者成人鞋
    dollarToRmb = 6.7   # 美元对人民币的汇率
    eurToDollar = 1.17  # 欧元对美元的汇率
    dallasToRu = 62  # 美元对人民币的汇率
    sells = (price/dollarToRmb+logistics*volume1/package_num+tariff*eurToDollar)/(1-rate)*(1+addRate)
    sallie = sells * dallasToRu  # 将根据公式计算得到的企发售价得出卢布价格
    return round(sallie)  # 将计算出的企发售价四舍五入

a = count_price()
print("企发售价是："+str(a))
