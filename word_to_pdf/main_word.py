import sys
import os
import comtypes.client

wdFormatPDF = 17




def make_pdf(in_path,out_path):
    in_file = os.path.abspath(in_path)
    out_file = os.path.abspath(out_path)

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()
    print(out_path + " make success.....")



if __name__ == '__main__':
    # in_file = os.path.abspath(sys.argv[1])
    # out_file = os.path.abspath(sys.argv[2])
    in_path = ".\\word"
    # out_path = "C:\\Users\\rango\\Documents\\code\\pdf2word\\pdf\\abc.pdf"
    out_path = ".\\pdf"

    for file in os.listdir(in_path):
        file_name = os.path.splitext(file)[0]
        extension_name = os.path.splitext(file)[1]
        if extension_name == '.docx' or extension_name == "doc":
            make_pdf(in_path+"\\"+file_name+extension_name,out_path+"\\"+file_name+".pdf")
