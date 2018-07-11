import chardet

def input_text_data(str_file_name):
    with open(str_file_name, 'rb') as f:
        txt_fr = f.read()
        encod = chardet.detect(txt_fr)
        s = txt_fr.decode(encod['encoding'])
    return s

def output_text_data(str_file_name, text):
    with open(str_file_name, 'w', encoding='utf-8') as f:
        f.write(text)
