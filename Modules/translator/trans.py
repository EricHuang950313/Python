from googletrans import Translator
translator = Translator()
translation = translator.translate("happy", dest="zh-tw")
print(translation.text)