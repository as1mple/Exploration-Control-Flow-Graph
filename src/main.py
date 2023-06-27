from staticfg import CFGBuilder

NAME_OBJECT = "example"
PATH_TO_FILE = "src/example.py"

NAME_RESULT_FILE = "example"
FORMAT_RESULT_FILE = "png"

if __name__ == "__main__":
    cfg = CFGBuilder().build_from_file(NAME_OBJECT, PATH_TO_FILE)
    cfg.build_visual(NAME_RESULT_FILE, FORMAT_RESULT_FILE)
