import arabic_reshaper
from bidi.algorithm import get_display

# 1. بنعمل الاختصار بتاعنا مرة واحدة بس فوق
def print_ar(text):
    reshaped_text = arabic_reshaper.reshape(text)
    final_text = get_display(reshaped_text)
    print(final_text)

# --------------------------------------------------

# 2. دلوقتي تقدر تطبع أي جملة عربي في سطر واحد بس براحتك!
print_ar("السلام عليكم")
print_ar("أهلاً بيك في عالم البرمجة")
print_ar("الموضوع طلع بسيط جداً")
