import unittest
from rcxproj.builder import RCXProjBuilder

class TestBuilder(unittest.TestCase):
    def test_build(self):
        project_info = {
            'sources': ['src/main.cpp', 'src/utils.cpp'],
            'output_dir': './bin/',
            'target_type': 'Application'
        }
        builder = RCXProjBuilder(project_info)
        result = builder.build()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()