import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_window = tk.Tk()
main_window.geometry("1366x768")
main_window.title("Write Here")
main_window.wm_iconbitmap(r'E:\Projects\Python\Write Here\Write-Here\Icon.ico')

################################## Main Menu ##############################################
main_menu = tk.Menu(main_window)

#Menu Icons
New = tk.PhotoImage(file = r'E:\Projects\Python\Write Here\Write-Here\Icons\new.png')
Open = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Open.png")
Save = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\diskette.png")
SaveAs = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\SaveAs.png")
Exit = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Exit2.png")


file = tk.Menu(main_menu, tearoff = False)


#Edit Icons
Cut = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\cutting.png")
copy = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\copy.png")
paste = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\paste.png")
clear = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Clear.png")
find = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\find.png")

edit = tk.Menu(main_menu, tearoff = False)

#View Icons
toolbar = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\toolbar.png")
statusbar = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Status.png")

view = tk.Menu(main_menu, tearoff = False)


#Theme Icons
white = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\white.png")
Black = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Black.png")
Blue = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Blue.png")
Red= tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Red.png")

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

#About Icons
about_icon = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\info.png")
update_icon = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\update.png")

def about_func():
    about_window = tk.Tk()
    about_window.title("About")
    about_window.geometry("400x200+450+200")
    about_window.resizable(0,0)
    
    #About Label Frame
    about_labelframe = ttk.LabelFrame(about_window, text = "About")
    about_labelframe.pack(pady=20)

    #Author Label
    author_desc = "This software is a basic text editor with basic functionalities.\nIt is built by Mohsin Khan as a personal project. \nFor more new stuff : \nGithub - https://github.com/mohsink98"
    author_label = ttk.Label(about_labelframe, text = author_desc)
    author_label.configure(anchor = "center")
    author_label.pack(pady=3)
    author_label.grid(row=0, column =0, padx = 4, pady = 2 )


    #Close Button
    close_btn = ttk.Button(about_labelframe, text = "Close", command = about_window.destroy)
    close_btn.config(width = 50)
    close_btn.grid(row=1, columnspan = 25, pady = 40)


    about_window.mainloop()

def updates():
    update_window = tk.Tk()
    update_window.title("Check for Updates")
    update_window.geometry("400x200+450+200")

    #Update Label Frame
    udpate_labelframe = ttk.Labelframe(update_window, text = "Steps for updation")
    udpate_labelframe.pack(pady=20)
    
    #updation steps
    steps = "1. Visit https://github.com/mohsink98/Write-Here. \n2. Download the latest version of the software.\n3. Install the latest version.\n4. Enjoy!"
    step_label = ttk.Label(udpate_labelframe, text = steps)
    step_label.grid(row=0, column=0, padx=4, pady = 4)
    step_label.configure(anchor = 'center')

    #close btn
    closebtn = ttk.Button(udpate_labelframe, text = "Close", command = update_window.destroy)
    closebtn.configure(width = 50)
    closebtn.grid(row=1, columnspan = 25, pady = 40)


    update_window.mainloop()

about = tk.Menu(main_menu, tearoff = False)
about.add_command(label = 'About', image = about_icon, compound = tk.LEFT, command = about_func)
about.add_separator()
about.add_command(label = 'Check for Updates', image = update_icon, compound = tk.LEFT, command = updates)


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
bold_icon = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Bold.png")
bold_btn = ttk.Button(tool_bar, image = bold_icon)
bold_btn.grid(row = 0, column = 2, padx = 3)

#italics button
italics_icon = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Italics.png")
italics_btn = ttk.Button(tool_bar, image = italics_icon)
italics_btn.grid(row = 0, column = 3, padx = 3)

#underline button
underline_icon = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Underline.png")
underline_btn = ttk.Button(tool_bar, image = underline_icon)
underline_btn.grid(row = 0, column = 4, padx = 3)

#Color Picker
color_picker_icon = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Color Palette.png")
color_btn = ttk.Button(tool_bar, image = color_picker_icon)
color_btn.grid(row = 0, column = 5, padx = 3)

#Left Align
left_align_icon = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Left Align.png")
left_btn = ttk.Button(tool_bar, image = left_align_icon)
left_btn.grid(row = 0, column = 6, padx = 5)

#Center Align
center_align_icon = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Center Align.png")
center_btn = ttk.Button(tool_bar, image = center_align_icon)
center_btn.grid(row = 0, column = 7, padx = 3)

#Right Align
right_align_icon = tk.PhotoImage(file = r"E:\Projects\Python\Write Here\Write-Here\Icons\Right Align.png")
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

#Font Box and Font Size Functionality
current_font_family = 'Arial'
current_font_size = 12

def font_change(main_window):
    global current_font_family 
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def size_change(main_window):
    global current_font_size
    current_font_size = font_size.get()
    text_editor.configure(font=(current_font_family, current_font_size))

font_box.bind("<<ComboboxSelected>>", font_change)
font_size_box.bind("<<ComboboxSelected>>", size_change)

#Buttons Functionality

#Bold Button
def change_bold():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command = change_bold)

#Italics Button
def change_italics():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font = (current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font = (current_font_family, current_font_size, 'roman'))
italics_btn.configure(command = change_italics)

#Italics Button
def change_unedrline():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font = (current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font = (current_font_family, current_font_size, 'normal'))
underline_btn.configure(command = change_unedrline)

#font colour functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
color_btn.configure(command = change_font_color) 

#align buttons

#left align button
def left_align():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify = tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')
left_btn.configure(command = left_align)

#Center Align
def center_align():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify = tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')
center_btn.configure(command = center_align)

#Right Align
def right_align():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify = tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')
right_btn.configure(command = right_align)

