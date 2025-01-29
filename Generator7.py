import winsound
import time
import math
import random
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import re

#import wavfile 


frequency = 1000     # частота воспроизводимой синусоиды
длительность_точки = 100 #мс = 100 периодов синусоиды
длительность_тире = 300  #мс = 300 периодов синусоиды 
длительность_паузы = 100 #мс 
длинная_пауза = 700  #мс
A=1  # Громкость

период=1/frequency    # период синусоиды Т=1/f = 1/1000 = 1мс

частота_дискретизации = 8000

mu = 0
sigma = 0.1

""" Значит на одном периоде синусойиды имее 8 отсчётов сигнала."""
N = int(частота_дискретизации/frequency)


print("Частота синусоиды:  ", frequency)
print("Частота дискретизации:  ", частота_дискретизации)
print("Число отсчётов на периоде:  ", N)
print("sigma: ", sigma)


# Отдискретизируем один период, чтобы потом из этих отсчётов собирать
# последовательность периодов
# Пусть частота дисткретизации кратна частоте синусиды
отсчёты_на_периоде = [A*math.cos(k*2*math.pi/N) for k in range(N)]


#print(отсчёты_на_периоде)
нули_на_периоде = [0 for k in range(N)]
#print(нули_на_периоде)

#Отсчёты на длительности точки - 100 периодов
sample_dot = []
for i in range(100): #повторяем периоды синусоиды
    sample_dot.extend(отсчёты_на_периоде)
#print(sample_dot)

#Отсчёты на длительности тире - 300 периодов
sample_dash = []
for i in range(300): #повторяем периоды синусоиды
    sample_dash.extend(отсчёты_на_периоде)
#print(sample_dash)

#Нулевые отсчёты на длительности точки 100 периодов - короткая пауза
sample_short_pause = []
for i in range(100): #повторяем периоды синусоиды
    sample_short_pause.extend(нули_на_периоде)
#print(sample_short_pause)

#Нулевые отсчёты на длительности точки 300 периодов - средняя пауза
sample_middle_pause = []
for i in range(300): #повторяем периоды синусоиды
    sample_middle_pause.extend(нули_на_периоде)
#print(sample_middle_pause)

#Нулевые отсчёты на длительности точки 700 периодов - длинная пауза
sample_long_pause = []
for i in range(700): #повторяем периоды синусоиды
    sample_long_pause.extend(нули_на_периоде)
#print(sample_long_pause)


rus_to_morse = {
                'а': '.-',
                'б': '-...',
                'в': '.--',
                'г': '--.',
                'д': '-..',
                'е': '.',
                'ж': '...-',
                'з': '--..',
                'и': '..',
                'й': '.---',
                'к': '-.-',
                'л': '.-..',
                'м': '--',
                'н': '-.',
                'о': '---',
                'п': '.--.',
                'р': '.-.',
                'с': '...',
                'т': '-',
                'у': '..-',
                'ф': '..-.',
                'х': '....',
                'ц': '-.-.',
                'ч': '---.',
                'ш': '----',
                'щ': '--.-',
                'ъ': '.--.-.',
                'ы': '-.--',
                'ь': '-..-',
                'э': '..-..',
                'ю': '..--',
                'я': '.-.-',
                ' ': ' '}


morse_to_rus = {'.-': 'а',
                '-...': 'б',
                '.--': 'в',
                '--.': 'г',
                '-..': 'д',
                '.': 'е',
                '...-': 'ж',
                '--..': 'з',
                '..': 'и',
                '.---': 'й',
                '-.-': 'к',
                '.-..': 'л',
                '--': 'м',
                '-.': 'н',
                '---': 'о',
                '.--.': 'п',
                '.-.': 'р',
                '...': 'с',
                '-': 'т',
                '..-': 'у',
                '..-.': 'ф',
                '....': 'х',
                '-.-.': 'ц',
                '---.': 'ч',
                '----': 'ш',
                '--.-': 'щ',
                '.--.-.': 'ъ',
                '-.--': 'ы',
                '-..-': 'ь',
                '..-..':'э',
                '..--': 'ю',
                '.-.-': 'я',
                ' ': ' ',
                }



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def Clean_stroke(content):
    result = []
    content = str(content).lower()

    for element in content:
        if (ord(element) >= 1072 and ord(element) <= 1103) or ord(element)==32:
            result.append(element)

    return result


