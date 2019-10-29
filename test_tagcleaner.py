import unittest
import tagcleaner
import os
import filecmp

class Test_tag(unittest.TestCase):
    def test_cleaner(self):
        self.assertFalse(os.path.exists("html.txt"))
   
    def test_cleaner_2(self):
        self.assertFalse(filecmp.cmp("/home/luisfilho/semantix/GITS/desafio_tag_HTML/git_tag/html.txt", "/home/luisfilho/semantix/GITS/desafio_tag_HTML/git_tag/mock01.txt"))

if __name__ == "__main__":
    unittest.main()
  
    
    
