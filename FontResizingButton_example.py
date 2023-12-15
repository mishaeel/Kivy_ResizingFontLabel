from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.lang.builder import Builder

# Run this code to see an example of a Kivy Button with resizing font.

class FontResizingButton(Button):

	original_window_size = Window.system_size
	original_font_size = '36sp'

	def __init__(self, **kwargs):
		super(FontResizingButton, self).__init__(**kwargs)
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

class Frame(FloatLayout):

	def __init__(self, **kwargs):
		super(Frame, self).__init__(**kwargs)

class FontResizingApp(App):

	kv_lang_styling = '''
<Frame>
	FontResizingButton:
		pos_hint: {'x': .35, 'y': .451}
		size_hint: (.3, .08)
		text: 'not clicked!'
		on_press: self.text = 'clicked!'
'''

	def build(self):
		Builder.load_string(self.kv_lang_styling)
		return Frame()

if __name__ == '__main__':
	FontResizingApp().run()