def Russian_to_Morse(content):
    content = Clean_stroke(content)
    result = []
    for element in content:
        result.append(rus_to_morse[element])
    return result



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

flag_probel = False

def озвучить_букву(bukva):
    global flag_probel
    morse_bukva = rus_to_morse[bukva]
    #print(morse_bukva)
    if morse_bukva==' ':
        if flag_probel:
            samples_all.extend(sample_long_pause)
            flag_probel=True
        else:
            samples_all.extend(sample_short_pause)
            samples_all.extend(sample_short_pause)
            samples_all.extend(sample_short_pause)
            samples_all.extend(sample_short_pause)
            flag_probel=True
        #time.sleep(0.7)
    else:
        flag_probel = False
        for symbol in morse_bukva:
            if symbol == '.':
                samples_all.extend(sample_dot)
                #winsound.Beep(frequency, 100)
            elif symbol == '-':
                samples_all.extend(sample_dash)
                #winsound.Beep(frequency, 300)
            #time.sleep(0.1)
            samples_all.extend(sample_short_pause)
        samples_all.extend(sample_short_pause)
        samples_all.extend(sample_short_pause)
        #time.sleep(0.2)    


def озвучить_слово(слово):
    morse_slovo = Russian_to_Morse(слово)
    for bukva in morse_slovo:
        for symbol in bukva:
            if symbol == '.':
                samples_all.extend(sample_dot)
                #winsound.Beep(frequency, 100)
            elif symbol == '-':
                samples_all.extend(sample_dash)
                #winsound.Beep(frequency, 300)
                #time.sleep(0.1)
            samples_all.extend(sample_short_pause)
    #time.sleep(0.3)      
    samples_all.extend(sample_middle_pause)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
""" Генерация исходного текста для передачи """
#предложение = input("Введите русское предложение:")

letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я', ' ']
предложение = [letters[random.randint(0, len(letters)-1)] for k in range(0, 30)]
предложение = ''.join(предложение)
print('предложение - ', предложение)


""" Удаление из текста пробелов вначале и в конце """
предложение = предложение.strip()
print('предложение - ', предложение)

#предложение = "аа   бб вв"

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""  Сборка сигнала по словам.
  Предложение разбивается на слова. При этом пробелы между словами 
  теряются. Если между словами было несколько пробелов, то они теряются все.
  Поэтому исходный текст после восстановления может искажаться 
  потерей пробелов.

samples_all=[]
слова = предложение.split()
print(слова)
templist_source =[]
for слово in слова:
    morse_slovo = Russian_to_Morse(слово)
    templist_source.append(morse_slovo)
    print(morse_slovo)
    samples_all.extend(sample_long_pause) 
