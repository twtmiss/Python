from wordcloud import WordCloud
import cv2
import jieba
import matplotlib.pyplot as plt
 
with open('F:/520/520.txt', 'r') as f:
    text = f.read()
 
cut_text = " ".join(jieba.cut(text))
print(cut_text)
color_mask = cv2.imread("F:/520/mask.jpg")
 
a520cloud = WordCloud(
    font_path=" C:\\Windows\\Fonts\\simkai.ttf",
    background_color='white',
    mask=color_mask,
    max_words=100,
    max_font_size=40
)
 
a520cloud = a520cloud.generate(cut_text)
a520cloud.to_file('F:/520/cloud.jpg')
 
plt.imshow(a520cloud, interpolation='bilinear')
plt.axis('off')
plt.show()
