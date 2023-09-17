#-*-coding: gbk-*-
import unittest
import tempfile
from main import *

class TestPaperSimilarity(unittest.TestCase):
    def test_remove_punctuation(self):
        # 测试去除标点符号的函数
        text_with_punctuation = "今天的天气是真     的，真的，好  啊. 哈哈!"
        expected_result = "今天的天气是真的真的好啊哈哈"
        result = remove_punctuation(text_with_punctuation)
        self.assertEqual(result, expected_result)

    def test_calculate_similarity(self):
        # 测试计算相似性的函数
        original_text = "这段文字，用于测试。这段文字也用于测试,这段文字也用于测试,这段文字也用于测试"
        text_to_check = "这段文字, 用于测试。这段文字也用于测试,这段文字也用于测试,这段文字也用于测试"
        expected_similarity = 1  # 示例值
        similarity = calculate_similarity(original_text, text_to_check)
        self.assertAlmostEqual(similarity, expected_similarity, places=2)  # 检查相似性值是否接近期望值

if __name__ == '__main__':
    unittest.main()


