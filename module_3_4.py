def single_root_words (root_word, *other_words):
    #Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
    same_words = []
    #Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    for a in other_words:
        #При помощи цикла for переберите предполагаемо подходящие слова.
        if root_word.lower() in a.lower() or a.lower() in root_word.lower():
            #Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
            same_words.append(a.lower())
            #Функция должна составить новый список same_words только из тех слов списка other_words, которые содержат root_word или наоборот root_word содержит одно из этих слов
    return same_words
    #После цикла верните образованный функцией список same_words.
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)