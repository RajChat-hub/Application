import unittest
from rcxproj.parser import RCXProjParser

class TestParser(unittest.TestCase):
    def test_parse_project(self):
        parser = RCXProjParser("project.rcxproj")
        project_info = parser.parse()
        
        self.assertIn('src/main.cpp', project_info['sources'])
        self.assertEqual(project_info['output_dir'], './bin/')

if __name__ == '__main__':
    unittest.main()