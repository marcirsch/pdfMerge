from glob import glob
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class PDFMerge:
    filesToMerge = []
    outputFile = './result.pdf'

    def merge_pdfs(self, files):
        ''' Merges all the pdf files in current directory '''
        merger = PdfMerger()
        [merger.append(pdf) for pdf in files]
        with open(self.outputFile, "wb") as new_file:
            merger.write(new_file)

    def select_pdfs(self):
        filetypes = (
            ('PDF files', '*.pdf'),
            ('All files', '*.*')
        )

        filenames = fd.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=filetypes)

        print("Selected files: " + str(filenames))
        self.filesToMerge = filenames

    def select_output_file(self):
        filetypes = (
            ('PDF files', '*.pdf'),
            ('All files', '*.*')
        )
        self.outputFile = tk.filedialog.asksaveasfilename( filetypes=filetypes)
    
    def get_output_file(self):
        return self.outputFile


    def select_merge(self):
        self.merge_pdfs(self.filesToMerge)

    def get_selected_files(self):
        return self.filesToMerge

class ViewController:
    pdfMerge = PDFMerge()

    def begin(self):
        self.root = tk.Tk()
        self.root.title('Merge PDF files')
        self.root.resizable(False, False)
        self.root.geometry('300x250')

        self.num_pdf = tk.Label(self.root, text="Selected 0 files")
        self.num_pdf.pack(expand=True)
        self.update_pdf_num()

        # open button
        self.pdf_select_button = ttk.Button(
            self.root,
            text='Select PDFs',
            command=self.input
        )
        self.pdf_select_button.pack(expand=True)

        self.output_path = tk.Label(self.root, text="Output File:")
        self.output_path.pack(expand=True)
        self.output_entry = tk.Entry(self.root, text="", width=40)
        self.output_entry.pack(expand=True)
        self.output_button = tk.Button(self.root, text="Select output", command=self.output)
        self.output_button.pack(expand=True)

        self.merge_button = ttk.Button(
            self.root,
            text='Merge documents',
            command=self.merge
        )
        self.merge_button.pack(expand=True)

        self.root.mainloop()

    def input(self):
        self.pdfMerge.select_pdfs()
        self.update_pdf_num()

    def update_pdf_num(self):
        self.num_pdf.config(text="Selected " + str(len(self.pdfMerge.get_selected_files())) + " files")

    def output(self):
        self.pdfMerge.select_output_file()
        self.output_entry.delete(1, tk.END)
        self.output_entry.insert(0, self.pdfMerge.get_output_file())

    def merge(self):
        self.pdfMerge.select_merge()
        showinfo(
            title='Merge Successful',
            message= "Merged " + str(len(self.pdfMerge.get_selected_files())) + " pdfs"
        )

if __name__ == "__main__":
    views = ViewController()
    views.begin()
