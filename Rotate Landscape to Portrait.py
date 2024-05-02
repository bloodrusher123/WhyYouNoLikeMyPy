import PyPDF2
 
pdf_in = open('C:\\Users\\jbateman\\Downloads\\PUPTest.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_in)
pdf_writer = PyPDF2.PdfWriter()
 
for pagenum in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[pagenum]
    rotation_angle = page.get('/Rotate')
    mediaBox = page.mediabox
    if mediaBox.right > 600:
        page.rotate(90)
        #print('Landscape')
    pdf_writer.add_page(page)
 
pdf_out = open('C:\\Users\\jbateman\\Downloads\\rotated.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()