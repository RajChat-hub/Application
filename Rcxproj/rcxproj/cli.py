import argparse
from .parser import RCXProjParser
from .builder import RCXProjBuilder

def main():
    parser = argparse.ArgumentParser(description="rcxproj build system")
    parser.add_argument("command", help="Command to execute (build/clean/run)")
    parser.add_argument("--file", help="Path to the .rcxproj file", default="project.rcxproj")
    
    args = parser.parse_args()
    
    if args.command == "build":
        project_file = args.file
        rcx_parser = RCXProjParser(project_file)
        project_info = rcx_parser.parse()
        
        builder = RCXProjBuilder(project_info)
        builder.build()

if __name__ == "__main__":
    main()