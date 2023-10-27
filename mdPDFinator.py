from markdown2 import markdown, markdown_path
from weasyprint import HTML, CSS
import fire

def md2pdf(md_file_path, pdf_file_path='output.pdf', css_file_path=None, new_page_char='---'):
	"""
	This converts markdown to pdf

	:param md_file_path: Path to the markdown file
	:type md_file_path: str
	:param pdf_file_path: Path to the output PDF file (it will not create a folder for you, make sure directory already exists)
	:type pdf_file_path: str
	:param css_file_path: Path to the CSS file
	:type css_file_path: str
	:param new_page_char: Character for new page
	:type new_page_char: str
	:return: Path of the converted PDF file
	:rtype: str
	"""

	extras = ['cuddled-lists', 'tables', 'footnotes', 'fenced-code-blocks']
	html_in_text = markdown_path(md_file_path, extras=extras)
	if new_page_char:
		page_break_char = markdown(new_page_char, extras=extras)
		html_in_text = html_in_text.replace(page_break_char, '<p style="page-break-before: always" ></p>')
	html_object = HTML(string=html_in_text)
	css = []
	if css_file_path:
		css.append(CSS(filename=css_file_path))
	html_object.write_pdf(pdf_file_path, stylesheets=css)

	return pdf_file_path

if __name__ == '__main__':
	fire.Fire(md2pdf)
