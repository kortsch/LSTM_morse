# открываем текстовый файл
f = open('bigtext.txt', "r", encoding="utf-8")
# закидываем его содержимое в переменную
text = f.read()
# выводим начало, чтобы убедиться, что всё считалось правильно
print(text[:300])



# переводим символы в нижний регистр, чтобы всё было одинаково
text = text.lower()
# подключаем встроенный модуль работы со строками
import string
# добавляем к стандартным знакам пунктуации кавычки и многоточие
spec_chars = string.punctuation + '«»\t—…’ '
# очищаем текст от знаков препинания
text = "".join([ch for ch in text if ch not in spec_chars])
# подключаем регулярные выражения
import re
# меняем переносы строк на пробелы
text = re.sub('\n', ' ', text)
# убираем из текста цифры
text = "".join([ch for ch in text if ch not in string.digits])
text = "".join([ch for ch in text if ch not in string.ascii_lowercase])
# смотрим на результат
print(text[:300])

# из библиотеки обработки текста подключаем модуль для токенизации слов
from nltk import word_tokenize
# токенизируем текст
text_tokens = word_tokenize(text, language='russian')
# подключаем библиотеку для работы с текстом
# import nltk
# # переводим токены в текстовый формат
# text = nltk.Text(text_tokens)
# # подключаем статистику
# from nltk.probability import FreqDist
# # и считаем слова в тексте по популярности
# fdist = FreqDist(text)
# # выводим первые 5 популярных слов
# print(fdist.most_common(5))


# подключаем модуль со стоп-словами
from nltk.corpus import stopwords
# добавляем русские и французские стоп-слова
russian_stopwords = stopwords.words("russian")
russian_stopwords += stopwords.words("french")
# перестраиваем токены, не учитывая стоп-слова
text_tokens = [token.strip() for token in text_tokens if token not in russian_stopwords]
# снова приводим токены к текстовому виду
text = nltk.Text(text_tokens)
# считаем заново частоту слов
fdist_sw = FreqDist(text)
# показываем самые популярные
print(fdist_sw.most_common(10))






