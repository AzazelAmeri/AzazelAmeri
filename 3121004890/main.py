#-*-coding: gbk-*-
import sys
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_file(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        return file.read()

def tokenize_chinese_text(text):
    seg_list = jieba.cut(text, cut_all=False)
    print(seg_list)
    # 将分词结果转换为字符串
    return " ".join(seg_list)

def calculate_similarity(original_text, text_to_check):
    # 使用TF-IDF向量化文本
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([original_text, text_to_check])
    
    # 计算余弦相似性
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

    # 返回相似性的数值
    return round(similarity,2)


if __name__=='__main__':
    jieba.initialize()
    original_file = sys.argv[1]
    file_to_check=sys.argv[2]
    output_file=sys.argv[3]
    original_text=read_file(original_file)
    text_to_check=read_file(file_to_check)
    original_text_segmented = tokenize_chinese_text(original_text)
    text_to_check_segmented = tokenize_chinese_text(text_to_check)
    similarity = calculate_similarity(original_text, text_to_check)

    #with open(output_file, 'w') as output_file:
    #    output_file.write(str(similarity))
    print(similarity)