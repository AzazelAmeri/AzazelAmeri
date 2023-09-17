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

    def test_read_file(self):
            # 创建临时文件以模拟输入文件
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(b"Hello, World!")
                file_content = read_file(temp_file.name)

                # 断言文件内容正确
                self.assertEqual(file_content, "Hello, World!")

            # 断言临时文件已被删除
            self.assertFalse(os.path.exists(temp_file.name))

    def test_read_nonexistent_file(self):
        # 测试读取不存在的文件是否引发异常
        with self.assertRaises(FileNotFoundError):
            read_file("nonexistent.txt")

    def test_tokenize_chinese_text(self):
        # 测试中文分词的函数
        chinese_text = "今天天气真好很适合去打球"
        expected_result = "今天天气 真好 很 适合 去 打球"
        result = tokenize_chinese_text(chinese_text)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()


