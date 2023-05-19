import ctypes
import random
import shutil
import sys, os
import json
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtMultimedia import QSound

from Form_n import Ui_MainWindow

class EngineRotor:
    def __init__(self):
        self.module = 33
        self.Rusrotors = [0, 0, 0]
        self.Engrotors = [0, 0, 0]

    def setRotor(self, mode, index, rotorF, rotorB):
        if mode == 0:
            self.Rusrotors[index] = [(ctypes.c_int*33)(*rotorF), (ctypes.c_int*33)(*rotorB)]
        elif mode == 1:
            self.Engrotors[index] = [(ctypes.c_int*26)(*rotorF), (ctypes.c_int*26)(*rotorB)]
    
    def createRotor(self, mode=0):
        if mode == 0:
            shake = []
            alphaNum = list([x for x in range(33)])

            for _ in range(33):
                ind = random.randint(0, len(alphaNum)-1)
                let = alphaNum[ind]
                alphaNum.pop(ind)
                shake.append(let)
            forward = shake
            
            reverse = list([0 for _ in range(33)])
            for ind in range(0, len(shake)):
                reverse[shake[ind]] = ind

            return tuple(forward), tuple(reverse)
        elif mode == 1:
            shake = []
            alphaNum = list([x for x in range(26)])

            for _ in range(26):
                ind = random.randint(0, len(alphaNum)-1)
                let = alphaNum[ind]
                alphaNum.pop(ind)
                shake.append(let)
            forward = shake
            
            reverse = list([0 for _ in range(26)])
            for ind in range(0, len(shake)):
                reverse[shake[ind]] = ind

            return tuple(forward), tuple(reverse)

