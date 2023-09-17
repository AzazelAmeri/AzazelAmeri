#-*-coding: gbk-*-
import unittest
import tempfile
from main import *

class TestPaperSimilarity(unittest.TestCase):
    def test_remove_punctuation(self):
        # ����ȥ�������ŵĺ���
        text_with_punctuation = "�������������     �ģ���ģ���  ��. ����!"
        expected_result = "����������������ĺð�����"
        result = remove_punctuation(text_with_punctuation)
        self.assertEqual(result, expected_result)

    def test_calculate_similarity(self):
        # ���Լ��������Եĺ���
        original_text = "������֣����ڲ��ԡ��������Ҳ���ڲ���,�������Ҳ���ڲ���,�������Ҳ���ڲ���"
        text_to_check = "�������, ���ڲ��ԡ��������Ҳ���ڲ���,�������Ҳ���ڲ���,�������Ҳ���ڲ���"
        expected_similarity = 1  # ʾ��ֵ
        similarity = calculate_similarity(original_text, text_to_check)
        self.assertAlmostEqual(similarity, expected_similarity, places=2)  # ���������ֵ�Ƿ�ӽ�����ֵ

if __name__ == '__main__':
    unittest.main()