text_editor.configure(font=('Arial',12))
#-------------------------------- Text Editor End -------------------------------------------

################################## Status Bar ##############################################
status_bar = ttk.Label(main_window, text = "Status Bar")
status_bar.pack(side = tk.BOTTOM)


text_changed = False
def changed(main_window):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text = f"Characters : {characters} | Words : {words}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", changed)
#-------------------------------- Status Bar End -------------------------------------------

################################## Main Menu Functionality ##############################################

## File Menu Functionality
#New file functionality
url = ""
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, 'end-1c')

#Open file functionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select File", filetypes = (('Text Files', '*.txt'), ("All Files", '*.*')))
    try:
        with open(url, "r") as file_read:
            text_editor.delete(1.0, 'end-1c')
            text_editor.insert(1.0, file_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main_window.title(os.path.basename(url))

#Save File Functionality
def save_file(event = None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes = (('Text Files', '*.txt'), ('All Files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return 

#Save As Functionality
def save_as_file(event = None):
    global url
    try:
        content = text_editor.get(1.0, 'end-1c')
        url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes = (('Text Files', '*.txt'), ('All Files', '*.*')))
        url.write(content)
        url.close()
    except:
        return

#Exit Functionality
def exit(event = None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning!', 'Do you want to save the file?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_window.destroy()
                else:
                    content2 = text_editor.get(1.0, tk.END)
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes = (('Text Files', '*.txt'), ('All Files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_window.destroy()
            else:
                main_window.destroy()
        else:
            main_window.destroy()
    except:
        return

#File Commands
file.add_command(label = 'New', image = New, compound = tk.LEFT, accelerator = 'Ctrl+N', command = new_file)
file.add_command(label = 'Open', image = Open, compound = tk.LEFT, accelerator = 'Ctrl+O', command  = open_file)
file.add_command(label = 'Save', image = Save, compound = tk.LEFT, accelerator = 'Ctrl+S', command = save_file)
file.add_command(label = 'Save As', image = SaveAs, compound = tk.LEFT, accelerator = 'Ctrl+Shift+S', command = save_as_file)
file.add_command(label = 'Exit', image = Exit, compound = tk.LEFT, accelerator = 'Ctrl+W', command = exit)

#Find Funtionality
def find_func(event=None):

    def find():
        word = find_entry.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground = 'red', background = 'yellow')
    
    def replace():
        word = find_entry.get()
        replace_text = replace_entry.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_window = tk.Tk()
    find_window.title("Find")
    find_window.geometry("365x150+500+200")
    find_window.resizable(0,0)

    #Find Label Frame
    find_frame = ttk.LabelFrame(find_window, text = "Find/Replace")
    find_frame.pack(pady=20)

    #Labels
    find_label = ttk.Label(find_frame, text = "Find : ")
    replace_label = ttk.Label(find_frame, text = "Replace : ")
   
    #Entry Box
    find_entry = ttk.Entry(find_frame, width = 30)
    replace_entry = ttk.Entry(find_frame, width = 30)

    #Buttons
    find_btn = ttk.Button(find_frame, text = "Find", command = find)
    replace_btn = ttk.Button(find_frame, text = "Replace", command = replace)

    #Grid
    find_label.grid(row = 0, column = 0, padx = 4, pady = 4)
    replace_label.grid(row = 1, column = 0, padx = 4, pady= 4)
    find_entry.grid(row = 0, column = 1, padx = 4, pady = 4)
    replace_entry.grid(row = 1, column = 1, padx = 4, pady = 4)
    find_btn.grid(row = 2, column = 0, padx = 8, pady = 4)
    replace_btn.grid(row = 2, column = 1, padx = 8, pady = 4)


    find_window.mainloop()


#Edit Commands
edit.add_command(label = 'Cut', image = Cut, compound = tk.LEFT, accelerator = 'Ctrl+X', command = lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label = 'Copy', image = copy, compound = tk.LEFT, accelerator = 'Ctrl+C', command = lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label = 'Paste', image = paste, compound = tk.LEFT, accelerator = 'Ctrl+V', command = lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label = 'Clear', image = clear, compound = tk.LEFT, accelerator = 'Ctrl+Shift+X', command = lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label = 'Find', image = find, compound = tk.LEFT, accelerator = 'Ctrl+F', command = find_func)

#View Commands

show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else :
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP, fill = tk.X)
        text_editor.pack(fill = tk.BOTH, expand = True)
        status_bar.pack(side = tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar :
        status_bar.pack_forget()
        show_statusbar = False
    else :
        status_bar.pack(side = tk.BOTTOM)
        show_statusbar = True

view.add_checkbutton(label = 'Toolbar', onvalue = True, offvalue = False, variable =  show_toolbar, image = toolbar, compound = tk.LEFT, command = hide_toolbar)
view.add_checkbutton(label = 'Status bar', onvalue = True, offvalue = False, variable =  show_statusbar, image = statusbar, compound = tk.LEFT, command = hide_statusbar)

#Theme Commands
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_colour, bg_colour = color_tuple[0], color_tuple[1]
    text_editor.config(background = bg_colour, fg = fg_colour)
count = 0
for i in color_dict:
    theme.add_radiobutton(label=i, image = colors[count], variable=theme_choice, compound = tk.LEFT, command = change_theme)
    count += 1

#About Functionality


#-------------------------------- Main Menu Functionality End -------------------------------------------

main_window.config(menu = main_menu)

#shortcut keys bind
main_window.bind("<Control-n>", new_file)
main_window.bind("<Control-o>", open_file)
main_window.bind("<Control-s>", save_file)
main_window.bind("<Control-Shift-s>", save_as_file)
main_window.bind("<Control-w>", exit)
main_window.bind("<Control-f>", find_func)


main_window.mainloop()