class EnigmaEngine:
    def __init__(self):
        self.RUSLANG = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self.ENGLANG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.RusCount = [0, 0, 0] # I II III
        self.EngCount = [0, 0, 0] # I II III

        self.RotorManager = EngineRotor()
        self.RotorManager.setRotor(0, 0, (1, 22, 7, 15, 29, 19, 11, 0, 13, 27, 31, 26, 20, 2, 28, 25, 8, 30, 24, 10, 5, 21, 3, 17, 23, 4, 6, 18, 14, 12, 16, 9, 32), (7, 0, 13, 22, 25, 20, 26, 2, 16, 31, 19, 6, 29, 8, 28, 3, 30, 23, 27, 5, 12, 21, 1, 24, 18, 15, 11, 9, 14, 4, 17, 10, 32))
        self.RotorManager.setRotor(0, 1, (10, 27, 21, 4, 16, 2, 22, 15, 9, 14, 20, 1, 5, 32, 23, 31, 28, 29, 17, 30, 3, 19, 7, 26, 12, 11, 8, 0, 24, 25, 6, 18, 13), (27, 11, 5, 20, 3, 12, 30, 22, 26, 8, 0, 25, 24, 32, 9, 7, 4, 18, 31, 21, 10, 2, 6, 14, 28, 29, 23, 1, 16, 17, 19, 15, 13))
        self.RotorManager.setRotor(0, 2, (20, 6, 23, 4, 2, 26, 10, 25, 9, 15, 21, 13, 3, 1, 22, 16, 32, 19, 18, 29, 0, 8, 30, 24, 14, 28, 27, 17, 5, 31, 11, 12, 7), (20, 13, 4, 12, 3, 28, 1, 32, 21, 8, 6, 30, 31, 11, 24, 9, 15, 27, 18, 17, 0, 10, 14, 2, 23, 7, 5, 26, 25, 19, 22, 29, 16))
        self.RotorManager.setRotor(1, 0, (11, 10, 8, 15, 2, 18, 12, 4, 1, 7, 20, 3, 22, 14, 0, 16, 21, 13, 5, 17, 6, 9, 23, 19, 25, 24), (14, 8, 4, 11, 7, 18, 20, 9, 2, 21, 1, 0, 6, 17, 13, 3, 15, 19, 5, 23, 10, 16, 12, 22, 25, 24))
        self.RotorManager.setRotor(1, 1, (11, 10, 21, 2, 16, 6, 12, 15, 1, 17, 24, 18, 9, 8, 19, 0, 5, 13, 3, 4, 22, 25, 20, 7, 14, 23), (15, 8, 3, 18, 19, 16, 5, 23, 13, 12, 1, 0, 6, 17, 24, 7, 4, 9, 11, 14, 22, 2, 20, 25, 10, 21))
        self.RotorManager.setRotor(1, 2, (3, 1, 13, 18, 12, 16, 8, 22, 4, 0, 11, 7, 6, 21, 17, 14, 2, 24, 15, 20, 25, 19, 9, 5, 10, 23), (9, 1, 16, 0, 8, 23, 12, 11, 6, 22, 24, 10, 4, 2, 15, 18, 5, 14, 3, 21, 19, 13, 7, 25, 17, 20))

        RusReflector = (32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
        RusReflectorArray = (ctypes.c_int*33)(*RusReflector)
        EngReflector = (25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
        EngReflectorArray = (ctypes.c_int*26)(*EngReflector)

        dll = ctypes.CDLL("./EngimaDefault.dll")
        #dll = ctypes.CDLL("./VSDll/AddDllPy/x64/Release/AddDllPy.dll")
        dll.set_rus_reflector(RusReflectorArray)
        dll.set_eng_reflector(EngReflectorArray)

        self.Dll = dll

        self.setRotorsCopy()

    def setRotorsCopy(self):
        self.Dll.set_rus_rotor(self.RotorManager.Rusrotors[0][0], 1, 0)
        self.Dll.set_rus_rotor(self.RotorManager.Rusrotors[0][1], 1, 1)
        self.Dll.set_rus_rotor(self.RotorManager.Rusrotors[1][0], 2, 0)
        self.Dll.set_rus_rotor(self.RotorManager.Rusrotors[1][1], 2, 1)
        self.Dll.set_rus_rotor(self.RotorManager.Rusrotors[2][0], 3, 0)
        self.Dll.set_rus_rotor(self.RotorManager.Rusrotors[2][1], 3, 1)
        self.Dll.set_eng_rotor(self.RotorManager.Engrotors[0][0], 1, 0)
        self.Dll.set_eng_rotor(self.RotorManager.Engrotors[0][1], 1, 1)
        self.Dll.set_eng_rotor(self.RotorManager.Engrotors[1][0], 2, 0)
        self.Dll.set_eng_rotor(self.RotorManager.Engrotors[1][1], 2, 1)
        self.Dll.set_eng_rotor(self.RotorManager.Engrotors[2][0], 3, 0)
        self.Dll.set_eng_rotor(self.RotorManager.Engrotors[2][1], 3, 1)

    def EncryptAlphaRus(self, letter):
        letter = letter.upper()
        AlphaId = self.RUSLANG.find(letter)
        AnwserId = self.Dll.encryptRus(AlphaId, self.RusCount[2], self.RusCount[1], self.RusCount[0])
        
        if self.RusCount[2] + 1 >= 33:
            self.RusCount[2] = 0
            if self.RusCount[1] + 1 >= 33:
                self.RusCount[1] = 0
                if self.RusCount[0] + 1 >= 33:
                    self.RusCount[0] = 0
                    self.RusCount[1] = 0
                    self.RusCount[2] = 0
                else:
                    self.RusCount[0] += 1
            else:
                self.RusCount[1] += 1
        else:
            self.RusCount[2] += 1

        return self.RUSLANG[AnwserId]
    
    def EncryptAlphaEng(self, letter):
        letter = letter.upper()
        AlphaId = self.ENGLANG.find(letter)
        AnwserId = self.Dll.encryptEng(AlphaId, self.EngCount[2], self.EngCount[1], self.EngCount[0])
        if self.EngCount[2] + 1 >= 26:
            self.EngCount[2] = 0
            if self.EngCount[1] + 1 >= 26:
                self.EngCount[1] = 0
                if self.EngCount[0] + 1 >= 26:
                    self.EngCount[0] = 0
                    self.EngCount[1] = 0
                    self.EngCount[2] = 0
                else:
                    self.EngCount[0] += 1
            else:
                self.EngCount[1] += 1
        else:
            self.EngCount[2] += 1
        return self.ENGLANG[AnwserId]

    def EncryptWord(self, lang, word):
        word = list(word.upper())
        anwser = ""
        if lang == "RUS":
            for letter in word:
                if letter in self.RUSLANG:
                    anwser += self.EncryptAlphaRus(letter)
                else:
                    anwser += letter
        elif lang == "ENG":
            for letter in word:
                if letter in self.ENGLANG:
                    anwser += self.EncryptAlphaEng(letter)
                else:
                    anwser += letter
        return anwser
    
    def EnglandDecrypt(self, INPUT, OUTPUT):
        GoodRotors = []
        TempEng = list([x for x in self.EngCount])
        for Rfirst in range(len(self.ENGLANG)):
            for Rsecond in range(len(self.ENGLANG)):
                for Rthird in range(len(self.ENGLANG)):
                    Rotor = [Rthird, Rsecond, Rfirst]
                    self.EngCount = Rotor
                    Start = len(INPUT)
                    for index_alpha, input_alpha in enumerate(INPUT):
                        encrypted = self.EncryptAlphaEng(input_alpha)
                        
                        if encrypted != OUTPUT[index_alpha]: 
                            break
                        else: Start -= 1

                    if Start <= 0: 
                        GoodRotors.append([Rthird, Rsecond, Rfirst])
        
        self.EngCount = list([x for x in TempEng])
        return GoodRotors
    
    def RussianDecrypt(self, INPUT, OUTPUT):
        GoodRotors = []
        TempRus = list([x for x in self.RusCount])
        for Rfirst in range(len(self.RUSLANG)):
            for Rsecond in range(len(self.RUSLANG)):
                for Rthird in range(len(self.RUSLANG)):
                    Rotor = [Rthird, Rsecond, Rfirst]
                    self.RusCount = Rotor
                    Start = len(INPUT)
                    for index_alpha, input_alpha in enumerate(INPUT):
                        encrypted = self.EncryptAlphaRus(input_alpha)
                        
                        if encrypted != OUTPUT[index_alpha]: 
                            break
                        else: Start -= 1

                    if Start <= 0: 
                        GoodRotors.append([Rthird, Rsecond, Rfirst])
        
        self.RusCount = list([x for x in TempRus])
        return GoodRotors


class EnigmaFile:
    def __init__(self, enigmadefault):
        self.Dll = ctypes.CDLL("./WorkWithFiles.dll")
        self.enigmadefault = enigmadefault
        self.rotors = [0, 0, 0]
    
    def EncryptFile(self, filename, every):
        with open(filename, "rb") as file:
            FileBytes = list(file.read())

        ToWrite, Rotors = self.EncryptWrittenBytes(FileBytes, every)

        zas = (filename.split("."))[-1]
        file = ".".join(filename.split(".")[x] for x in range(0, len(filename.split("."))-1))

        with open(file+"_eg."+zas, "wb") as file:
            file.write(bytes(ToWrite))

    def EncryptWrittenBytes(self, Abytes, every):
        Abytes = (ctypes.c_int*len(Abytes))(*Abytes)
        RotorsValue = (ctypes.c_int*3)(*reversed(self.rotors))   
        self.Dll.EncryptValues(Abytes, len(Abytes), RotorsValue, every)
        return list(Abytes), list(reversed(list(RotorsValue)))
    
    def EncryptFileSecond(self, filename, is_copy):
        try:
            if is_copy[0]:
                toWho = is_copy[1].split(".")[-1]
                shutil.copyfile(is_copy[1], is_copy[1]+"-copy."+toWho)
            #ctypes.c_char_p(filename.encode("utf-8"))
            self.Dll.EncryptFile(ctypes.c_char_p(filename.encode("cp866")), (ctypes.c_int*3)(*reversed(self.rotors)), 1)
        except Exception as exp:
            print(exp)

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #CPP Dll для энигмы
        self.EnigmaDefault = EnigmaEngine()
        self.EnigmaFileWork = EnigmaFile(self.EnigmaDefault)

        #Доп переменные
        self.LoadSounds()
        self.NormalPath = ""
        self.LastFilePath = ""
        self.NormalFilesArray = []
        self.FilesArrayToCrypt = []
        self.SwitchingPanelBool = False
        self.SwitchLetters = {}
        self.CryptIs = 0
        self.TimeCrypt = 0
        self.lastShowedAlpha = [0, 0]
        self.TempFilesEnigmaPath = "C:/ProgramData/AstroEnigma/"
    
        if not(os.path.exists(self.TempFilesEnigmaPath)):
            os.mkdir(self.TempFilesEnigmaPath)
    
        #Подключение кнопок
        self.ui.pushButton_13.clicked.connect(self.DeleteLastSymbol)
        self.ui.pushButton_24.clicked.connect(self.SetEnigmaSettings)
        self.ui.pushButton_33.clicked.connect(self.BigSetEnigmaFile)
        self.ui.pushButton_34.clicked.connect(self.EncryptingWord)
        self.ui.pushButton_35.clicked.connect(self.TurnSwitchingPanel)
        self.ui.pushButton_36.clicked.connect(self.ResetSwitchingPanel)
        self.ui.pushButton_37.clicked.connect(self.SaveConfigFile)
        self.ui.pushButton_38.clicked.connect(self.LoadConfigFile)
        self.ui.pushButton_39.clicked.connect(self.TakePathFFile)
        self.ui.pushButton_40.clicked.connect(self.BreakEnigma)
        self.ui.pushButton_45.clicked.connect(self.findRotorForText)

        #Текстовые поля        
        self.ui.plainTextEdit_2.setPlaceholderText("Здесь будет результат")
        self.ui.plainTextEdit_5.setPlaceholderText("Введите текст, что хотите зашифровать")
        self.ui.plainTextEdit_6.setPlaceholderText("Здесь будет результат")
        self.ui.plainTextEdit_5.textChanged.connect(self.PreEncryptingWord)

        #Таблицы
        self.ui.tableWidget.cellClicked.connect(self.UseEnigmaFunctionWithAlpha)
        self.ui.tableWidget_3.dropEvent = self.dropEvent

    def findRotorForText(self):
        lang = self.ui.comboBox_2.currentText()
        text_encrypted = self.ui.plainTextEdit_8.toPlainText()
        text_source = self.ui.plainTextEdit_7.toPlainText()
        Text = self.ui.plainTextEdit_9.toPlainText()
        LANG = self.EnigmaDefault.RUSLANG if lang == "RUS" else self.EnigmaDefault.ENGLANG
        Text = "".join([x for x in Text if x in LANG])
        if text_encrypted is None or text_source is None or Text is None: return
        
    
        items = [self.ui.listWidget.item(x).text() for x in range(self.ui.listWidget.count())]
        self.ui.listWidget.clear()
        for package in items:
            Rotor = list(map(lambda x: int(x.replace("[","").replace("]","")), package.split(";")[0].split(",")))
            StartRotor = list([x for x in Rotor])
            if not(text_encrypted in Text): 
                print(f"{text_encrypted=} wasn't found")
                continue
            start_pos = Text.find(text_encrypted)

            if lang == "RUS": module = 33
            elif lang == "ENG": module = 26
        
            Rotor[0] = Rotor[0] - start_pos
            Rotor[1] = (Rotor[1]) - abs(Rotor[0] // module)
            Rotor[2] = (Rotor[2]) - abs(Rotor[1] // (module * module))

            Rotor[0] %= module
            Rotor[1] %= module
            Rotor[2] %= module

            self.ui.listWidget.addItem(f"{Rotor[0]}, {Rotor[1]}, {Rotor[2]}; if {StartRotor}")

    def BreakEnigma(self):
        lang = self.ui.comboBox_2.currentText()
        input_ = self.ui.plainTextEdit_7.toPlainText()
        output_ = self.ui.plainTextEdit_8.toPlainText()
        rotors = []

        if lang == "RUS":
            rotors = self.EnigmaDefault.RussianDecrypt(input_, output_)
        elif lang == "ENG":
            rotors = self.EnigmaDefault.EnglandDecrypt(input_, output_)

        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(list([f"[{x[2]}, {x[1]}, {x[0]}]; {input_} -> {output_}" for x in rotors]))

    def BigSetEnigmaFile(self):
        self.EncryptDirectory()

    def EncryptDirectory(self):
        try:
            self.EnigmaFileWork.rotors[2] = self.ui.spinBox_5.value()
            self.EnigmaFileWork.rotors[1] = self.ui.spinBox_7.value()
            self.EnigmaFileWork.rotors[0] = self.ui.spinBox_6.value()
            IsCopy = self.ui.checkBox_2.isChecked()
            
            for Id, file in enumerate(self.FilesArrayToCrypt):
                self.EnigmaFileWork.EncryptFileSecond(file, [IsCopy, self.NormalFilesArray[Id]])
                shutil.copyfile(file, self.NormalFilesArray[Id])
                os.remove(file)
                self.ui.label_21.setText("Статус: "+str(self.NormalFilesArray[Id])+" завершён!")
        except Exception as exp:
            print(exp)

    def LoadConfigFile(self):
        try:
            path = (QtWidgets.QFileDialog.getOpenFileName(None, 'Выберите файл конфига:'))[0]
            with open(path, "r", encoding="utf-16") as read_file:
                data = json.load(read_file)

            self.EnigmaDefault.RusCount = data['rotorsRus']
            self.EnigmaDefault.EngCount = data['rotorsEng']
            tempSwitchLetters = data['switchPanel']
            self.SwitchLetters = data['switchPanel']

            abc = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" if "RUS" in (self.ui.comboBox.currentText()).upper() else "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            if "RUS" in (self.ui.comboBox.currentText()).upper():
                self.ui.spinBox_3.setValue(int(self.EnigmaDefault.RusCount[0]))
                self.ui.spinBox_2.setValue(int(self.EnigmaDefault.RusCount[1]))
                self.ui.spinBox.setValue(int(self.EnigmaDefault.RusCount[2]))
            elif "ENG" in (self.ui.comboBox.currentText()).upper():
                self.ui.spinBox_3.setValue(int(self.EnigmaDefault.EngCount[0]))
                self.ui.spinBox_2.setValue(int(self.EnigmaDefault.EngCount[1]))
                self.ui.spinBox.setValue(int(self.EnigmaDefault.EngCount[2]))
            
            for letter in abc:
                if letter in self.SwitchLetters:
                    string = letter + "-" + self.SwitchLetters[letter]
                    position = abc.find(letter)
                    row = position // 9
                    column = position % 9
                    self.ui.tableWidget_3.setItem(row, column, QtWidgets.QTableWidgetItem(string))
                else:
                    position = abc.find(letter)
                    row = position // 9
                    column = position % 9
                    self.ui.tableWidget_3.setItem(row, column, QtWidgets.QTableWidgetItem(letter))
            
            for n in range(len(abc), 36):
                self.ui.tableWidget_3.setItem(n//9, n%9, QtWidgets.QTableWidgetItem("-"))
            

        except Exception as exp:
            print(exp)

    def SaveConfigFile(self):
        try:
            path = (QtWidgets.QFileDialog.getSaveFileName(None, 'Выберите файл для конфига:'))[0]
            data = {
                "rotorsRus": self.EnigmaDefault.RusCount,
                "rotorsEng": self.EnigmaDefault.EngCount,
                "switchPanel": self.SwitchLetters,
            }
            with open(path, "w", encoding="utf-16") as write_file:
                json.dump(data, write_file, ensure_ascii=False)
        except Exception as exp:
            print(exp)

    def EncryptFile(self): 
        try:
            self.EnigmaFileWork.rotors[2] = self.ui.spinBox_5.value()
            self.EnigmaFileWork.rotors[1] = self.ui.spinBox_7.value()
            self.EnigmaFileWork.rotors[0] = self.ui.spinBox_6.value()
            IsCopy = self.ui.checkBox_2.isChecked()
            if self.LastFilePath == "":
                print(f"{self.LastFilePath=}")
                return 
            self.EnigmaFileWork.EncryptFileSecond(self.LastFilePath, [IsCopy, self.NormalPath])
            shutil.copyfile(self.LastFilePath, self.NormalPath)
            os.remove(self.LastFilePath)
            self.ui.label_21.setText("Статус: "+str(self.NormalPath)+" завершён!")
        except Exception as exp:
            print(exp)

    def TakePathFFile(self):
        try:
            BigK = 30000000
            self.accept_button.play()
            self.FilesArrayToCrypt = QtWidgets.QFileDialog.getOpenFileNames()[0]
            self.FilesArrayToCrypt = list([x for x in self.FilesArrayToCrypt if os.path.isfile(x)])
            self.ui.label_16.setText(", ".join(list([x.split("/")[-1] for x in self.FilesArrayToCrypt])))
            sizeFile = 0
            for File in self.FilesArrayToCrypt:
                sizeFile += os.path.getsize(File)
            stringToMemory = ""
            if (sizeFile/1024) / 1024 >= 1024:
                stringToMemory = f"{round(((sizeFile)/1024) / 1024, 3)} ГБ"
            elif sizeFile/1024 >= 1024:
                stringToMemory = f"{round(((sizeFile)/1024)/1024, 3)} МБ"
            elif sizeFile > 1024:
                stringToMemory = f"{round((sizeFile)/1024, 3)} КБ"
            else:
                stringToMemory = f"{sizeFile} Байт"
                
            timetoCrypt = sizeFile/BigK 
            self.TimeCrypt = timetoCrypt
            if ((timetoCrypt / 60)) >= 1:
                self.ui.label_20.setText(str(round(timetoCrypt/60, 5))+" минут")
            elif (timetoCrypt * 1000) <= 10:
                self.ui.label_20.setText(str(round(timetoCrypt*1000, 5))+" милисекунд")
            else:
                self.ui.label_20.setText(str(round(timetoCrypt, 5))+" сек")

            self.ui.label_18.setText(stringToMemory)
            self.NormalFilesArray = self.FilesArrayToCrypt.copy()
            for Id in range(0, len(self.FilesArrayToCrypt)):
                pseudoName = ""
                for _ in range(10):
                    pseudoName+=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                self.FilesArrayToCrypt[Id] = self.TempFilesEnigmaPath+pseudoName+"."+((self.FilesArrayToCrypt[Id].split("/")[-1]).split(".")[-1])
                shutil.copyfile(self.NormalFilesArray[Id], self.FilesArrayToCrypt[Id])
            self.CryptIs = 1
        except Exception as exp:
            print(exp)

    def TakePathTFile(self):
        try:
            BigK = 30000000
            self.accept_button.play()
            self.path_to_file = QtWidgets.QFileDialog.getOpenFileName()[0]
            if self.path_to_file == " " or self.path_to_file == "":
                self.path_to_file = self.LastFilePath
            self.ui.label_16.setText(((self.path_to_file.split("/"))[-1]+" - "+"/".join((self.path_to_file.split("/"))[0:-1])))
            sizeFile = os.path.getsize(self.path_to_file)
            stringToMemory = ""
            if (sizeFile/1024) / 1024 >= 1024:
                stringToMemory = f"{round(((sizeFile)/1024) / 1024, 3)} ГБ"
            elif sizeFile/1024 >= 1024:
                stringToMemory = f"{round(((sizeFile)/1024)/1024, 3)} МБ"
            elif sizeFile > 1024:
                stringToMemory = f"{round((sizeFile)/1024, 3)} КБ"
            else:
                stringToMemory = f"{sizeFile} Байт"
            timetoCrypt = sizeFile/BigK 
            self.TimeCrypt = timetoCrypt
            if ((timetoCrypt / 60)) >= 1:
                self.ui.label_20.setText(str(round(timetoCrypt/60, 5))+" минут")
            elif (timetoCrypt * 1000) <= 10:
                self.ui.label_20.setText(str(round(timetoCrypt*1000, 5))+" милисекунд")
            else:
                self.ui.label_20.setText(str(round(timetoCrypt, 5))+" сек")

            self.ui.label_18.setText(stringToMemory)
            self.NormalPath = self.path_to_file
            pseudoName = ""
            for _ in range(10):
                pseudoName+=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            self.LastFilePath = self.TempFilesEnigmaPath+pseudoName+"."+((self.path_to_file.split("/")[-1]).split(".")[-1])
            shutil.copyfile(self.NormalPath, self.LastFilePath)
            self.CryptIs = 0
        except Exception as exp:
            print(exp)

    def ResetSwitchingPanel(self):
        try:
            self.SwitchLetters = {}
            lang = self.ui.comboBox.currentText()
            if "RUS" in lang:
                Lang = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ---"
            elif "ENG" in lang:
                Lang = "ABCDEFGHIJKLMNOPQRSTUVWXYZ----------"

            self.clicked_button.play()
            for x in range(0, 4):
                for y in range(0, 9):
                    self.ui.tableWidget_3.setItem(x, y ,QtWidgets.QTableWidgetItem(f"{Lang[9*x+y]}"))
        except Exception as exp:
            print(exp)

    def TurnSwitchingPanel(self):
        self.accept_button.play()
        self.SwitchingPanelBool = not(self.SwitchingPanelBool)
        if self.SwitchingPanelBool:
            self.ui.label_15.setStyleSheet(r'color: rgb(0, 255, 0); font: 28pt "Consolas";')
        else:
            self.ui.label_15.setStyleSheet(r'color: rgb(230, 230, 230); font: 28pt "Consolas";')

    def dropEvent(self, event):
        try:
            self.switchPanelOut.play()
            fromIndexRow = self.ui.tableWidget_3.currentRow()
            fromIndexColumn = self.ui.tableWidget_3.currentColumn()
            ix = self.ui.tableWidget_3.indexAt(event.pos())
            if ix.isValid():
                toIndexRow = ix.row()
                toIndexColumn = ix.column()
            else:
                return
            
            FromItem = (self.ui.tableWidget_3.item(fromIndexRow, fromIndexColumn)).text()
            ToItem = (self.ui.tableWidget_3.item(toIndexRow, toIndexColumn)).text()
            if FromItem == ToItem:
                print("Буква не может переходить в себя")
                return
            lang = self.ui.comboBox.currentText()
            if "RUS" in lang:
                Lang = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ---"
            elif "ENG" in lang:
                Lang = "ABCDEFGHIJKLMNOPQRSTUVWXYZ----------"
            #self.SwitchLetters = {}

            if FromItem == "-":
                FromWho = Lang.find((ToItem.split("-"))[0])
                ToWho = Lang.find((ToItem.split("-"))[1])
                del self.SwitchLetters[(ToItem.split("-"))[0]]
                del self.SwitchLetters[(ToItem.split("-"))[1]]
                self.ui.tableWidget_3.setItem(ToWho//9,ToWho%9,QtWidgets.QTableWidgetItem(f"{Lang[ToWho]}"))
                self.ui.tableWidget_3.setItem(FromWho//9,FromWho%9,QtWidgets.QTableWidgetItem(f"{Lang[FromWho]}"))
            elif ToItem == "-":
                FromWho = Lang.find((FromItem.split("-"))[0])
                ToWho = Lang.find((FromItem.split("-"))[1])
                del self.SwitchLetters[(FromItem.split("-"))[0]]
                del self.SwitchLetters[(FromItem.split("-"))[1]]
                self.ui.tableWidget_3.setItem(ToWho//9,ToWho%9,QtWidgets.QTableWidgetItem(f"{Lang[ToWho]}"))
                self.ui.tableWidget_3.setItem(FromWho//9,FromWho%9,QtWidgets.QTableWidgetItem(f"{Lang[FromWho]}"))
            elif not("-" in FromItem) and not("-" in ToItem):
                self.SwitchLetters[FromItem] = ToItem
                self.SwitchLetters[ToItem] = FromItem 
                self.ui.tableWidget_3.setItem(fromIndexRow, fromIndexColumn, QtWidgets.QTableWidgetItem(f"{FromItem}-{ToItem}"))
                self.ui.tableWidget_3.setItem(toIndexRow, toIndexColumn, QtWidgets.QTableWidgetItem(f"{ToItem}-{FromItem}"))
            else:
                print("Буквы уже соединены")
        except Exception as exp:
            print(exp)

    def EncryptingWord(self):
        Text = (self.ui.plainTextEdit_5.toPlainText()).upper()
        lang = self.ui.comboBox.currentText()
        if self.ui.checkBox.isChecked():
            abc = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" if "RUS" in lang.upper() else "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            Text = "".join(list([x for x in list(Text) if x in abc]))

        if Text == "" or Text == None:
            Text = "-"

        TempFValue = str(self.ui.spinBox.value())
        TempSValue = str(self.ui.spinBox_2.value())
        TempTValue = str(self.ui.spinBox_3.value())

        if "RUS" in lang.upper():
            if self.SwitchingPanelBool:
                Text = list(Text)
                for xPos, element in enumerate(Text):
                    if element in self.SwitchLetters:
                        Text[xPos] = self.SwitchLetters[element]
                Text = "".join(Text)
            View = self.EnigmaDefault.EncryptWord("RUS", Text)
            if self.SwitchingPanelBool:
                View = list(View)
                for xPos, element in enumerate(View):
                    if element in self.SwitchLetters:
                        View[xPos] = self.SwitchLetters[element]
                View = "".join(View)
            self.ui.plainTextEdit_6.setPlainText(View)
            self.ui.spinBox_3.setValue(int(self.EnigmaDefault.RusCount[0]))
            self.ui.spinBox_2.setValue(int(self.EnigmaDefault.RusCount[1]))
            self.ui.spinBox.setValue(int(self.EnigmaDefault.RusCount[2]))
        elif "ENG" in lang.upper():
            if self.SwitchingPanelBool:
                Text = list(Text)
                for xPos, element in enumerate(Text):
                    if element in self.SwitchLetters:
                        Text[xPos] = self.SwitchLetters[element]
                Text = "".join(Text)
            View = self.EnigmaDefault.EncryptWord("ENG", Text)
            if self.SwitchingPanelBool:
                View = list(View)
                for xPos, element in enumerate(View):
                    if element in self.SwitchLetters:
                        View[xPos] = self.SwitchLetters[element]
                View = "".join(View)
            self.ui.plainTextEdit_6.setPlainText(View)
            self.ui.spinBox_3.setValue(int(self.EnigmaDefault.EngCount[0]))
            self.ui.spinBox_2.setValue(int(self.EnigmaDefault.EngCount[1]))
            self.ui.spinBox.setValue(int(self.EnigmaDefault.EngCount[2]))   
        self.ui.label_28.setText(TempFValue)
        self.ui.label_29.setText(TempSValue)
        self.ui.label_27.setText(TempTValue)
        self.clicked_button.play()
        del TempFValue, TempSValue, TempTValue   

    def PreEncryptingWord(self):
        Text = (self.ui.plainTextEdit_5.toPlainText()).upper()
        lang = self.ui.comboBox.currentText()
        if self.ui.checkBox.isChecked():
            abc = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" if "RUS" in lang.upper() else "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            Text = "".join(list([x for x in list(Text) if x in abc]))

        if Text == "" or Text == None:
            Text = "-"

        if "RUS" in lang.upper():
            SavedSettings = [0, 0, 0]
            SavedSettings[0] = self.EnigmaDefault.RusCount[0]
            SavedSettings[1] = self.EnigmaDefault.RusCount[1]
            SavedSettings[2] = self.EnigmaDefault.RusCount[2]
            if self.SwitchingPanelBool:
                Text = list(Text)
                for xPos, element in enumerate(Text):
                    if element in self.SwitchLetters:
                        Text[xPos] = self.SwitchLetters[element]
                Text = "".join(Text)
            preView = self.EnigmaDefault.EncryptWord("RUS", Text)
            if self.SwitchingPanelBool:
                preView = list(preView)
                for xPos, element in enumerate(preView):
                    if element in self.SwitchLetters:
                        preView[xPos] = self.SwitchLetters[element]
                preView = "".join(preView)
            self.ui.plainTextEdit_6.setPlaceholderText(preView)
            self.EnigmaDefault.RusCount[0] = SavedSettings[0]
            self.EnigmaDefault.RusCount[1] = SavedSettings[1]
            self.EnigmaDefault.RusCount[2] = SavedSettings[2]
        elif "ENG" in lang.upper():
            SavedSettings = [0, 0, 0]
            SavedSettings[0] = self.EnigmaDefault.EngCount[0]
            SavedSettings[1] = self.EnigmaDefault.EngCount[1]
            SavedSettings[2] = self.EnigmaDefault.EngCount[2]
            if self.SwitchingPanelBool:
                Text = list(Text)
                for xPos, element in enumerate(Text):
                    if element in self.SwitchLetters:
                        Text[xPos] = self.SwitchLetters[element]
                Text = "".join(Text)
            preView = self.EnigmaDefault.EncryptWord("ENG", Text)
            if self.SwitchingPanelBool:
                preView = list(preView)
                for xPos, element in enumerate(preView):
                    if element in self.SwitchLetters:
                        preView[xPos] = self.SwitchLetters[element]
                preView = "".join(preView)
            self.ui.plainTextEdit_6.setPlaceholderText(preView)
            self.EnigmaDefault.EngCount[0] = SavedSettings[0]
            self.EnigmaDefault.EngCount[1] = SavedSettings[1]
            self.EnigmaDefault.EngCount[2] = SavedSettings[2]

    def UseEnigmaFunctionWithAlpha(self):
        lang = self.ui.comboBox.currentText()
        row = self.ui.tableWidget.currentRow()
        column = self.ui.tableWidget.currentColumn()
        value = (self.ui.tableWidget.item(row, column)).text()
        if value == "-":
            return
        if "RUS" in lang.upper():
            if value in self.SwitchLetters and self.SwitchingPanelBool:
                value = self.SwitchLetters[value]
            anwser = self.EnigmaDefault.RUSLANG.find(self.EnigmaDefault.EncryptAlphaRus(value))
            value = self.EnigmaDefault.RUSLANG[anwser]
            if value in self.SwitchLetters and self.SwitchingPanelBool:
                value = self.SwitchLetters[value]
                anwser = self.EnigmaDefault.RUSLANG.find(value)
            self.ui.spinBox_3.setValue(int(self.EnigmaDefault.RusCount[0]))
            self.ui.spinBox_2.setValue(int(self.EnigmaDefault.RusCount[1]))
            self.ui.spinBox.setValue(int(self.EnigmaDefault.RusCount[2]))
        elif "ENG" in lang.upper():
            if value in self.SwitchLetters and self.SwitchingPanelBool:
                value = self.SwitchLetters[value]
            anwser = self.EnigmaDefault.ENGLANG.find(self.EnigmaDefault.EncryptAlphaEng(value))
            value = self.EnigmaDefault.ENGLANG[anwser]
            if value in self.SwitchLetters and self.SwitchingPanelBool:
                value = self.SwitchLetters[value]
                anwser = self.EnigmaDefault.ENGLANG.find(value)
            self.ui.spinBox_3.setValue(int(self.EnigmaDefault.EngCount[0]))
            self.ui.spinBox_2.setValue(int(self.EnigmaDefault.EngCount[1]))
            self.ui.spinBox.setValue(int(self.EnigmaDefault.EngCount[2]))
        else:
            return
        
        row = anwser // 7
        column = anwser % 7
        self.clicked_button.play()
        self.ui.tableWidget_2.item(self.lastShowedAlpha[0], self.lastShowedAlpha[1]).setBackground(QColor(40, 40, 40))
        self.lastShowedAlpha = [row, column]
        self.ui.tableWidget_2.item(row, column).setBackground(QColor(255, 170, 0))
        oldvalue = self.ui.plainTextEdit_2.toPlainText()
        value = oldvalue + value
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_2.setPlainText(value)

    def SetEnigmaSettings(self):
        try:
            self.accept_button.play()
            lang = self.ui.comboBox.currentText()

            if "RUS" in lang.upper():
                if not("Б" in (self.ui.tableWidget_3.item(0, 1)).text()):
                    self.ResetSwitchingPanel()
                self.ui.spinBox.setMaximum(32)
                self.ui.spinBox_2.setMaximum(32)
                self.ui.spinBox_3.setMaximum(32)
                self.EnigmaDefault.RusCount[0] = self.ui.spinBox_3.value()
                self.EnigmaDefault.RusCount[1] = self.ui.spinBox_2.value()
                self.EnigmaDefault.RusCount[2] = self.ui.spinBox.value()
                alphas = list([list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ--"[x:x+7]) for x in range(0, len("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ--"), 7)])
                self.ui.tableWidget.setRowCount(5)
                self.ui.tableWidget_2.setRowCount(5)
                for idLine, line in enumerate(alphas):
                    for idL, alpha in enumerate(line):
                        self.ui.tableWidget.setItem(idLine, idL, QtWidgets.QTableWidgetItem(str(alpha)))
                        self.ui.tableWidget_2.setItem(idLine, idL, QtWidgets.QTableWidgetItem(str(alpha)))

            elif "ENG" in lang.upper():
                if not("B" in (self.ui.tableWidget_3.item(0, 1)).text()):
                    self.ResetSwitchingPanel()
                self.ui.spinBox.setMaximum(25)
                self.ui.spinBox_2.setMaximum(25)
                self.ui.spinBox_3.setMaximum(25)
                self.EnigmaDefault.EngCount[0] = self.ui.spinBox_3.value()
                self.EnigmaDefault.EngCount[1] = self.ui.spinBox_2.value()
                self.EnigmaDefault.EngCount[2] = self.ui.spinBox.value()
                self.ui.tableWidget.setRowCount(4)
                self.ui.tableWidget_2.setRowCount(4)
                alphas = list([list("ABCDEFGHIJKLMNOPQRSTUVWXYZ--"[x:x+7]) for x in range(0, len("ABCDEFGHIJKLMNOPQRSTUVWXYZ--"), 7)])
                for idLine, line in enumerate(alphas):
                    for idL, alpha in enumerate(line):
                        self.ui.tableWidget.setItem(idLine, idL, QtWidgets.QTableWidgetItem(str(alpha)))
                        self.ui.tableWidget_2.setItem(idLine, idL, QtWidgets.QTableWidgetItem(str(alpha)))
            
            self.ui.label_24.setText(str(self.ui.spinBox.value()))
            self.ui.label_25.setText(str(self.ui.spinBox_2.value()))
            self.ui.label_26.setText(str(self.ui.spinBox_3.value()))
            self.ui.plainTextEdit_2.setPlainText("")
            self.ui.plainTextEdit_6.setPlainText("")
            
        except Exception as exp:
            print(exp)

    def DeleteLastSymbol(self):
        try:
            value = self.ui.plainTextEdit_2.toPlainText()
            if value == "" or value == None:
                return
            
            self.accept_button.play()
            self.ui.plainTextEdit_2.clear()
            self.ui.plainTextEdit_2.setPlainText(value[:-1])

            lang = self.ui.comboBox.currentText()

            if "RUS" in lang.upper():
                if self.EnigmaDefault.RusCount[2] - 1 < 0:
                    self.EnigmaDefault.RusCount[2] = 32
                    if self.EnigmaDefault.RusCount[1] - 1 < 0:
                        self.EnigmaDefault.RusCount[1] = 32
                        if self.EnigmaDefault.RusCount[0] - 1 < 0:
                            self.EnigmaDefault.RusCount[0] = 32
                        else:
                            self.EnigmaDefault.RusCount[0] -= 1
                    else:
                        self.EnigmaDefault.RusCount[1] -= 1
                else:
                    self.EnigmaDefault.RusCount[2] -= 1

                self.ui.spinBox_3.setValue(int(self.EnigmaDefault.RusCount[0]))
                self.ui.spinBox_2.setValue(int(self.EnigmaDefault.RusCount[1]))
                self.ui.spinBox.setValue(int(self.EnigmaDefault.RusCount[2]))
            elif "ENG" in lang.upper():
                if self.EnigmaDefault.EngCount[2] - 1 < 0:
                    self.EnigmaDefault.EngCount[2] = 25
                    if self.EnigmaDefault.EngCount[1] - 1 < 0:
                        self.EnigmaDefault.EngCount[1] = 25
                        if self.EnigmaDefault.EngCount[0] - 1 < 0:
                            self.EnigmaDefault.EngCount[0] = 25
                        else:
                            self.EnigmaDefault.EngCount[0] -= 1
                    else:
                        self.EnigmaDefault.EngCount[1] -= 1
                else:
                    self.EnigmaDefault.EngCount[2] -= 1

                self.ui.spinBox_3.setValue(int(self.EnigmaDefault.EngCount[0]))
                self.ui.spinBox_2.setValue(int(self.EnigmaDefault.EngCount[1]))
                self.ui.spinBox.setValue(int(self.EnigmaDefault.EngCount[2]))
        except Exception as exp:
            print(exp)

    def LoadSounds(self):
        self.clicked_button = QSound('sounds/clicked.wav', self)
        self.accept_button = QSound('sounds/accept.wav', self)
        self.changePanel = QSound('sounds/changePanel.wav', self)
        self.switchPanelOut = QSound("sounds/outSwitchPanel.wav", self)  
        self.rotorPassSound = QSound("sounds/moveRotor.wav", self)

        self.ui.pushButton_2.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(1), self.changePanel.play()])
        self.ui.pushButton_10.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(2), self.changePanel.play()])
        self.ui.pushButton_26.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(3), self.changePanel.play()])
        self.ui.pushButton_4.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(4), self.changePanel.play()])
        self.ui.pushButton_16.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(5), self.changePanel.play()])

        self.ui.pushButton_3.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(0), self.changePanel.play()])
        self.ui.pushButton_11.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(2), self.changePanel.play()])
        self.ui.pushButton_27.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(3), self.changePanel.play()])
        self.ui.pushButton_6.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(4), self.changePanel.play()])
        self.ui.pushButton_17.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(5), self.changePanel.play()])

        self.ui.pushButton_41.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(0), self.changePanel.play()])
        self.ui.pushButton_42.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(1), self.changePanel.play()])
        self.ui.pushButton_43.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(3), self.changePanel.play()])
        self.ui.pushButton_44.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(4), self.changePanel.play()])
        self.ui.pushButton_19.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(5), self.changePanel.play()])

        self.ui.pushButton_29.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(0), self.changePanel.play()])
        self.ui.pushButton_30.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(1), self.changePanel.play()])
        self.ui.pushButton_12.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(2), self.changePanel.play()])
        self.ui.pushButton_32.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(4), self.changePanel.play()])
        self.ui.pushButton_18.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(5), self.changePanel.play()])

        self.ui.pushButton_7.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(0), self.changePanel.play()])
        self.ui.pushButton_8.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(1), self.changePanel.play()])
        self.ui.pushButton_14.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(2), self.changePanel.play()])
        self.ui.pushButton_28.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(3), self.changePanel.play()])
        self.ui.pushButton_46.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(5), self.changePanel.play()])

        self.ui.pushButton_20.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(0), self.changePanel.play()])
        self.ui.pushButton_21.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(1), self.changePanel.play()])
        self.ui.pushButton_22.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(2), self.changePanel.play()])
        self.ui.pushButton_23.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(4), self.changePanel.play()])
        self.ui.pushButton_47.clicked.connect(lambda: [self.ui.tabWidget.setCurrentIndex(3), self.changePanel.play()])

        self.ui.spinBox.valueChanged.connect(self.rotorPassSound.play)
        self.ui.spinBox_2.valueChanged.connect(self.rotorPassSound.play)
        self.ui.spinBox_3.valueChanged.connect(self.rotorPassSound.play)

def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.setFixedSize(1095, 700)
    application.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()
