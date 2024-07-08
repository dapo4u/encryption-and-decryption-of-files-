import PyPDF2
from tkinter import Tk, filedialog, simpledialog, messagebox

def password_protect_pdf(input_pdf_path, output_pdf_path, password):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_pdf_file:
        pdf_reader = PyPDF2.PdfReader(input_pdf_file)
        
        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Add all pages to the writer
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Encrypt the PDF with the password
        pdf_writer.encrypt(password)

        # Write the output PDF file
        with open(output_pdf_path, 'wb') as output_pdf_file:
            pdf_writer.write(output_pdf_file)

# Create a Tkinter root window (it will be hidden)
root = Tk()
root.withdraw()

# Ask the user to select the input PDF file
input_pdf_path = filedialog.askopenfilename(title="Select PDF file to password protect", filetypes=[("PDF files", "*.pdf")])

if input_pdf_path:
    # Ask the user for the output PDF file path
    output_pdf_path = filedialog.asksaveasfilename(title="Save password protected PDF as", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    if output_pdf_path:
        # Ask the user for the password
        password = simpledialog.askstring("Password", "Enter password to protect the PDF:", show='*')

        if password:
            # Protect the PDF with the password
            password_protect_pdf(input_pdf_path, output_pdf_path, password)
            messagebox.showinfo("Success", "The PDF has been password protected successfully!")
        else:
            messagebox.showwarning("Warning", "No password entered. Operation cancelled.")
    else:
        messagebox.showwarning("Warning", "No output file selected. Operation cancelled.")
else:
    messagebox.showwarning("Warning", "No input file selected. Operation cancelled.")
