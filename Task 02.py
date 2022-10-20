# В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, 
# какое мороженное есть на складе. Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

goods_all = []
goods_warehouse = []

with open("Task_02.txt", "r", encoding="utf-8") as f:
    goods_all = set(f.readline().replace("\n","").split(", "))
    goods_warehouse = set(f.readline().replace("\n","").split(", "))

print(goods_all, " - весь ассортимент")
print(goods_warehouse," - есть на складе")
print(goods_all - goods_warehouse, " - закончился")
