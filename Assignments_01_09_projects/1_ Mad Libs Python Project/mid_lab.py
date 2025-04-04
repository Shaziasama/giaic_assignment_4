import tkinter as tk
from tkinter import ttk, messagebox
import random

class MadLibsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Creative Mad Libs ✨")
        self.root.geometry("800x600")
        self.root.configure(bg="#2C3E50")  # Dark blue background
        
        # Custom styles for widgets
        style = ttk.Style()
        style.configure("Custom.TCombobox",
                       background="#34495E",
                       fieldbackground="#34495E",
                       foreground="white",
                       arrowcolor="white")
        
        # Mad Libs templates
        self.templates = {
            "All About Me 🌟": {
                "template": "Hi! My name is {name}! My favorite color is {color} and I love eating {food}. "
                           "When I'm not playing {game}, you can find me hanging out at {place}. "
                           "My best friend says I'm very {adjective}! If I could have any superpower, "
                           "I would want to {verb}. My dream job is to be a {profession}!",
                "words": ["name", "color", "food", "game", "place", "adjective", "verb", "profession"]
            },
            "Dream Day ⭐": {
                "template": "My perfect day starts with eating {food} for breakfast. I'd wear my favorite {color} "
                           "outfit and go to {place} with my {adjective} friend. We'd play {game} all day long "
                           "and I'd become a famous {profession}. At night, I would {verb} under the stars!",
                "words": ["food", "color", "place", "adjective", "game", "profession", "verb"]
            },
            "Future Me 🔮": {
                "template": "In 10 years, I'll be living in {place}, working as a {profession}. "
                           "I'll have a {color} house and eat {food} every day. My hobby will be to {verb} "
                           "and I'll still love playing {game}. Everyone will know me as the {adjective} one!",
                "words": ["place", "profession", "color", "food", "verb", "game", "adjective"]
            }
        }

        self.create_widgets()

    def create_widgets(self):
        # Title with gradient effect
        title_frame = tk.Frame(self.root, bg="#2C3E50")
        title_frame.pack(pady=20)
        
        title_label = tk.Label(title_frame, 
                              text="✨ Magical Mad Libs ✨", 
                              font=("Helvetica", 32, "bold"),
                              bg="#2C3E50",
                              fg="#ECF0F1")
        title_label.pack()
        
        subtitle = tk.Label(title_frame,
                          text="Create your own wild stories!",
                          font=("Helvetica", 14, "italic"),
                          bg="#2C3E50",
                          fg="#BDC3C7")
        subtitle.pack(pady=5)

        # Template selection with custom styling
        select_frame = tk.Frame(self.root, bg="#2C3E50")
        select_frame.pack(pady=10)
        
        tk.Label(select_frame,
                text="Choose your adventure:",
                font=("Helvetica", 12, "bold"),
                bg="#2C3E50",
                fg="#ECF0F1").pack(side=tk.LEFT, padx=5)
        
        self.template_var = tk.StringVar()
        template_combo = ttk.Combobox(select_frame,
                                    textvariable=self.template_var,
                                    values=list(self.templates.keys()),
                                    state="readonly",
                                    width=25,
                                    style="Custom.TCombobox")
        template_combo.pack(side=tk.LEFT, padx=5)
        template_combo.set("All About Me 🌟")
        template_combo.bind("<<ComboboxSelected>>", self.start_new_game)

        # Main content frame
        self.content_frame = tk.Frame(self.root, bg="#2C3E50")
        self.content_frame.pack(pady=20, expand=True, fill="both")

        # Start the game
        self.start_new_game()

    def start_new_game(self, event=None):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        selected_template = self.template_var.get()
        self.current_template = self.templates[selected_template]
        self.word_entries = {}

        # Create scrollable input frame
        canvas = tk.Canvas(self.content_frame, bg="#2C3E50", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical", command=canvas.yview)
        input_frame = tk.Frame(canvas, bg="#2C3E50")

        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True, padx=20)
        
        # Create window in canvas
        canvas_frame = canvas.create_window((0, 0), window=input_frame, anchor="nw")

        # Configure canvas scrolling
        def configure_scroll(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        input_frame.bind("<Configure>", configure_scroll)

        # Create input fields with modern styling
        for i, word_type in enumerate(self.current_template["words"]):
            frame = tk.Frame(input_frame, bg="#34495E", padx=10, pady=5)
            frame.pack(fill="x", pady=5)

            label = tk.Label(frame,
                           text=f"Enter a {word_type.replace('_', ' ')}:",
                           font=("Helvetica", 10, "bold"),
                           bg="#34495E",
                           fg="#ECF0F1")
            label.pack(anchor="w")
            
            entry = tk.Entry(frame,
                           width=30,
                           font=("Helvetica", 12),
                           bg="#ECF0F1",
                           fg="#2C3E50",
                           relief="flat")
            entry.pack(pady=2)
            self.word_entries[word_type] = entry

        # Generate button with hover effect
        generate_button = tk.Button(self.content_frame,
                                  text="✨ Generate Magic! ✨",
                                  command=self.generate_story,
                                  font=("Helvetica", 14, "bold"),
                                  bg="#E74C3C",
                                  fg="white",
                                  padx=30,
                                  pady=15,
                                  relief="flat",
                                  cursor="hand2")
        generate_button.pack(pady=20)

        # Hover effects for button
        def on_enter(e):
            generate_button['bg'] = '#C0392B'
        def on_leave(e):
            generate_button['bg'] = '#E74C3C'
            
        generate_button.bind("<Enter>", on_enter)
        generate_button.bind("<Leave>", on_leave)

    def generate_story(self):
        # Collect all words
        words = {}
        for word_type, entry in self.word_entries.items():
            word = entry.get().strip()
            if not word:
                messagebox.showwarning("Missing Words", f"Please enter a {word_type.replace('_', ' ')}!")
                return
            words[word_type] = word

        # Generate the story
        story = self.current_template["template"]
        for word_type, word in words.items():
            story = story.replace("{" + word_type + "}", word)

        # Show the result in a styled window
        result_window = tk.Toplevel(self.root)
        result_window.title("Your Magical Story")
        result_window.geometry("500x400")
        result_window.configure(bg="#34495E")

        # Add some decoration
        tk.Label(result_window,
                text="✨ Your Magical Creation ✨",
                font=("Helvetica", 20, "bold"),
                bg="#34495E",
                fg="#ECF0F1").pack(pady=15)

        # Story display with custom styling
        story_frame = tk.Frame(result_window, bg="#2C3E50", padx=20, pady=20)
        story_frame.pack(padx=20, pady=10, fill="both", expand=True)

        story_text = tk.Text(story_frame,
                           wrap=tk.WORD,
                           width=40,
                           height=10,
                           font=("Helvetica", 12),
                           bg="#ECF0F1",
                           fg="#2C3E50",
                           padx=15,
                           pady=15)
        story_text.pack(expand=True, fill="both")
        story_text.insert("1.0", story)
        story_text.config(state="disabled")

        # Styled button
        new_story_btn = tk.Button(result_window,
                                text="Create Another Story",
                                command=result_window.destroy,
                                font=("Helvetica", 12, "bold"),
                                bg="#E74C3C",
                                fg="white",
                                padx=20,
                                pady=10,
                                relief="flat",
                                cursor="hand2")
        new_story_btn.pack(pady=15)

        # Hover effects
        def on_enter(e):
            new_story_btn['bg'] = '#C0392B'
        def on_leave(e):
            new_story_btn['bg'] = '#E74C3C'
            
        new_story_btn.bind("<Enter>", on_enter)
        new_story_btn.bind("<Leave>", on_leave)

if __name__ == "__main__":
    root = tk.Tk()
    app = MadLibsGame(root)
    root.mainloop()    