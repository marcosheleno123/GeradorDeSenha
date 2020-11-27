import PySimpleGUI
import os

class TelaPython:
    def __init__(self):

        PySimpleGUI.theme('DarkBlue13')

        layout = [
            [PySimpleGUI.Text('Nome',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='nome')],
            [PySimpleGUI.Text('Aniversário',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='aniversario')],
            [PySimpleGUI.Text('Sobrenome',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='sobrenome')],
            [PySimpleGUI.Text('Animal',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='dog')],
            [PySimpleGUI.Text('Filme',size=(10,0)),PySimpleGUI.Input(size=(30,0),key='filme')],
            #[PySimpleGUI.Text(' ' , size=(5,0))],
            [PySimpleGUI.Text('Usar caracteres especiais?')],
            [PySimpleGUI.Radio('Sim', 'caracteres',key='sim'),PySimpleGUI.Radio('Não','caracteres',key='não'),],
            [PySimpleGUI.Checkbox('Salvar senhas',key='salvar')],
            [PySimpleGUI.Button('Gerar senhas')],
            [PySimpleGUI.Output(size=(58,10))],
            [PySimpleGUI.Text('Desenvolvido por Murilo Martins                                      Versão: 3.0' , size=(60,0))]
        ]
        self.janela = PySimpleGUI.Window("Gerador de senha").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            aniversario = self.values['aniversario']
            sobrenome = self.values['sobrenome']
            dog = self.values['dog']
            filme = self.values['filme']
            sim = self.values['sim']
            nao = self.values['não']
            salvar = self.values['salvar']
            
            senha1c = aniversario+'%'+sobrenome+'-'+nome+'@'+dog+'#'+filme
            senha2c = nome+')'+aniversario+'$'+filme+'!'+dog+'&'+sobrenome
            senha3c = dog+'#'+nome+'+'+filme+'*'+aniversario+'_'+sobrenome
            senha4c = aniversario+'$'+dog+'%'+filme+'"'+sobrenome+'('+nome

            senha1s = aniversario+sobrenome+nome+dog+filme
            senha2s = nome+aniversario+filme+dog+sobrenome
            senha3s = dog+nome+filme+aniversario+sobrenome
            senha4s = aniversario+dog+sobrenome+filme+nome

            if (sim == True):
                if (salvar == True):
                    with open("senhas.txt", "w") as stream:
                            print(senha1c, file=stream)
                            print(senha2c, file=stream)
                            print(senha3c, file=stream)
                            print(senha4c, file=stream)
                else:
                    print(senha1c)
                    print(senha2c)
                    print(senha3c)
                    print(senha4c)

                
            if (nao == True):
                if (salvar == True):
                    with open("senhas2.txt", "w") as stream:
                            print(senha1s, file=stream)
                            print(senha2s, file=stream)
                            print(senha3s, file=stream)
                            print(senha4s, file=stream)
                else:
                    print(senha1s)
                    print(senha2s)
                    print(senha3s)
                    print(senha4s)
           
tela = TelaPython()
tela.Iniciar()    