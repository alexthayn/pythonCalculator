import wx

class Calculator(wx.Frame):
	calculation=""
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'Calculator!',size=(400,500))
		panel=wx.Panel(self)
		
		inputField = wx.TextCtrl(panel,value="",pos=(0,0),size=(295,-1))
		inputField.Bind(wx.EVT_TEXT,self.OnKeyTyped)
		
		
		btn1=wx.Button(panel,label="1",pos=(0,300), size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.one, btn1)
		
		btn2=wx.Button(panel,label="2",pos=(100,300),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.two, btn2)
		
		btn3=wx.Button(panel,label="3",pos=(200,300),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.three, btn3)
		
		btn4=wx.Button(panel,label="4",pos=(0,200),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.four, btn4)
		
		btn5=wx.Button(panel,label="5",pos=(100,200),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.five, btn5)
		
		btn6=wx.Button(panel,label="6",pos=(200,200),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.six, btn6)
		
		btn7=wx.Button(panel,label="7",pos=(0,100),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.seven, btn7)
		
		btn8=wx.Button(panel,label="8",pos=(100,100),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.eight, btn8)
		
		btn9=wx.Button(panel,label="9",pos=(200,100),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.nine, btn9)
		
		btn0=wx.Button(panel,label="0",pos=(100,400),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.zero, btn0)
		
		btnclr=wx.Button(panel,label="CLR",pos=(300,0),size=(100,100))
		self.Bind(wx.EVT_BUTTON, self.clear, btn9)
		
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
		self.caclulation = ""
		
	def OnKeyTyped(self, event): 
		print event.GetString() 
		
		
if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=Calculator(parent=None,id=-1)
	frame.Show()
	app.MainLoop()
		
