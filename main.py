import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
kv = Builder.load_file("gui.kv")
class Sc_Manager(ScreenManager):
    pass
class Sc_Calculadora(Screen):
    txt_display = ObjectProperty(None)
class Calculadora(App):
    txt_display = ObjectProperty(None)
    num1 = None
    num2 = None
    op = None
    ligada = False
    fun = None
    valor = 0
    def tela_digitos(self, btn): 
        display = self.sm.get_screen('calculadora').txt_display       
        if self.se_ligada():
            self.sm.get_screen('calculadora').txt_display.text += btn.text
            if self.num1 != None:
                self.num2 = display.text
                print(self.num2)

    def funcoes(self, btn):
        self.fun = btn.text
        display = self.sm.get_screen('calculadora').txt_display
        if self.fun == "ON | CE":
            self.ligar()
        elif self.fun == "MRC":
            self.limpar_memoria()
            display.text = str(self.valor)
            self.num1 = None
            self.num2 = None
        elif self.fun == "M-":
            self.menos_memoria()            
            display.text = str(self.valor)
            self.num1 = None
            self.num2 = None
        elif self.fun == "M+":
            self.mais_memoria()            
            display.text = str(self.valor)
            self.num1 = None
            self.num2 = None
        elif self.fun == "OFF":
            self.desligar()
            self.num1 = None
            self.num2 = None
        elif self.fun == "=":
            self.igualdade(self.num1, self.num2)
    def operacoes(self, btn):
        display = self.sm.get_screen('calculadora').txt_display
        self.op = btn.text
        if self.se_ligada():
            if self.op == "+":
                self.num1 = display.text
                display.text = ''
                print('soma')            
            elif self.op == "-":
                self.num1 = display.text
                display.text = ''
                print('diferença')
            elif self.op == "*":
                self.num1 = display.text
                display.text = ''
                print('produto')
            elif self.op == "÷":
                self.num1 = display.text
                display.text = ''
                print('razão')
            elif self.op == "%":
                self.num1 = display.text
                display.text = ''
                print('porcentagem')
            elif self.op == "√":
                self.num1 = display.text
                print('raiz quadrada')                
                self.raiz_quadrada(self.num1)
    def mais_memoria(self):
        display = self.sm.get_screen('calculadora').txt_display
        if display.text != '':
            self.valor += float(display.text)
    def menos_memoria(self):
        display = self.sm.get_screen('calculadora').txt_display
        if display.text != '':
            self.valor -= float(display.text)
    def limpar_memoria(self):
        self.valor = 0
    def se_ligada(self):
        if self.ligada == True:
            return True
        else:
            return False
    def ligar(self):        
        self.ligada = True
        self.sm.get_screen('calculadora').txt_display.text = '0'        
    def desligar(self):        
        self.ligada = False
        self.sm.get_screen('calculadora').txt_display.text = ''
    def raiz_quadrada(self, num1):
        display = self.sm.get_screen('calculadora').txt_display       
        if self.se_ligada():
            if self.num1 != None:
                if self.op != None:
                    if self.op == "√":
                    
                        if float(self.num1) >= 0:
                            display.text = str(float(self.num1)**0.5)
    def igualdade(self, num1, num2):
        display = self.sm.get_screen('calculadora').txt_display        
        if self.se_ligada():
            if self.num1 != None:
                if self.op != None:                    
                    if self.num2 != None:
                        if self.op == "+":
                            display.text = str(float(self.num1) + float(self.num2))
                        elif self.op == "-":
                            display.text = str(float(self.num1) - float(self.num2))
                        elif self.op == "*":
                            display.text = str(float(self.num1) * float(self.num2))
                        elif self.op == "÷":
                            try:
                                if self.num2 != 0:
                                    display.text = str(float(self.num1) / float(self.num2))
                            except:
                                print("Impossível dividir por zero.")
                        elif self.op == "%":
                            display.text = 'porcentagem'
    def build(self):
        Window.size = (320, 480)
        App.title = "Calculadora Digital"
        self.sm = Sc_Manager()
        return self.sm
if __name__ == "__main__":
    Calculadora().run()  