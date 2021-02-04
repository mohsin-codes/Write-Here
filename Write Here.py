import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import font, colorchooser, filedialog
import os

main_window = tk.Tk()
main_window.geometry("1366x768")
main_window.title("Write Here")

################################## Main Menu ##############################################
main_menu = tk.Menu(main_window)

#Menu Icons
New = tk.PhotoImage(file = "Icons/new.png")
Open = tk.PhotoImage(file = "Icons/Open.png")
Save = tk.PhotoImage(file = "Icons/diskette.png")
Exit = tk.PhotoImage(file = "Icons/Exit2.png")


file = tk.Menu(main_menu, tearoff = False)


#Edit Icons
Cut = tk.PhotoImage(file = 'Icons/cutting.png')
copy = tk.PhotoImage(file = 'Icons/copy.png')
paste = tk.PhotoImage(file = 'Icons/paste.png')
clear = tk.PhotoImage(file = 'Icons/Clear.png')
find = tk.PhotoImage(file = 'Icons/find.png')

edit = tk.Menu(main_menu, tearoff = False)

#View Icons
toolbar = tk.PhotoImage(file = 'Icons/toolbar.png')
statusbar = tk.PhotoImage(file = 'Icons/Status.png')

view = tk.Menu(main_menu, tearoff = False)


#Theme Icons
white = tk.PhotoImage(file = 'Icons/White.png')
Black = tk.PhotoImage(file = 'Icons/Black.png')
Blue = tk.PhotoImage(file = 'Icons/Blue.png')
Red= tk.PhotoImage(file = 'Icons/Red.png')

theme = tk.Menu(main_menu, tearoff = False)
theme_choice = tk.StringVar()
colors = (white, Black, Blue, Red)
color_dict = {
    'white' : ('#000000', '#ffffff'),
    'Black' : ('#c4c4c4', '#2d2d2d'),
    'Blue' : ('#ededed', '#6b9dc2'),
    'Red' : ('#2d2d2d', '#ffe8e8')
}


# theme.add_command(label = 'Light', image = white, compound = tk.LEFT)
# theme.add_command(label = 'Dark', image = Black, compound = tk.LEFT)
# theme.add_command(label = 'Midnight Blue', image =Blue, compound = tk.LEFT)
# theme.add_command(label = 'Crimson Red', image = Red, compound = tk.LEFT)

about_icon = tk.PhotoImage(file = "Icons/info.png")
update_icon = tk.PhotoImage(file = "Icons/update.png")

about = tk.Menu(main_menu, tearoff = False)
about.add_command(label = 'About', image = about_icon, compound = tk.LEFT)
about.add_separator()
about.add_command(label = 'Check for Updates', image = update_icon, compound = tk.LEFT)



#cascade
main_menu.add_cascade(label = 'File', menu = file)
main_menu.add_cascade(label = 'Edit', menu = edit)
main_menu.add_cascade(label = 'View', menu = view)
main_menu.add_cascade(label = 'Theme', menu = theme)
main_menu.add_cascade(label = 'About', menu = about)

#-------------------------------- Main Menu End -------------------------------------------

################################## Toolbar ##############################################

tool_bar = ttk.Label(main_window)
tool_bar.pack(side = tk.TOP, fill = tk.X)

#font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width = 30, textvariable = font_family, state = 'readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row = 0, column = 0, padx = 5)

#font size
font_size = tk.StringVar()
font_size_box = ttk.Combobox(tool_bar, width = 5, textvariable = font_size, state = 'readonly')
font_size_box['values'] = tuple(range(8,81,2))
font_size_box.current(2)
font_size_box.grid(row = 0, column = 1, padx = 5)

#Bold Icon
bold_icon = tk.PhotoImage(file = "Icons/Bold.png")
bold_btn = ttk.Button(tool_bar, image = bold_icon)
bold_btn.grid(row = 0, column = 2, padx = 3)

#italics button
italics_icon = tk.PhotoImage(file ="Icons/Italics.png")
italics_btn = ttk.Button(tool_bar, image = italics_icon)
italics_btn.grid(row = 0, column = 3, padx = 3)

#underline button
underline_icon = tk.PhotoImage(file = "Icons/Underline.png")
underline_btn = ttk.Button(tool_bar, image = underline_icon)
underline_btn.grid(row = 0, column = 4, padx = 3)

#Color Picker
color_picker_icon = tk.PhotoImage(file = "Icons/Color Palette.png")
color_btn = ttk.Button(tool_bar, image = color_picker_icon)
color_btn.grid(row = 0, column = 5, padx = 3)

#Left Align
left_align_icon = tk.PhotoImage(file = "Icons/Left Align.png")
left_btn = ttk.Button(tool_bar, image = left_align_icon)
left_btn.grid(row = 0, column = 6, padx = 5)

#Center Align
center_align_icon = tk.PhotoImage(file = "Icons/Center Align.png")
center_btn = ttk.Button(tool_bar, image = center_align_icon)
center_btn.grid(row = 0, column = 7, padx = 3)

#Right Align
right_align_icon = tk.PhotoImage(file = "Icons/Right Align.png")
right_btn = ttk.Button(tool_bar, image = right_align_icon)
right_btn.grid(row = 0, column = 8, padx = 3)

#-------------------------------- Toolbar End -------------------------------------------

################################## Text Editor ##############################################
text_editor = tk.Text(main_window)
text_editor.config(wrap = 'word', relief = tk.FLAT)

scroll_bar = tk.Scrollbar(main_window)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT, fill = tk.Y)
text_editor.pack(fill = tk.BOTH, expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

#-------------------------------- Text Editor End -------------------------------------------

################################## Main Status Bar ##############################################
#-------------------------------- Main Status Bar End -------------------------------------------

################################## Main Menu Functionality ##############################################

#File Commands
file.add_command(label = 'New', image = New, compound = tk.LEFT, accelerator = 'Ctrl+N')
file.add_command(label = 'Open', image = Open, compound = tk.LEFT, accelerator = 'Ctrl+O')
file.add_command(label = 'Save', image = Save, compound = tk.LEFT, accelerator = 'Ctrl+S')
file.add_command(label = 'Exit', image = Exit, compound = tk.LEFT, accelerator = 'Ctrl+W')


#Edit Commands
edit.add_command(label = 'Cut', image = Cut, compound = tk.LEFT, accelerator = 'Ctrl+X')
edit.add_command(label = 'Copy', image = copy, compound = tk.LEFT, accelerator = 'Ctrl+C')
edit.add_command(label = 'Paste', image = paste, compound = tk.LEFT, accelerator = 'Ctrl+V')
edit.add_command(label = 'Clear', image = clear, compound = tk.LEFT, accelerator = 'Ctrl+Shift+C')
edit.add_command(label = 'Find', image = find, compound = tk.LEFT, accelerator = 'Ctrl+F')

#View Commands
view.add_checkbutton(label = 'Toolbar', image = toolbar, compound = tk.LEFT)
view.add_checkbutton(label = 'Status bar', image = statusbar, compound = tk.LEFT)

#Theme Commands
count = 0
for i in color_dict:
    theme.add_radiobutton(label=i, image = colors[count], variable=theme_choice, compound = tk.LEFT)
    count += 1

#-------------------------------- Main Menu Functionality End -------------------------------------------

main_window.config(menu = main_menu)
main_window.mainloop()