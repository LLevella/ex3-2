import chardet

def input_text_data(str_file_name):
    with open(str_file_name, 'r') as f:
        txt = f.read()
    return txt

def output_text_data(str_file_name, text):
    with open(str_file_name, 'w') as f:
        f.write(text)
