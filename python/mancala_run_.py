import tkinter
from tkinter import ttk
from tkinter import filedialog
import re

class Adder(ttk.Frame):
    """The adders gui and functions."""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def on_quit(self):
        """Exits program."""
        quit()

    def data_upload(self, event=None):
        filename = filedialog.askopenfilename()
        self.data_entry.insert(tkinter.END, filename)

    def fit_upload(self, event=None):
        filename = filedialog.askopenfilename()
        self.fit_entry.insert(tkinter.END, filename)

    def sequence_upload(self, event=None):
        filename = filedialog.askopenfilename()
        self.sequence_entry.insert(tkinter.END, filename)

    def pdb_upload(self, event=None):
        filename = filedialog.askopenfilename()
        self.pdb_entry.insert(tkinter.END, filename)

    def calculate(self):
        """Calculates the sum of the two inputted numbers."""
        #num1 = int(self.num1_entry.get())
        #num2 = int(self.num2_entry.get())
        #num3 = num1 + num2
        #self.answer_label['text'] = num3

        data = self.data_entry.get()
        fit = self.fit_entry.get()
        sequence = self.sequence_entry.get()
        pdb = self.pdb_entry.get()

        print(data, fit, sequence, pdb)
    def init_gui(self):
        """Builds GUI."""
        self.root.title('Mancala: SAXS Data Bead Modeling Routine')
        self.root.option_add('*tearOff', 'FALSE')

        self.grid(column=0, row=0, sticky='nsew')

        self.menubar = tkinter.Menu(self.root)

        self.menu_file = tkinter.Menu(self.menubar)
        self.menu_file.add_command(label='Exit', command=self.on_quit)

        self.menu_edit = tkinter.Menu(self.menubar)

        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menubar.add_cascade(menu=self.menu_edit, label='Edit')

        self.root.config(menu=self.menubar)

        self.data_entry = ttk.Entry(self, width = 15)
        self.data_entry.grid(column=1, row=2)

        self.data_button = ttk.Button(self, text='Browse',command=self.data_upload)
        self.data_button.grid(column=2, row=2, columnspan=1)

        self.fit_entry = ttk.Entry(self, width = 15)
        self.fit_entry.grid(column=1, row=3)

        self.fit_button = ttk.Button(self, text='Browse',command=self.fit_upload)
        self.fit_button.grid(column=2, row=3, columnspan=1)

        self.sequence_entry = ttk.Entry(self, width = 15)
        self.sequence_entry.grid(column=1, row=4)

        self.sequence_button = ttk.Button(self, text='Browse',command=self.sequence_upload)
        self.sequence_button.grid(column=2, row=4, columnspan=1)

        self.pdb_entry = ttk.Entry(self, width = 15)
        self.pdb_entry.grid(column=1, row=5)

        self.pdb_button = ttk.Button(self, text='Browse',command=self.pdb_upload)
        self.pdb_button.grid(column=2, row=5, columnspan=1)

        # self.dmax = ttk.Entry(self, width=8)
        # self.dmax.grid(column=1, row=4)
        #
        # self.npasses = ttk.Entry(self, width=8)
        # self.npasses.insert(tkinter.END, '80')
        # self.npasses.grid(column=3, row=4)
        #
        # self.loops_per_pass = ttk.Entry(self, width=8)
        # self.loops_per_pass.insert(tkinter.END, 'def')
        # self.loops_per_pass.grid(column=1, row=5)
        #
        # self.ll = ttk.Entry(self, width=8)
        # self.ll.insert(tkinter.END, '100')
        # self.ll.grid(column=3, row=5)
        #
        # self.connect = ttk.Entry(self, width=8)
        # self.connect.insert(tkinter.END, '30000')
        # self.connect.grid(column=1, row=6)
        #
        # self.verbose = ttk.Entry(self, width=8)
        # self.verbose.insert(tkinter.END, 'yes')
        # self.verbose.grid(column=3, row=6)
        #
        # self.clash = ttk.Entry(self, width=8)
        # self.clash.insert(tkinter.END, '1.8')
        # self.clash.grid(column=1, row=9)
        #
        # self.shift = ttk.Entry(self, width=8)
        # self.shift.insert(tkinter.END, '50')
        # self.shift.grid(column=3, row=9)



        self.calc_button = ttk.Button(self, text='Run',
                command=self.calculate)
        self.calc_button.grid(column=0, row=20, columnspan=4)

        # Labels that remain constant throughout execution.
        ttk.Label(self, text='Input parameters').grid(column=0, row=0,columnspan=4)
        ttk.Separator(self, orient='horizontal').grid(column=0,row=1, columnspan=4, sticky='ew')
        ttk.Label(self, text='Data file (.rad)').grid(column=0, row=2,sticky='w')
        ttk.Label(self, text='Fit file (*_bf.dat)').grid(column=0, row=3,sticky='w')
        ttk.Label(self, text='Sequence file').grid(column=0, row=4,sticky='w')
        ttk.Label(self, text='Sequence from PDB').grid(column=0, row=5,sticky='w')


        # ttk.Label(self, text='Dmax').grid(column=0, row=4,sticky='w')
        # ttk.Label(self, text='Number of passes').grid(column=2, row=4,sticky='w')
        # ttk.Label(self, text='Loops per pass').grid(column=0, row=5,sticky='w')
        # ttk.Label(self, text='Lambda').grid(column=2, row=5,sticky='w')
        # ttk.Label(self, text='Connect').grid(column=0, row=6,sticky='w')
        # ttk.Label(self, text='Verbose').grid(column=2, row=6,sticky='w')
        #
        # ttk.Separator(self, orient='horizontal').grid(column=0,row=7, columnspan=4, sticky='ew')
        # ttk.Label(self, text='Advanced parameters').grid(column=0, row=8,columnspan=4)
        # ttk.Label(self, text='Clash distance').grid(column=0, row=9,sticky='w')
        # ttk.Label(self, text='Initial shift').grid(column=2, row=9,sticky='w')
        # ttk.Label(self, text='Insertion').grid(column=0, row=10,sticky='w')
        # ttk.Label(self, text='T strength').grid(column=2, row=10,sticky='w')

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

if __name__ == '__main__':
    root = tkinter.Tk()
    Adder(root)
    root.mainloop()