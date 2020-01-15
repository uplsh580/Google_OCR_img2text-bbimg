import utility.gcp_ocr_utility as gocr
import os
import argparse
import glob

#basic path
input_path="./input/*"
output_path="./output"

parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

'''
Command line options
'''
parser.add_argument(
    '-img_path', type=str, default=input_path,
    help='path to image directory path'
)
parser.add_argument(
    '-output_path', type=str, default=output_path,
    help='path to ouput'
)

parser.add_argument(
    '--blocks', default=False, action="store_true",
    help='Draw block boxes line'
)
parser.add_argument(
    '--paragraphs', default=False, action="store_true",
    help='Draw block boxes line'
)
parser.add_argument(
    '--words', default=False, action="store_true",
    help='Draw block boxes line'
)
parser.add_argument(
    '--symbols', default=False, action="store_true",
    help='Draw block boxes line'
)
parser.add_argument(
    '--txt', default=False, action="store_true",
    help='make result text file'
)
FLAGS = parser.parse_args()

img_num = 0
print("===========================================")
for img_file in glob.iglob(input_path, recursive=True):
    img_num += 1
    print ("# of img : ", img_num)
    print("Input img : ", img_file)
    response = gocr.gcv_detect_text(img_file)
    text_info = gocr.get_text_info(response)

    if (FLAGS.blocks | FLAGS.paragraphs | FLAGS.words | FLAGS.symbols):
        gocr.save_bbox_img(img_file, text_info, output_path, draw_blocks=FLAGS.blocks, draw_paragraphs=FLAGS.paragraphs, 
                            draw_words=FLAGS.words, draw_symbols=FLAGS.symbols)

    if FLAGS.txt:
        gocr.save_text_info(img_file, text_info, output_path)
    print("===========================================")
print("Total # of img : ", img_num)
print("Program Finish~!")


