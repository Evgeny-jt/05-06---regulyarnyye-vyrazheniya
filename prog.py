from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


# TODO 1: выполните пункты 1-3 ДЗ
def fio_norm():
    fio = ' '.join(i[0:3])

    fio = fio.replace("  ", " ")
    if fio[-1] == " ":
        fio = fio[:-1]

    if fio[0] == " ":
        fio = fio[:0]

    # print("ФИО", fio)

    i.pop(0)
    i.pop(0)
    i.pop(0)

    if fio.count(' ') == 2:
        i.insert(0, fio.split()[2])
        i.insert(0, fio.split()[1])
        i.insert(0, fio.split()[0])
    elif fio.count(' ') == 1:
        # print('Вход ФИ')
        i.insert(0, '')
        i.insert(0, fio.split()[1])
        i.insert(0, fio.split()[0])
    else:
        print("ВНИМАНИЕ")


def phone_norm():
    if i[5] != '':
        pattern = re.compile(r'(\+7|8)\s?\(?\-?(\d\d\d)\)?\s?\-?(\d\d\d)\-?(\d\d)\-?(\d\d)\s?\(?(доб.)?\s?(\d+)?')
        subst_pattern = r'+7(\2)\3-\4-\5 \6\7'
        #
        result = pattern.sub(subst_pattern, i[5])
        i.pop(5)
        i.insert(5, result.replace(" ", ""))


def merge(contact_1, contact_2):
    merge_contacts = [contact_1[0], contact_1[1]]
    if contact_1[2] != '':
        merge_contacts.append(contact_1[2])
    else:
        merge_contacts.append(contact_2[2])
    if contact_1[3] != '':
        merge_contacts.append(contact_1[3])
    else:
        merge_contacts.append(contact_2[3])
    if contact_1[4] != '':
        merge_contacts.append(contact_1[4])
    else:
        merge_contacts.append(contact_2[4])
    if contact_1[5] != '':
        merge_contacts.append(contact_1[5])
    else:
        merge_contacts.append(contact_2[5])
    if contact_1[6] != '':
        merge_contacts.append(contact_1[6])
    else:
        merge_contacts.append(contact_2[6])
    return merge_contacts


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for n, i in enumerate(contacts_list):
    if n == 0:  # пропуск первой строки
        continue
    fio_norm()
    phone_norm()
for n, i in enumerate(contacts_list):
    print('end', n, '-', i)

new_contacts_list = []
contact_processed = []  # список повторных контактов
for n, i in enumerate(contacts_list):
    if n == 0:  # запись первой строки
        new_contacts_list.append(i)
        continue
    merge_contacts = []
    for m, j in enumerate(contacts_list):

        if m == 0:  # пропук первой строки
            continue
        if n > m:  # исключение повторнх проходов
            continue

        if contacts_list[n][0] == contacts_list[m][0] and n != m:  # поиск совподения по фамилии кромесобственной
            # print
            if contacts_list[n][1] == contacts_list[m][1]:  # поиск совподения по имени
                if contacts_list[n][2] == contacts_list[m][2]:
                    new_contacts_list.append(merge(contact_1=contacts_list[n], contact_2=contacts_list[m]))
                    contact_processed.append(n)
                    contact_processed.append(m)
                elif contacts_list[n][2] == '' or contacts_list[m][2] == '':
                    new_contacts_list.append(merge(contact_1=contacts_list[n], contact_2=contacts_list[m]))
                    contact_processed.append(n)
                    contact_processed.append(m)

        if m == len(contacts_list) - 1:  # зписываем уникальный контакт
            if n not in contact_processed:
                new_contacts_list.append(contacts_list[n])

print(new_contacts_list)
for n, i in enumerate(new_contacts_list):
    print(n, " - ", i)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contacts_list)


# with open("phonebook.csv", encoding="utf-8") as f:
#     rows = csv.reader(f, delimiter=",")
#     contacts_list = list(rows)
#
# for n, i in enumerate(contacts_list):
#     print(n, '---', i)

