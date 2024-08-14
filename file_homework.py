
import tkinter as tk
from tkinter import messagebox
import os

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("400x500+220+100")
        # Define file paths as a list of strings
        self.file_paths = [f"text_file_{i}.txt" for i in range(1, 7)]
        # Create buttons individually
        self.create_buttons()

    def create_buttons(self):
        # Create buttons individually without using a loop
        self.create_button("Home Work Function", self.file_paths[0])
        self.create_button("Button_Home_Work_2", self.file_paths[1])
        self.create_button("Button_Home_Work_3", self.file_paths[2])
        self.create_button("Button_Home_Work_4", self.file_paths[3])
        self.create_button("Button_Home_Work_5", self.file_paths[4])
        self.create_button("Button_Home_Work_6", self.file_paths[5])

    def create_button(self, text, file_path):
        button = tk.Button(self.root, text=text, background="Green",font=30, command=lambda p=file_path: self.open_text_editor(p))
        button.pack(padx=10, pady=10, expand=True)

    def open_text_editor(self, file_path):
        editor_window = tk.Toplevel(self.root)
        editor_window.title(f"Edit Text - {file_path}")
        editor_window.geometry("900x500+300+200")
        
        # Create a frame to hold the text area and scrollbar
        frame = tk.Frame(editor_window)
        frame.pack(expand=1, fill=tk.BOTH)
        
        # Create the text area with scrollbar
        text_area = tk.Text(frame, wrap=tk.WORD, font=("Arial", 12))
        text_area.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_area.config(yscrollcommand=scrollbar.set)
        
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text_area.insert(tk.END, file.read())
            except Exception as e:
                messagebox.showerror("File Error", f"Error reading file: {e}")

        save_button = tk.Button(editor_window, text="Save", background="red", command=lambda: self.save_text(file_path, text_area))
        save_button.pack(pady=10, expand=True, fill="both")

    def save_text(self, file_path, text_area):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text_area.get("1.0", tk.END).strip())
            messagebox.showinfo("Save File", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("File Error", f"Error saving file: {e}")

def main():
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


