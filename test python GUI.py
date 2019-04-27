#!/usr/bin/python3
# invoice_solution.py by JCMatteson
# test python GUI

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
    
class Invoice:

    def __init__(self, master):
        
        master.title("Chris' Invoice Shack")
        master.resizable(False, False)
        master.configure(background = '#F5EEF8')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#F5EEF8')
        self.style.configure('TButton', background = '#F5EEF8')
        self.style.configure('TLabel', background = '#F5EEF8', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))      

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        
        ttk.Label(self.frame_header, text = 'Thanks for Invoicing!', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("We're glad you chose Chris' Invoice Shack for your invoicing needs.  "
                          "Hope you made money today.")).grid(row = 1, column = 1)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Date:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Vin:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Invoice:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Dealer:').grid(row = 2, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'PO:').grid(row = 4, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Price:').grid(row = 4, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Product:').grid(row = 6, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Product:').grid(row = 6, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Product:').grid(row = 8, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Product:').grid(row = 8, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Year:').grid(row = 0, column = 3, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Make:').grid(row = 2, column = 3, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Model:').grid(row = 4, column = 3, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Product:').grid(row = 6, column = 3, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Product:').grid(row = 8, column = 3, padx = 5, sticky = 'sw')
        
        
        self.entry_date = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_vin = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_innum = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_dealer = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_po = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_price = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_product1 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_product2 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_product3 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_product4 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_year = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_make = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_model = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_product5 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_product6 = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
      
        
        
        
        self.entry_date.grid(row = 1, column = 0, padx = 5)
        self.entry_vin.grid(row = 1, column = 1, padx = 5)
        self.entry_innum.grid(row = 3, column = 0, padx = 5)
        self.entry_dealer.grid(row = 3, column = 1, padx = 5)
        self.entry_po.grid(row = 5, column = 0, padx = 5)
        self.entry_price.grid(row = 5, column = 1, padx = 5)
        self.entry_product1.grid(row = 7, column = 0, padx = 5)
        self.entry_product2.grid(row = 7, column = 1, padx = 5)
        self.entry_product3.grid(row = 9, column = 0, padx = 5)
        self.entry_product4.grid(row = 9, column = 1, padx = 5)
        self.entry_year.grid(row = 1, column = 3, padx = 5)
        self.entry_make.grid(row = 3, column = 3, padx = 5)
        self.entry_model.grid(row = 5, column = 3, padx = 5)
        self.entry_product5.grid(row = 7, column = 3, padx = 5)
        self.entry_product6.grid(row = 9, column = 3, padx = 5)
      
        
        ttk.Button(self.frame_content, text = 'Submit',
                   command = self.submit).grid(row = 10, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear',
                   command = self.clear).grid(row = 10, column = 1, padx = 5, pady = 5, sticky = 'w')

    def submit(self):
        print('invoice: {}'.format(self.entry_innum.get()))
        print('Vin: {}'.format(self.entry_vin.get()))
        print('Make: {}'.format(self.entry_make.get()))
        print('Model: {}'.format(self.entry_model.get()))
        print('Year: {}'.format(self.entry_year.get()))
        print('Date: {}'.format(self.entry_date.get()))
        print('Dealer: {}'.format(self.entry_dealer.get()))
        print('PO: {}'.format(self.entry_po.get()))
        print('Price: {}'.format(self.entry_price.get()))
        print('Product: {}'.format(self.entry_product1.get()))
        print('Product: {}'.format(self.entry_product2.get()))
        print('Product: {}'.format(self.entry_product3.get()))
        print('Product: {}'.format(self.entry_product4.get()))
        print('Product: {}'.format(self.entry_product5.get()))
        print('Product: {}'.format(self.entry_product6.get()))
     
        #messagebox.showinfo(title = 'Todays Invoces', message = 'Submitted!  Thank You')
     
    #def save(self):

        #chmod 777("textfile.txt")
        f=open("test5.txt", "a+")
        f.write('Date:      {}\n'.format(self.entry_date.get()))
        f.write('invoice:   {}\n'.format(self.entry_innum.get())),
        f.write('Vin:       {}\n'.format(self.entry_vin.get())),
        f.write('Make:      {}\n'.format(self.entry_make.get())),
        f.write('Model:     {}\n'.format(self.entry_model.get()))
        f.write('Year:      {}\n'.format(self.entry_year.get()))        
        f.write('Dealer:    {}\n'.format(self.entry_dealer.get()))
        f.write('PO:        {}\n'.format(self.entry_po.get()))        
        f.write('Product:   {}\n'.format(self.entry_product1.get()))
        f.write('Product:   {}\n'.format(self.entry_product2.get()))
        f.write('Product:   {}\n'.format(self.entry_product3.get()))
        f.write('Product:   {}\n'.format(self.entry_product4.get()))
        f.write('Product:   {}\n'.format(self.entry_product5.get()))
        f.write('Product:   {}\n'.format(self.entry_product6.get()))
        f.write('Price:     {}\n'.format(self.entry_price.get()))
        f.write('------------------------{}\n'.format(()))
        f.close()
        
        
        
        
        
        self.clear()
        messagebox.showinfo(title = 'Todays Invoces', message = 'Submitted!  Thank You')   
    
    def clear(self):
        self.entry_innum.delete(0, 'end')
        self.entry_vin.delete(0, 'end')
        #self.entry_date.delete(0, 'end')
        self.entry_dealer.delete(0, 'end')
        self.entry_po.delete(0, 'end')
        self.entry_price.delete(0, 'end')
        self.entry_product1.delete(0, 'end')
        self.entry_product2.delete(0, 'end')
        self.entry_product3.delete(0, 'end')
        self.entry_product4.delete(0, 'end')
        self.entry_make.delete(0, 'end')
        self.entry_model.delete(0, 'end')
        self.entry_year.delete(0, 'end')
        self.entry_product5.delete(0, 'end')
        self.entry_product6.delete(0, 'end')
  
  
        
         
def main():            
    
    root = Tk()
    invoice = Invoice(root)
    root.mainloop()
    
if __name__ == "__main__": main()
