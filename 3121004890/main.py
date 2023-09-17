#-*-coding: gbk-*-
import sys
import jieba
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def remove_punctuation(text):
    #��������ȥ��
    translator = str.maketrans('', '', string.printable)
    # ʹ��ӳ���ȥ��������
    text_without_punctuation = text.translate(translator)
    return text_without_punctuation

def read_file(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as e:
        print(f"File not found: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

def tokenize_chinese_text(text):
    seg_list = jieba.cut(text)
    # ���ִʽ��ת��Ϊ�ַ���
    return " ".join(seg_list)

def calculate_similarity(original_text, text_to_check):
    # ʹ��TF-IDF�������ı�
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([original_text, text_to_check])   
    # ��������������
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    # ����������,����С�������λ
    return round(similarity,2)

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <original_file.txt> <file_to_check.txt> <output_file.txt>")
        sys.exit(1)
    jieba.initialize()
    original_file = sys.argv[1]
    file_to_check=sys.argv[2]
    output_file=sys.argv[3]
    original_text=read_file(original_file)
    text_to_check=read_file(file_to_check)
    original_text_processed=remove_punctuation(original_text)
    text_to_check_processed=remove_punctuation(text_to_check)
    original_text_segmented = tokenize_chinese_text(original_text_processed)
    text_to_check_segmented = tokenize_chinese_text(text_to_check_processed)
    similarity = calculate_similarity(original_text_segmented, text_to_check_segmented)

    with open(output_file, 'w') as output_file:
        output_file.write(str(similarity))
    print(similarity)

if __name__=='__main__':
    main()