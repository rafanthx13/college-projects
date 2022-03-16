from tkinter import *
from tkinter import messagebox
from Perceptron import Perceptron
import pickle

class Application:
    def __init__(self, master=None):
        with open('../pesos.pickle', 'rb') as file:
            self.wj = pickle.load(file)
            
        self.perceptron = Perceptron(self.wj)
        self.features = {}
        
        self.font = ('Arial', '10')
        self.width = 8

        self.ctTitulo = Frame(master)
        self.ctTitulo['padx'] = 10
        self.ctTitulo['pady'] = 5
        self.ctTitulo.pack()

        self.titulo = Label(self.ctTitulo, text = 'Qual sua probabilidade de sobreviver ao Titanic?', anchor = CENTER)
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()

        #

        self.ctAge = Frame(master)
        self.ctAge['padx'] = 10
        self.ctAge['pady'] = 5
        self.ctAge.pack(anchor = W)

        self.lbAge = Label(self.ctAge, text = 'Idade: ', font = self.font, anchor = E, width = self.width, height = 2)
        self.lbAge.pack(side = LEFT)

        self.etAge = Entry(self.ctAge, font = self.font, width = 30)
        self.etAge.pack(side = LEFT)

        #

        self.ctGender = Frame(master)
        self.ctGender['padx'] = 10
        self.ctGender['pady'] = 5
        self.ctGender.pack(anchor = W)

        self.lbGender = Label(self.ctGender, text = 'Sexo: ', font = self.font, anchor = E, width = self.width, height = 2)
        self.lbGender.pack(side = LEFT)

        self.genderVar = IntVar()
        self.rbGender0 = Radiobutton(self.ctGender, text = 'Feminino', var = self.genderVar, value = 0, font = self.font)
        self.rbGender1 = Radiobutton(self.ctGender, text = 'Masculino', var = self.genderVar, value = 1, font = self.font)
        self.rbGender0.pack(side = LEFT)
        self.rbGender1.pack(side = LEFT)
        self.rbGender0.select()
        
        #

        self.ctClass = Frame(master)
        self.ctClass['padx'] = 10
        self.ctClass['pady'] = 5
        self.ctClass.pack(anchor = W)

        self.lbClass = Label(self.ctClass, text = 'Classe: ', font = self.font, anchor = E, width = self.width, height = 2)
        self.lbClass.pack(side = LEFT)

        self.classVar = IntVar()
        self.rbClass1 = Radiobutton(self.ctClass, text = '1ª classe', var = self.classVar, value = 1, font = self.font)
        self.rbClass2 = Radiobutton(self.ctClass, text = '2ª classe', var = self.classVar, value = 2, font = self.font)
        self.rbClass3 = Radiobutton(self.ctClass, text = '3ª classe', var = self.classVar, value = 3, font = self.font)
        self.rbClass3.pack(side = LEFT)
        self.rbClass2.pack(side = LEFT)
        self.rbClass1.pack(side = LEFT)
        self.rbClass3.select()

        #
        
        self.ctSibSp = Frame(master)
        self.ctSibSp['padx'] = 10
        self.ctSibSp['pady'] = 5
        self.ctSibSp.pack(anchor = CENTER)

        self.lbSibSp = Label(self.ctSibSp, text = 'Número de irmãos + cônjuge a bordo: ', anchor = CENTER, font = self.font, height = 2)
        self.lbSibSp.pack(side = TOP)
        
        self.etSibSp = Entry(self.ctSibSp, font = self.font, width = 10)
        self.etSibSp.pack(side = TOP)

        #

        self.ctParch = Frame(master)
        self.ctParch['padx'] = 10
        self.ctParch['pady'] = 5
        self.ctParch.pack()

        self.lbParch = Label(self.ctParch, text = 'Número de pais + filhos a bordo: ', anchor = E, font = self.font, height = 2)
        self.lbParch.pack(side = TOP)

        self.etParch = Entry(self.ctParch, font = self.font, width = 10)
        self.etParch.pack(side = TOP)
        
        #

        self.ctCalc = Frame(master)
        self.ctCalc['padx'] = 10
        self.ctCalc['pady'] = 20
        self.ctCalc.pack()
        
        self.btCalc = Button(self.ctCalc, text = 'Calcular', font = self.font, width = 12)
        self.btCalc['command'] = self.Calc
        self.btCalc.pack(side = TOP)

        #
        
        master.mainloop()

    def Calc(self):
        
        if self.etParch.get() != '':
            self.features['Parch'] = int(self.etParch.get())
        else:
            self.features['Parch'] = 0

        self.features['Pclass'] = self.classVar.get()
        self.features['Sex'] = self.genderVar.get()

        if self.etAge.get() != '':
            self.features['Age'] = int(self.etAge.get())
        else:
            self.features['Age'] = 0

        if self.etSibSp.get() != '':
            self.features['SibSp'] = int(self.etSibSp.get())
        else:
            self.features['SibSp'] = 0

        result = self.perceptron.neuron(self.features)
        print(self.features)
        print(result)
        if(result == 0):
            message = 'Voce Morreria'
        else:
            message = 'Voce Sobreviveria'
        # result *= 100
        # message = 'Você teria'
        # message + str(result) + '% de chance de sobreviver!' 
        messagebox.showinfo('Resultado', message)
        

root = Tk()
Application(root)
