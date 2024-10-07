from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import *
import pyperclip

root = Tk()
root.title("py_translator")
root.geometry("400x300")

# when submit is pressed, user input stored
def handle_input():
    global user_input
    user_input = entry.get()

label = Label(root, text="Enter text:")
label.grid(row=0, column=0)

entry = Entry(root, width=50)
entry.grid(row=1, column=0, padx=10)

submit_b1 = Button(root, text="Submit", command=handle_input, width=7)
submit_b1.grid(row=1, column=1, padx=5)

languages = {"afrikaans":"af", "albanian": "sq", "amharic":"am", "arabic":"ar", "armenian":"hy", "azerbaijani":"az", "basque":"eu", "belarusian":"be", "bengali":"bn", "bosnian":"bs", "bulgarian":"bg", "catalan":"ca", "cebuano":"ceb", "chichewa":"ny", "chinese traditional": "zh-tw", "chinese simplified": "zh-cn", "corsican":"co", "croatian":"hr", "czech":"cs", "danish":"da", "dutch":"nl", "english":"en", "esperanto":"eo", "filipino":"tl", "estonian":"et", "finnish":"fi", "french":"fr", "frisian":"fy", "galician":"gl", "georgian":"ka", "german":"de", "greek":"el", "gujarati":"gu", "haitian creole": "ht", "hausa":"ha", "hawaiian":"haw", "hebrew":"he", "hindi":"hi", "hmong":"hmn", "hungarian":"hu", "icelandic":"is", "igbo":"ig", "indonesian":"id", "irish":"ga", "italian":"it", "japanese":"ja", "javanese":"jw", "kannada":"kn", "kazakh":"kk", "khmer":"kh", "korean":"ko", "kurdish":"ku", "kyrgyz":"ky", "lao":"lo", "latin":"la", "latvian":"lv", "lithuanian":"lt", "louxembourgish":"lb", "macedonian":"mk", "malagasy":"mg", "malay":"ms", "malayalam":"ml", "maltese":"mt", "marathi": "mi", "mongolian":"mn", "myanmar":"me", "norwegian":"no", "nepali":"ne", "odia":"or", "pashto":"ps", "persian":"fa", "polish":"pl", "portugese":"pt", "punjabi":"pa", "romanian":"ro", "russian":"ru", "samoan":"sm", "scots gaelic":"gd", "serbian":"sr", "sesotho":"st", "shona":"sn", "sindhi":"sd", "sinhala":"si", "slovak":"sk", "slovenian":"sl", "somali":"so", "spanish":"es", "sudanese":"su", "swhili":"sw", "swedish":"sv", "tajik":"tg", "tamil":"ta", "telugu":"te", "thai":"th", "turkish":"tr", "ukrainian":"uk", "urdu":"ur", "uyghur":"ug", "uzbek":"uz", "vietnamese":"vi", "welsh":"cy", "xhosa":"xh", "yiddish":"yi", "yoruba":"yo", "zulu":"zu"}

variable = tk.StringVar(root)
variable.set(languages["chinese simplified"])

label2 = Label(root, text="Translate to:")
label2.grid(row=3, column=0)

opt = tk.OptionMenu(root, variable, *languages)
opt.config(width=44)
opt.grid(row=4, column=0, padx=0)

def find_abbrev():
    chosen_lang = variable.get()
    for each_lang in languages.keys():
        if chosen_lang == each_lang:
            global lang_abbrev
            lang_abbrev = languages[each_lang]
            break
    
submit_b2 = Button(root, text="Select", command=find_abbrev, width=7)
submit_b2.grid(row=4, column=1, padx=5)

result = ""
def translate():
    global result
    result = GoogleTranslator(source='auto', target=lang_abbrev).translate(user_input)
    T.delete(1.0, tk.END)
    T.insert(tk.END, result)
    
T = Text(root, height=7, width=38)
T.grid(row=5, column=0, padx=10, pady=20)

def copy_to_clipboard():
    pyperclip.copy(T.get(1.0, "end-1c"))

submit_b4 = Button(root, text="Translate", command=translate, width=25)
submit_b4.grid(row=6, column=0 , padx=5)

submit_b5 = Button(root, text="Copy", command=copy_to_clipboard, width=7)
submit_b5.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