"""
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
""" Сборка сигнала по буквам. Здесь нет разбивки по словам. 
Поэтому все внутренние пробелы учитываются, даже если они 
идут понескольку подряд."""
samples_all=[]
templist_source =[]
for буква in предложение:
    morse_bukva = rus_to_morse[буква]
    templist_source.append(morse_bukva)
    озвучить_букву(буква)
print(templist_source)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for i in range(len(samples_all)):
    samples_all[i]+=random.gauss(mu, sigma)
    
#while len(samples_all) < 1200000:
#    samples_all.append(0)    


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
print('len(samples_all) = ', len(samples_all) )

t = [k/частота_дискретизации for k in range(len(samples_all))]
y = samples_all[0:len(samples_all)]
plt.plot(t,y)

#print('sa', samples_all)

#filepath= "C:/Users/Sozadmin/Desktop/telegraph/otschet1000.txt"

#f=open(filepath,"wt")
#for t in y:
#    f.write(str(t)+"\n")
#f.close()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Kolvo = len(samples_all)
#print("Число принятых отсчетов = ", Kolvo)
#filepath= "C:/Users/Sozadmin/Desktop/telegraph/samplestest.txt"

#f=open(filepath,"wt")
#for sample in samples_all:
#    f.write(str(sample)+"\n")
#f.close()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

CountFragment = Kolvo//800
# Демодулятор

over = []
tire_flag = False
probel_flag = False
tochka_flag = False
kp=0
for kk in range(CountFragment-1):  
    x = samples_all[0+kk*800:1600+kk*800] # Забрали фрагмент
    #plt.plot(x)
    # Формирует ЛФОП для точки L1
    sumeh=0
    for i in range(0, 800):
        sum = x[i]*math.cos(math.pi*i/4) 
        #print("sum",sum)
        sumeh = sumeh +sum
    #print( "Сумма для 800 = ", sumeh)
    L1 = A*sumeh/(sigma**2)-((A**2)*800)/(4*(sigma**2))
    #print ("L1 (Логарифм функционала отношения правдоподобия = ", L1)
       
    sumsh=0
    for i in range(0, 1600):
        sum = x[i]*math.cos(math.pi*i/4)
        #print("sum",sum)
        sumsh = sumsh +sum
    #print( "Сумма для 800 = ", sumsh)
    L2 = A*sumsh/(sigma**2)-((A**2)*1600)/(4*(sigma**2))
    #print ("L2 (Логарифм функционала отношения правдоподобия = ", L2)
    L3 = 0;
    #print ("L3 (Логарифм функционала отношения правдоподобия = ", L3)
      
    sumzh=0
    for i in range(800, 1600):
        #if i<816:
        #    print(i,x[i],math.cos(math.pi*i/4))
        sum = x[i]*math.cos(math.pi*i/4) 
        #print("sum",sum)
        sumzh = sumzh +sum
        #if i<832:
        #    print(sumzh)
    #print( "Сумма для 800 = ", sumeh)
    L4 = A*sumzh/(sigma**2)-((A**2)*800)/(4*(sigma**2))
    #print ("L4 (Логарифм функционала отношения правдоподобия = ", L4)
       
    #Сравниваем логарифмы для выдачи решения
    if (L2>L1) and (L2>L3) and (L2>L4):
        if tire_flag == True:
           over.extend ("-")
        else:
            tire_flag = True
    elif (L1>L2) and (L1>L3) and (L1>L4):
        if tire_flag == True:
            tire_flag = False
        else:
            over.extend('.')    
    elif (L3>L1) and (L3>L2) and (L3>L4):
        #if probel_flag == True:
        ##    over.extend(' ')
        ##    probel_flag = False
        #else:
        #    probel_flag = True
        kp = kp + 1
        if kp==6:    # если нам встретился пробел
            over.extend('!')
            over.extend(' ')
        if kp==7:    # если еже начался следующий пробел
            kp=0
    else:  # L4 самый большой. Это значит  началась следующя точка или тире
        if kp>=2:  # Если перед ней был пробел 300мс, то это граница между буквами
            over.extend('!') # Это разделитель между буквами
        kp=0

#print('Список принятых точек и тире', over)
print(over)
over_str = "".join(over).rstrip()
print("Собраны в строку ", over_str)

over_str_bukvy = over_str.split("!")
print("Строка разбита по буквам ", over_str_bukvy)

templist = []
for b in over_str_bukvy:
    templist.append(morse_to_rus[b])

print(templist)
выход_декодера = ''.join(templist)

print("Передаваемые исходники ", templist_source)
print('-'*70)
print(предложение)
print(выход_декодера)


""" Спавним строки посимвольно """
L1 = len(предложение)
L2 = len(выход_декодера)
k_err = abs(L1-L2)
for i in range(min(L1,L2)):
    if предложение[i] != выход_декодера[i]:
        k_err += 1

print("Количество ошибок: ", k_err)


plt.show()



