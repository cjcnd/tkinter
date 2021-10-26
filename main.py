from tkinter import *

root = Tk()
root.title("GUI")

file_frame = Frame(root)
file_frame.pack()


def delete():
    pass


def file_plus():
    pass


btn_add_file = Button(file_frame, text="파일 추가", padx=5, pady=5)
btn_add_file.pack(side="left")

btn_delete_file = Button(file_frame, text="선택삭제", padx=5, pady=5)
btn_delete_file.pack(side="right")

list_frame = Frame(root)
list_frame.pack()

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

path_frame = LabelFrame(root, text="저장경로")
path_frame.pack()

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right")

root.resizable(False, False)
root.mainloop()
