from __future__ import division 
import wx
from math import *


class Calculator(wx.Frame):
	calculation=""
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'Calculator!',size=(400,500))
		panel=wx.Panel(self)
		panel.SetBackgroundColour((135,206,250))
		
		#add a text field combo box for calculations to be displayed and stored
		self.inputField = wx.ComboBox(panel,value="",pos=(0,0),size=(300,50))
		#allow for the input to be typed
		self.inputField.Bind(wx.EVT_TEXT,self.OnKeyTyped)
		
		#create all the buttons
		btn1=wx.Button(panel,label="1",pos=(0,300), size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.one, btn1)
		btn1.SetBackgroundColour((135,206,255))
		
		btn2=wx.Button(panel,label="2",pos=(100,300),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.two, btn2)
		btn2.SetBackgroundColour((135,206,255))
		
		btn3=wx.Button(panel,label="3",pos=(200,300),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.three, btn3)
		btn3.SetBackgroundColour((135,206,255))
		
		btn4=wx.Button(panel,label="4",pos=(0,200),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.four, btn4)
		btn4.SetBackgroundColour((135,206,255))
		
		btn5=wx.Button(panel,label="5",pos=(100,200),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.five, btn5)
		btn5.SetBackgroundColour((135,206,255))
		
		btn6=wx.Button(panel,label="6",pos=(200,200),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.six, btn6)
		btn6.SetBackgroundColour((135,206,255))
		
		btn7=wx.Button(panel,label="7",pos=(0,100),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.seven, btn7)
		btn7.SetBackgroundColour((135,206,255))
		
		btn8=wx.Button(panel,label="8",pos=(100,100),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.eight, btn8)
		btn8.SetBackgroundColour((135,206,255))		
		
		btn9=wx.Button(panel,label="9",pos=(200,100),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.nine, btn9)
		btn9.SetBackgroundColour((135,206,255))
		
		btn0=wx.Button(panel,label="0",pos=(0,400),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.zero, btn0)
		btn0.SetBackgroundColour((135,206,255))
		
		btnclr=wx.Button(panel,label="CLR",pos=(300,0),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.clear, btnclr)
		btnclr.SetBackgroundColour((255,127,80))
		
		btnplus=wx.Button(panel,label="+",pos=(300,400),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.plus, btnplus)
		btnplus.SetBackgroundColour((30,144,255))
		
		btnminus=wx.Button(panel,label="-",pos=(300,300),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.minus, btnminus)
		btnminus.SetBackgroundColour((30,144,255))
		
		btnmultiply=wx.Button(panel,label="x",pos=(300,200),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.multiply, btnmultiply)
		btnmultiply.SetBackgroundColour((30,144,255))
		
		btndivide=wx.Button(panel,label="/",pos=(300,100),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.divide, btndivide)
		btndivide.SetBackgroundColour((30,144,255))
		
		btnpoint=wx.Button(panel,label=".",pos=(100,400),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.point, btnpoint)
		btnpoint.SetBackgroundColour((30,144,255))
		
		btnequal=wx.Button(panel,label="=",pos=(200,400),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.equal, btnequal)
		btnequal.SetBackgroundColour((30,144,255))
		
		btnopen=wx.Button(panel,label="(",pos=(0,50),size=(50,50))
		self.Bind(wx.EVT_BUTTON,self.open,btnopen)
		btnopen.SetBackgroundColour((30,144,255))
		
		btnclose=wx.Button(panel,label=")",pos=(50,50),size=(50,50))
		self.Bind(wx.EVT_BUTTON,self.close,btnclose)
		btnclose.SetBackgroundColour((30,144,255))
		
		btnsqrt=wx.Button(panel,label="sqrt",pos=(100,50),size=(50,50))
		self.Bind(wx.EVT_BUTTON,self.sqrt,btnsqrt)
		btnsqrt.SetBackgroundColour((30,144,255))
		
		btnsin=wx.Button(panel,label="sin",pos=(150,50), size=(50,50))
		self.Bind(wx.EVT_BUTTON,self.sin,btnsin)
		btnsin.SetBackgroundColour((30,144,255))
		
		btncos=wx.Button(panel,label="cos",pos=(200,50), size=(50,50))
		self.Bind(wx.EVT_BUTTON,self.cos,btncos)
		btncos.SetBackgroundColour((30,144,255))
		
		btntan=wx.Button(panel,label="tan",pos=(250,50), size=(50,50))
		self.Bind(wx.EVT_BUTTON,self.tan,btntan)
		btntan.SetBackgroundColour((30,144,255))
		
	
		
		
	#create a function for each button press
	def one(self,event):
		self.calculation = self.calculation + "1"
		self.inputField.SetValue(self.calculation)
	def two(self,event):
		self.calculation = self.calculation + "2"
		self.inputField.SetValue(self.calculation)
	def three(self,event):
		self.calculation = self.calculation + "3"
		self.inputField.SetValue(self.calculation)
	def four(self,event):
		self.calculation = self.calculation + "4"
		self.inputField.SetValue(self.calculation)
	def five(self,event):
		self.calculation = self.calculation + "5"
		self.inputField.SetValue(self.calculation)
	def six(self,event):
		self.calculation = self.calculation + "6"
		self.inputField.SetValue(self.calculation)
	def seven(self,event):
		self.calculation = self.calculation + "7"
		self.inputField.SetValue(self.calculation)
	def eight(self,event):
		self.calculation = self.calculation + "8"
		self.inputField.SetValue(self.calculation)
	def nine(self,event):
		self.calculation = self.calculation + "9"
		self.inputField.SetValue(self.calculation)
	def zero(self,event):
		self.calculation = self.calculation + "0"
		self.inputField.SetValue(self.calculation)	
	def clear(self,event):
		self.calculation = ""
		self.inputField.SetValue(self.calculation)	
	def plus(self,event):
		self.calculation= self.calculation + "+"
		self.inputField.SetValue(self.calculation)
	def minus(self,event):
		self.calculation= self.calculation + "-"
		self.inputField.SetValue(self.calculation)
	def multiply(self,event):
		self.calculation= self.calculation + "*"
		self.inputField.SetValue(self.calculation)
	def divide(self,event):
		self.calculation= self.calculation + "/"
		self.inputField.SetValue(self.calculation)
	def point(self,event):
		self.calculation= self.calculation + "."
		self.inputField.SetValue(self.calculation)
	def open(self,event):
		self.calculation=self.calculation + "("
		self.inputField.SetValue(self.calculation)
	def close(self,event):
		self.calculation=self.calculation + ")"
		self.inputField.SetValue(self.calculation)
	def sqrt(self,event):
		self.calculation=self.calculation + "sqrt("
		self.inputField.SetValue(self.calculation)
	def sin(self,event):
		self.calculation=self.calculation + "sin("
		self.inputField.SetValue(self.calculation)
	def cos(self,event):
		self.calculation=self.calculation + "cos("
		self.inputField.SetValue(self.calculation)
	def tan(self,event):
		self.calculation=self.calculation + "tan("
		self.inputField.SetValue(self.calculation)
		
	#evaluate the function entered
	def equal(self,event):
		#try-catch block to handle exceptions
		try:
			#evalutate the string as a math function
			result = eval(self.calculation)
			#add the function to the combo box history
			self.inputField.Insert(self.calculation, 0)
			#set the text field to the answer
			self.inputField.SetValue(str(result))
			self.calcuation = ""
		except Exception, e:
			wx.LogError(str(e))
			return
		self.calcuation = ""
	
	#handle keyboard entries
	#cannot handle enter key invocation yet or error checking
	def OnKeyTyped(self, event): 
		self.calculation = event.GetString() 
		
if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=Calculator(parent=None,id=-1)
	frame.Show()
	app.MainLoop()
		
