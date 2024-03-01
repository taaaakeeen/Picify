import os
from pathlib import Path
from pdf2image import convert_from_path

poppler_dir = Path(__file__).parent.absolute() / 'poppler_v24.02.0/Library/bin'
os.environ["PATH"] += os.pathsep + str(poppler_dir)

def pdf_to_img(input_file_path, save_dir_path, output_dpi):
    pdf_file_name = os.path.splitext(os.path.basename(input_file_path))[0]
    fmt = 'jpeg'
    pages = convert_from_path(input_file_path, fmt=fmt, dpi=output_dpi)
    for i, page in enumerate(pages):
        page_num = str(i+1).zfill(3)
        file_name = f'{pdf_file_name}_{output_dpi}dpi_{page_num}.{fmt}'
        output_file_path = os.path.join(save_dir_path, file_name)
        print(output_file_path)
        page.save(output_file_path, fmt)

if __name__ == '__main__':

    input_file_path = 'pdf/recipe.pdf'
    save_dir_path = 'img'
    output_dpi = 600
    pdf_to_img(input_file_path, save_dir_path, output_dpi)