from googletrans import Translator

translator = Translator()

chosen_lang = input("enter the language you want to translate to: ")

chosen_lang = chosen_lang.strip().lower()

languages = {"afrikaans":"af", "albanian": "sq", "amharic":"am", "arabic":"ar", "armenian":"hy", "azerbaijani":"az", "basque":"eu", "belarusian":"be", "bengali":"bn", "bosnian":"bs", "bulgarian":"bg", "catalan":"ca", "cebuano":"ceb", "chichewa":"ny", "chinese traditional": "zh-tw", "chinese simplified": "zh-cn", "corsican":"co", "croatian":"hr", "czech":"cs", "danish":"da", "dutch":"nl", "english":"en", "esperanto":"eo", "filipino":"tl", "estonian":"et", "finnish":"fi", "french":"fr", "frisian":"fy", "galician":"gl", "georgian":"ka", "german":"de", "greek":"el", "gujarati":"gu", "haitian creole": "ht", "hausa":"ha", "hawaiian":"haw", "hebrew":"he", "hindi":"hi", "hmong":"hmn", "hungarian":"hu", "icelandic":"is", "igbo":"ig", "indonesian":"id", "irish":"ga", "italian":"it", "japanese":"ja", "javanese":"jw", "kannada":"kn", "kazakh":"kk", "khmer":"kh", "korean":"ko", "kurdish":"ku", "kyrgyz":"ky", "lao":"lo", "latin":"la", "latvian":"lv", "lithuanian":"lt", "louxembourgish":"lb", "macedonian":"mk", "malagasy":"mg", "malay":"ms", "malayalam":"ml", "maltese":"mt", "maori":"mi", "marathi": "mi", "mongolian":"mn", "myanmar":"me", "norwegian":"no", "nepali":"ne", "odia":"or", "pashto":"ps", "persian":"fa", "polish":"pl", "portugese":"pt", "punjabi":"pa", "romanian":"ro", "russian":"ru", "samoan":"sm", "scots gaelic":"gd", "serbian":"sr", "sesotho":"st", "shona":"sn", "sindhi":"sd", "sinhala":"si", "slovak":"sk", "slovenian":"sl", "somali":"so", "spanish":"es", "sudanese":"su", "swhili":"sw", "swedish":"sv", "tajik":"tg", "tamil":"ta", "telugu":"te", "thai":"th", "turkish":"tr", "ukrainian":"uk", "urdu":"ur", "uyghur":"ug", "uzbek":"uz", "vietnamese":"vi", "welsh":"cy", "xhosa":"xh", "yiddish":"yi", "yoruba":"yo", "zulu":"zu"}

for each_lang in languages.keys():
    if chosen_lang == each_lang:
        lang_abbrev = languages[each_lang]
        break
    
input_text = input("\nenter the text you want to translate: ")

print("\ntranslating...\n")

print(translator.translate(input_text, dest=lang_abbrev).text)