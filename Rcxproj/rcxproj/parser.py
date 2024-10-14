import xml.etree.ElementTree as ET

class RCXProjParser:
    def __init__(self, project_file):
        self.project_file = project_file

    def parse(self):
        tree = ET.parse(self.project_file)
        root = tree.getroot()
        
        # Extract relevant information
        sources = []
        for file in root.findall(".//File"):
            sources.append(file.get('Include'))
        
        return {
            'sources': sources,
            'output_dir': root.findtext(".//OutputDirectory"),
            'target_type': root.findtext(".//TargetType"),
        }