# # import nltk
# # from nltk.tokenize import word_tokenize, sent_tokenize
import matplotlib.pyplot as plt
import numpy as np
# # Task 72: Split text into a list of words
# # text = "NLTK is a leading platform for building Python programs to work with human language data."
# # words = word_tokenize(text)
# # print("DEBUG: Split text into words")
# # print(f"Words: {words}")

# # # Task 73: Tokenize words sentence-wise
# # paragraph = "NLTK is great for natural language processing. It supports tokenization and other NLP tasks."
# # sentences = sent_tokenize(paragraph)
# # print("DEBUG: Tokenized text into sentences and words")
# # for i, sentence in enumerate(sentences):
# #     print(f"Sentence {i + 1}: {sentence}")
# #     print(f"Words: {word_tokenize(sentence)}")

# # Task 74: Plot two or more lines with legends
# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]  # Square values
# y2 = [1, 8, 27, 64, 125]  # Cube values

# plt.plot(x, y1, label='Square')
# plt.plot(x, y2, label='Cube')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Square and Cube Values')
# plt.legend()
# print("DEBUG: Plotting square and cube values")
# plt.show()



# math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
# science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
# plt.scatter(math_marks, science_marks, color='red', label='Marks')
# plt.xlabel('Math Marks')
# plt.ylabel('Science Marks')
# plt.title('Scatter Plot of Math vs Science Marks')
# plt.legend()
# print("DEBUG: Displaying scatter plot for math and science marks")
# plt.show()



# groups = ["Group1", "Group2", "Group3", "Group4", "Group5"]
# men_means = [22, 30, 35, 35, 26]
# women_means = [25, 32, 30, 35, 29]
# x = np.arange(len(groups))  # Group locations
# width = 0.35  # Bar width

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, men_means, width, label='Men', color='blue')
# rects2 = ax.bar(x + width/2, women_means, width, label='Women', color='pink')

# ax.set_xlabel('Groups')
# ax.set_ylabel('Scores')
# ax.set_title('Scores by Group and Gender')
# ax.set_xticks(x)
# ax.set_xticklabels(groups)
# ax.legend()

# print("DEBUG: Displaying grouped bar chart for scores by gender")
# plt.show()




programming_languages=[' Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity= [22.2, 17.6, 8.8, 8, 7.7, 6.7]


plt.pie(popularity, labels=programming_languages ,autopct='%1.1f%%')
plt.show()