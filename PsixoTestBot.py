#Botu aşlışdırmadan öncə  D:\Bot\CavabList.txt faynını yaratdığınızdan əmin olun
import telebot
Mytoooken = "5606731286:AAFtm7Ulv90UNBX4H1u_0tY9l_Ml0a0UWsw"
#from telebot import TeleBot
MyBot = telebot.TeleBot(Mytoooken)
MyChatID = 633283743
print('Bot is online...')

Sual_1 = """1. Seher tezden yuxudan oyanmaq ucun ne edirsiz?
      A) hokmen zengli saat lazimdir
      B) ozum dururam
      C) seraitden asili olaraq oyana bilerem"""
Sual_2 = """2.Yemek sizin ucun ilk novbede ne demekdir?
      A) Istirahet ucun vaxt
      B) Sakitlesmek ucun imkan
      C) Yalniz qida ucun ayrilan zaman"""
Sual_3 = """3.Cox gezmeyi xoslayirsiniz?
      A) Beli
      B) Ehvalimdan asili olur
      C) Xeyr"""
Sual_4 = """4. Adeten kucede nece yeriyirsiniz?
      A) Qabaga baxaraq tez tez adimlayaraq
      B) Sakit ve telesmeden
      C) Ora bura baxaraq"""
Sual_5 = """5. Qol saatina munasibetiniz necedir?
      A) Onsuz hec yere getmerem
      B) Menim ucun onu taxmaq ferq etmez
      C) Qol saatindan xosum gelmir, taxmiram"""
Sual_6 = """6. Siz her gun axsam gezintisine cixmalisiniz?
      A) Beli
      B) Xeyr
      C) Ehvalimdan asili olur"""

@MyBot.message_handler(commands=['start'])
def SualList(message):
    FaylRead = open('D:\Bot\CavabList.txt', 'w+')
    MyBot.reply_to(message, 'Suallara bir-bir toxunub cavab variantını (A,B ya C) göndərin: \n\n/Sual_1\n\n/Sual_2\n\n/Sual_3\n\n/Sual_4\n\n/Sual_5\n\n/Sual_6\n\n/result')

@MyBot.message_handler(commands=['Sual_1'])
def CommandLine(message):
    MyBot.reply_to(message, Sual_1)
    @MyBot.message_handler(func=lambda m: True)
    def AnsCheck(message):
        #print(message.chat.id)
        Cavab = message.text
        Cavab1 = Cavab.upper()
        if Cavab1 == "A":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('1 ')
        if Cavab1 == "B":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('2 ')
        if Cavab1 == "C":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('3 ')

@MyBot.message_handler(commands=['Sual_2'])
def CommandLine(message):
    MyBot.reply_to(message, Sual_2)
    @MyBot.message_handler(func=lambda m: True)
    def AnsCheck(message):
        Cavab = message.text
        Cavab2 = Cavab.upper()
        if Cavab2 == "A":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('3 ')
        if Cavab2 == "B":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('2 ')
        if Cavab2 == "C":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('1 ')

@MyBot.message_handler(commands=['Sual_3'])
def CommandLine(message):
    MyBot.reply_to(message, Sual_3)
    @MyBot.message_handler(func=lambda m: True)
    def AnsCheck(message):
        Cavab = message.text
        Cavab1 = Cavab.upper()
        if Cavab1 == "A":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('2 ')
        if Cavab1 == "B":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('3 ')
        if Cavab1 == "C":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('1 ')

@MyBot.message_handler(commands=['Sual_4'])
def CommandLine(message):
    MyBot.reply_to(message, Sual_4)
    @MyBot.message_handler(func=lambda m: True)
    def AnsCheck(message):
        Cavab = message.text
        Cavab1 = Cavab.upper()
        if Cavab1 == "A":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('3 ')
        if Cavab1 == "B":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('1 ')
        if Cavab1 == "C":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('2 ')

@MyBot.message_handler(commands=['Sual_5'])
def CommandLine(message):
    MyBot.reply_to(message, Sual_5)
    @MyBot.message_handler(func=lambda m: True)
    def AnsCheck(message):
        Cavab = message.text
        Cavab1 = Cavab.upper()
        if Cavab1 == "A":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('3 ')
        if Cavab1 == "B":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('1 ')
        if Cavab1 == "C":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('2 ')

@MyBot.message_handler(commands=['Sual_6'])
def CommandLine(message):
    MyBot.reply_to(message, Sual_6)
    @MyBot.message_handler(func=lambda m: True)
    def AnsCheck(message):
        Cavab = message.text
        Cavab1 = Cavab.upper()
        if Cavab1 == "A":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('3 ')
        if Cavab1 == "B":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('1 ')
        if Cavab1 == "C":
            Fayl = open('D:\Bot\CavabList.txt', 'a')
            Fayl.write('2 ')
@MyBot.message_handler(commands=['result'])
def CommandLine(message):
    MyList = []  # File-den gelen datalarin listi
    MyList2 = []  # Ywkun list
    MyFile = open('D:\Bot\CavabList.txt', 'r')
    MyText = ''
    for i in MyFile:
        MyList.append(i)
    for i in MyList:
        MyText = str(i)  # List içindeki bötöv elemneti str edir
    # Yeni str data içindən boşluqrarı alır ve qalanı MyList2-ye verir
    for i in MyText:
        if i != " ":
            MyList2.append(int(i))
    print(sum(MyList2))
    print(message.chat.id)
    Result_1 = "Sizi seherler yalniz cox guclu sese malik saat zengi oyada biler!"
    Result_2 = "Siz cox celd ve enerjili adamsiniz!"
    Result_3 = "Siz cox celd ve aktiv adamsiniz!"
    SumMyList = sum(MyList2)
    if SumMyList <= 10:
        MyBot.reply_to(message, 'NƏTİCƏ:  {} '.format(Result_1))
    elif 10 < SumMyList < 15:
        MyBot.reply_to(message, 'NƏTİCƏ:  {} '.format(Result_2))
    elif SumMyList >= 15:
        MyBot.reply_to(message, 'NƏTİCƏ:  {} '.format(Result_3))
    MyBot.reply_to(message,'Siz {} bal topladınız! Testə yenidən başlamaq üçün /start göndərin'.format(sum(MyList2)))
    FaylRead = open('D:\Bot\CavabList.txt', 'w')
MyBot.polling()