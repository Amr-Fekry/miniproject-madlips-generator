import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QMainWindow):

	def __init__(self):
		# initialize a QMainWindow object (will be referred to as "self")
		super(Window, self).__init__()
		# modify the Window object
		self.setGeometry(450, 200, 600, 400)
		self.setWindowTitle("Madlips Generator")
		self.setWindowIcon(QtGui.QIcon("smile.png"))

		# add a stacked widget for multiple pages
		self.pages = QtWidgets.QStackedWidget()
		# set the stacked widget as the central
		self.setCentralWidget(self.pages)

		# load (and show) page1
		self.page_one()

	# ________________________________________PAGES_________________________________________

	def page_one(self):

		# create a widget for the page and set a layout to it
		self.page1 = QtWidgets.QWidget()
		self.pages.addWidget(self.page1) # add to the stacked widget
		self.layout = QtWidgets.QGridLayout()
		self.layout.setAlignment(QtCore.Qt.AlignCenter) # alignment of cells inside the layout. Center = (HCenter + VCenter)
		self.page1.setLayout(self.layout)
		# make widgets of the page
		# A) intro_label1
		self.intro_label1 = QtWidgets.QLabel("""Welcome to Madlips Generator game\n\nIt takes two players to play this game: a 'game designer' and a 'game player'\n""")
		self.intro_label1.setAlignment(QtCore.Qt.AlignCenter) # alignment of text inside the label
		# B) intro_label2
		self.intro_label2 = QtWidgets.QLabel("""\ngame designer:\nwrites a sentence with some words encrypted as parts of speech. He can use a list of words that we already made for parts of speech, and he can modify this list to add/delete words. player2 must not see the sentence.\n\ngame player:\nAfter the sentence is created, it is the game player's turn to play the game. He will be asked to replace the parts of speech present in the sentence with random words. \n\nFinally both can see the final result.\n\n""")
		#self.intro_label2.setMaximumWidth(800)
		#self.intro_label2.setMinimumWidth(800)
		self.intro_label2.setMinimumHeight(160)
		self.intro_label2.setWordWrap(True)
		# C) gotit_btn
		self.gotit_btn = QtWidgets.QPushButton("Got it")
		self.gotit_btn.clicked.connect(self.page1_gotit_btn)
		#self.gotit_btn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		# add widgets/layouts to main layout
		self.layout.addWidget(self.intro_label1, 0, 0, QtCore.Qt.AlignCenter) 
		self.layout.addWidget(self.intro_label2, 1, 0, QtCore.Qt.AlignCenter)
		self.layout.addWidget(self.gotit_btn, 2, 0, QtCore.Qt.AlignCenter) # for grid layout: (widget, row, column, alignment in cell)
		# show page1
		self.pages.setCurrentIndex(0)
		# load page2
		self.page_two()

	def page_two(self):

		# create a widget for the page and set a layout to it
		self.page2 = QtWidgets.QWidget()
		self.pages.addWidget(self.page2) # add to the stacked widget
		self.layout2 = QtWidgets.QGridLayout()
		self.layout2.setAlignment(QtCore.Qt.AlignCenter)
		self.page2.setLayout(self.layout2)
		# make widgets of the page
		# A) top_label
		self.top_label = QtWidgets.QLabel("""Designer turn\n\nHere is the current list of parts-of-speech that you can use:\n""")
		self.top_label.setAlignment(QtCore.Qt.AlignCenter)
		# B) pos_screen
		self.pos_screen = QtWidgets.QTextEdit()
		self.pos_screen.setFixedSize(500, 50)
		self.pos_list = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"] # initial pos_list
		self.pos_screen.setText(" , ".join(self.pos_list)) # show pos_list in pos_screen
		self.pos_screen.setReadOnly(True)
		# C) add_entry
		self.add_entry = QtWidgets.QLineEdit()
		self.add_entry.setFixedSize(100, 30)
		# D) add_btn
		self.add_btn = QtWidgets.QPushButton("Add")
		self.add_btn.clicked.connect(self.page2_add_btn)
		# E) delete_entry
		self.delete_entry = QtWidgets.QLineEdit()
		self.delete_entry.setFixedSize(100, 30)
		# F) delete_btn
		self.delete_btn = QtWidgets.QPushButton("Delete")
		self.delete_btn.clicked.connect(self.page2_delete_btn)
		# G) sub_Hlayout1
		self.sub_Hlayout1 = QtWidgets.QHBoxLayout()
		# add C, D, E, F to layout G
		self.sub_Hlayout1.addWidget(self.add_entry, False, QtCore.Qt.AlignCenter) # for horizontal layout: (widget, stretch, alignment)
		self.sub_Hlayout1.addWidget(self.add_btn, False, QtCore.Qt.AlignCenter)
		self.sub_Hlayout1.addWidget(self.delete_entry, False, QtCore.Qt.AlignCenter)
		self.sub_Hlayout1.addWidget(self.delete_btn, False, QtCore.Qt.AlignCenter)
		# H) mid_label
		self.mid_label = QtWidgets.QLabel("""* to add a word: write the word in the entry field (in all caps), then press Add\n* to delete a word: copy the word from the list and paste it in the entry field, then press Delete\n""")
		# I) mid_label2
		self.mid_label2 = QtWidgets.QLabel("""Enter your sentence with the parts of speech below:""")
		# J) sentence_entry
		self.sentence_entry = QtWidgets.QTextEdit()
		self.sentence_entry.setFixedSize(500, 100)
		# K) play_btn
		self.play_btn = QtWidgets.QPushButton("Play")
		self.play_btn.clicked.connect(self.page2_play_btn)
		# L) back_btn
		self.back_btn = QtWidgets.QPushButton("Back")
		self.back_btn.clicked.connect(self.page2_back_btn)
		# M) sub_Hlayout2 
		self.sub_Hlayout2 = QtWidgets.QHBoxLayout()
		# add K, L to the layout M
		self.sub_Hlayout2.addWidget(self.play_btn, False, QtCore.Qt.AlignCenter)
		self.sub_Hlayout2.addWidget(self.back_btn, False, QtCore.Qt.AlignCenter)
		# # add widgets/layouts to main layout
		self.layout2.addWidget(self.top_label, 0, 0, QtCore.Qt.AlignCenter)
		self.layout2.addWidget(self.pos_screen, 1, 0, QtCore.Qt.AlignCenter)
		self.layout2.addLayout(self.sub_Hlayout1, 2, 0, QtCore.Qt.AlignCenter) # layout
		self.layout2.addWidget(self.mid_label, 3, 0, QtCore.Qt.AlignCenter)
		self.layout2.addWidget(self.mid_label2, 4, 0, QtCore.Qt.AlignCenter)
		self.layout2.addWidget(self.sentence_entry, 5, 0, QtCore.Qt.AlignCenter)
		self.layout2.addLayout(self.sub_Hlayout2, 6, 0, QtCore.Qt.AlignCenter) # layout

	def page_three(self):

		# create a widget for the page and set a layout to it
		self.page3 = QtWidgets.QWidget()
		self.pages.addWidget(self.page3) # add to the stacked widget
		self.layout3 = QtWidgets.QGridLayout()
		self.layout3.setAlignment(QtCore.Qt.AlignCenter)
		self.page3.setLayout(self.layout3)
		# make widgets of the page
		# A) top_label2
		self.top_label2 = QtWidgets.QLabel("""Player turn\n\nGive an example for each part of speech below:\n""")
		self.top_label2.setAlignment(QtCore.Qt.AlignCenter)
		# B) form_layout
		self.form_layout = QtWidgets.QFormLayout()
		self.form_layout.setAlignment(QtCore.Qt.AlignCenter)
		# C) done_btn
		self.done_btn = QtWidgets.QPushButton("Done")
		self.done_btn.clicked.connect(self.page3_done_btn)
		# D) back_btn2
		self.back_btn2 = QtWidgets.QPushButton("Back")
		self.back_btn2.clicked.connect(self.page3_back_btn)
		# E) sub_Hlayout3
		self.sub_Hlayout3 = QtWidgets.QHBoxLayout()
		# add C, D to the layout E
		self.sub_Hlayout3.addWidget(self.done_btn, False, QtCore.Qt.AlignCenter)
		self.sub_Hlayout3.addWidget(self.back_btn2, False, QtCore.Qt.AlignCenter)
		# add widgets/layouts to main layout
		self.layout3.addWidget(self.top_label2, 0, 0, QtCore.Qt.AlignCenter)
		self.layout3.addLayout(self.form_layout, 1, 0, QtCore.Qt.AlignCenter)
		self.layout3.addLayout(self.sub_Hlayout3, 2, 0, QtCore.Qt.AlignCenter)

	def page_four(self):
		# create a widget for the page and set a layout to it
		self.page4 = QtWidgets.QWidget()
		self.pages.addWidget(self.page4) # add to the stacked widget
		self.layout4 = QtWidgets.QGridLayout()
		self.layout4.setAlignment(QtCore.Qt.AlignCenter)
		self.page4.setLayout(self.layout4)
		# make widgets of the page
		# A) result_label
		self.result_label = QtWidgets.QLabel("""SENTENCE:""")
		# B) sentence_label
		self.sentence_label = QtWidgets.QLabel()
		# C) image_label
		self.image_label = QtWidgets.QLabel()
		self.image = QtGui.QPixmap("chandler.png")
		self.image_label.setPixmap(self.image)
		# D) play_agin_btn
		self.playagain_btn = QtWidgets.QPushButton("Play Again")
		self.playagain_btn.clicked.connect(self.page4_playagian_btn)
		# add widgets/layouts to main layout
		self.layout4.addWidget(self.result_label, 0, 0, QtCore.Qt.AlignCenter)
		self.layout4.addWidget(self.sentence_label, 1, 0, QtCore.Qt.AlignCenter)
		self.layout4.addWidget(self.image_label, 2, 0, QtCore.Qt.AlignCenter)
		self.layout4.addWidget(self.playagain_btn, 3, 0, QtCore.Qt.AlignCenter)

	# ________________________________________METHODS_________________________________________

	def page1_gotit_btn(self):
		# show page2
		self.pages.setCurrentIndex(1)
		# load page3
		self.page_three()

	def page2_add_btn(self):
		self.to_add = self.add_entry.text() # get text from a QLineEdit
		self.pos_list.append(self.to_add)
		self.pos_screen.setText(" , ".join(self.pos_list))
		self.add_entry.clear()

	def page2_delete_btn(self):
		self.to_delete = self.delete_entry.text()
		if self.to_delete in self.pos_list:
			self.pos_list.remove(self.to_delete)
			self.pos_screen.setText(" , ".join(self.pos_list))
		else:
			pass
		self.delete_entry.clear()

	def page2_back_btn(self):
		self.delete_entry.clear()
		self.add_entry.clear()
		self.pages.setCurrentIndex(0)

	# helper function for page2_play_btn
	def pos_in_word(self, parts_of_speech, word):
		"""returns the part of speech if it is a substring in the word. otherwise, None"""
		for pos in parts_of_speech:
			if pos in word:
				return pos
		return None

	def page2_play_btn(self):
		self.sentence = self.sentence_entry.toPlainText()
		self.sentence_entry.clear()
		self.delete_entry.clear()
		self.add_entry.clear()
		self.list_of_words = self.sentence.split()

		# a list to later refer to (and parse) the dinamically generated QLineEdit in page3
		self.list_of_QLineEdits = []

		# iterate over list_of_words and make a form row (label: field) for each pos detected
		for word in self.list_of_words:
			pos_word = self.pos_in_word(self.pos_list, word)
			if pos_word:
				field = QtWidgets.QLineEdit()
				field.setMinimumHeight(30)
				field.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
				self.form_layout.addRow(pos_word+": ", field)
				self.list_of_QLineEdits.append(field)

		# show page3
		self.pages.setCurrentIndex(2)
		# load page4
		self.page_four()

	def page3_back_btn(self):
		# clear the form layout
		while self.form_layout.count():
			widgetToRemove = self.form_layout.itemAt(0).widget()
			# remove it from the layout list
			self.form_layout.removeWidget(widgetToRemove)
			# schedules object for deletion.
			widgetToRemove.deleteLater()
			# set reference to None 
			widgetToRemove = None

		self.pages.setCurrentIndex(1)

	def page3_done_btn(self):
		# get entries of user from fields and store in a list
		list_of_inputs = []
		for entry in self.list_of_QLineEdits:
			list_of_inputs.append(entry.text())

		# words of the sentence after processing 
		list_processed = []

		for index, word in enumerate(self.list_of_words):
			pos_word = self.pos_in_word(self.pos_list, word)
			if pos_word:
				word = word.replace(pos_word, list_of_inputs[0])
				self.list_of_words[index] = word
				del list_of_inputs[0]
		string_processed = " ".join(self.list_of_words)

		self.sentence_label.setText("{ " + string_processed + " }")
		# show page4
		self.pages.setCurrentIndex(3)

	def page4_playagian_btn(self):
		self.page3_back_btn()

	# ________________________________________END_________________________________________


def main():
	# initialize the App
	app = QtWidgets.QApplication(sys.argv)
	# initialize a Window object
	window = Window()
	# show window
	window.show()
	# keep app running
	sys.exit(app.exec_())

main()