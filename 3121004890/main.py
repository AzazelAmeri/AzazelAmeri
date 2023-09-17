#-*-coding: gbk-*-
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_file(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        return file.read()

def calculate_similarity(original_text, text_to_check):
    vectorizer = TfidfVectorizer()#文本向量化
    tfidf_matrix = vectorizer.fit_transform([original_text, text_to_check])   
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]# 计算余弦相似性
    return similarity

if __name__=='__main__':
    original_file = sys.argv[1]
    file_to_check=sys.argv[2]
    output_file=sys.argv[3]
    original_text=read_file(original_file)
    text_to_check=read_file(file_to_check)
    similarity = calculate_similarity(original_text, text_to_check)

    with open(output_file, 'w') as output_file:
        output_file.write(str(similarity))