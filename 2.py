def find_common_participants(pervaya_stroka, vtoraya_stroka, razdelitel=','):
    pervyi_spisok = pervaya_stroka.split(razdelitel)
    vtoroi_spisok = vtoraya_stroka.split(razdelitel)
    spisok1 = set(pervyi_spisok)
    spisok2 = set(vtoroi_spisok)
    obshie = spisok1.intersection(spisok2)
    itog = sorted(list(obshie))
    return itog

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print (find_common_participants(participants_first_group, participants_second_group))

