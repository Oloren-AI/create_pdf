import oloren as olo
import sys
import io

@olo.register()
def hello():
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Hello World!')
    pdf.output('tuto1.pdf', 'F')
    
    return olo.OutputFile("tuto1.pdf")

@olo.register(description="""
This function takes a list of 'pages', where each 'page' is a list of 'cells'. Each 'cell' is a dictionary of parameters that specify its properties. The function generates a PDF with the given configuration. The cells on a page are processed from top to bottom, and pages are processed in the order they appear in the list. 

Each 'cell' dictionary can include the following properties:

'w' (width): Cell width. If None or 0, the cell extends up to the right margin.

'h' (height): Cell height. If None, the height is equal to the current font size.

'txt' (text): String to print. 

'border': Indicates if borders must be drawn around the cell. 

'align': Sets text alignment inside the cell. Possible values are 'L' (left align), 'C' (center), and 'R' (right align).

'font_family': Font family. Can be 'Courier', 'Helvetica', 'Arial', 'Times', 'Symbol', 'ZapfDingbats' or a name defined by add_font.

'font_style': Font style. Possible values are 'B' (bold), 'I' (italic), 'U' (underline), and empty string (regular).

'font_size': Font size. 

Please note that all parameters are optional, and will use default values if not provided.
""")
def create_text_pdf(pages = olo.Json()):
    from fpdf import FPDF

    pdf = FPDF()
    
    for page in pages:
        pdf.add_page()
        for cell in page:
            # Extract cell parameters
            w = cell.get('w', 0)
            h = cell.get('h', pdf.font_size)
            txt = cell.get('txt', '')
            border = cell.get('border', 0)
            align = cell.get('align', 'L')
            font_family = cell.get('font_family', 'Arial')
            font_style = cell.get('font_style', '')
            font_size = cell.get('font_size', 16)
            link = cell.get('link', '')
            fill = cell.get('fill', False)
            
            # Set font for each cell
            pdf.set_font(family=font_family, style=font_style, size=font_size)
            
            # Write cell content
            pdf.multi_cell(w, h, txt, border, align, fill, link)
            
    output_filename = "generated_pdf.pdf"
    pdf.output(output_filename, 'F')
    
    return olo.OutputFile(output_filename)

if __name__ == "__main__":
    olo.run("createpdf", port=80)