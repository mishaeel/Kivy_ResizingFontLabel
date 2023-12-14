from kivy.uix.label import Label
from kivy.core.window import Window

'''
This code takes a Kivy Label and resizes the font automatically
if the window is resized/maximized/restored or if the window is dragged
to another display. I have only tested on Windows and desktop, 
float and grid layouts. Feel free to let me know if you experience issues.

To use the code, you have to declare the inital font size in python. 
For whatever reason, declaring the iniial size in the kv language has not 
worked for me. You also have to use 'sp' units in your font size.

Either: 1. Add the code below to your own Label, or

        2. Save the code as a module in your app's root directory
           and include as follows in your application's python code.
           ---------------------------------------------------------
			from FontResizingLabel import FontResizingLabel

			class YourLabel(FontResizingLabel):

				original_font_size = '22sp'
				
				# declare your initial font size in python
				# as a string with sp units

				def __init__(self, **kwargs):
					super(YourLabel, self).__init__(**kwargs)
'''

class FontResizingLabel(Label):

	original_window_size = Window.system_size
	original_font_size = '30sp'

	def __init__(self, **kwargs):
		super(FontResizingLabel, self).__init__(**kwargs)
		Window.bind(on_pre_resize=self.resize_font)
		Window.bind(on_resize=self.resize_font)
		self.font_size = self.original_font_size

	def resize_font(self, *args):
		fs = int(self.original_font_size[:2])
		wss = Window.system_size
		oss = self.original_window_size
		if (wss[0] / oss[0]) >= (wss[1] / oss[1]):
			ratio = wss[1] / oss[1]
			new_fs = fs * ratio
			new_fs_str = str(new_fs) + 'sp'
			self.font_size = new_fs_str
		elif (wss[0] / oss[0]) < (wss[1] / oss[1]):
			ratio = wss[0] / oss[0]
			new_fs = fs * ratio
			new_fs_str = str(new_fs) + 'sp'
			self.font_size = new_fs_str		
		else:
			pass
