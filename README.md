# Что это
Рандомная перемешивалка людей между группами с возможностью прибивания отдельных членов групп к этим группам навсегда.

# Как пользоваться
python3 ./order.py <filename> <size>

<filename> - имя такстового файла с группами
<size> - целевой размер одной группы

# Формат <filename>
```
group 0
Иванов Карл Колюневич
=Собака Изергилевич
Мойша Никодимович Оленяев

group 100
Школотронов Люгер Викторович
=Ололоев Пётруша

group 200
Вася Васильев
Иван Алмазов
Вика Изумрудова
```

group N - отделяет одну группу от другой. Номер N не важен и не учитывается, но группы считаются по порядку. Программа понимает вышеприведённые группы как 0, 1, 2.

Строка, начинающаяся со знака равно `=` будет прибита к этой по счёту группе. В примере выше "Собака Изергилевич" будет всё время в группе 0.

