from datetime import datetime, date
from transaction import *
import tkinter as tk
from tkinter import ttk, messagebox
from db import DBHelper

class FinanceManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('FinanceManager')
        self.geometry('400x300')
        self.resizable(False, False)

        # container for the stack-like page structure
        container = tk.Frame(self)
        container.pack(side='top', expand=True, fill='both')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for page in (IndexPage, ExpensePage, DepositPage, HistoryPage):
            page_name = page.__name__
            frame = page(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('IndexPage')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == 'HistoryPage':
            frame.populate_list()

class IndexPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text='Click a button to get started', font=('Arial', 14))
        label.pack(pady=20)

        expense_button = tk.Button(self, text='Expense',
                                   command=lambda: controller.show_frame('ExpensePage'))
        deposit_button = tk.Button(self, text='Deposit',
                                   command=lambda: controller.show_frame('DepositPage'))
        history_button = tk.Button(self, text='History',
                                   command=lambda: controller.show_frame('HistoryPage'))
        expense_button.pack(pady=20)
        deposit_button.pack(pady=20)
        history_button.pack()

class ExpensePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.transaction_method = ttk.Combobox(self,
                                               value=[method.value for method in TransactionMethod],
                                               state='readonly',
                                               font=('Arial', 14))
        self.transaction_method.current(0)
        self.transaction_method.pack(pady=20)

        self.expense_type = ttk.Combobox(self,
                                         value=[types.value for types in ExpenseType],
                                         state='readonly',
                                         font=('Arial', 14))
        self.expense_type.current(0)
        self.expense_type.pack(pady=20)

        self.amount_label = tk.Label(self, text='Amount:', font=('Arial', 12))
        self.amount_label.pack()
        self.amount = tk.Entry(self, width=30, font=('Arial', 12))
        self.amount.pack()

        self.description_label = tk.Label(self, text='Description:', font=('Arial', 12))
        self.description_label.pack()
        self.description = tk.Entry(self, width=30, font=('Arial', 12))
        self.description.pack(pady=20)

        self.submit_button = tk.Button(self,
                                       text='Add transaction',
                                       command=self.__write_transaction)
        self.submit_button.pack()

    def __default_option(self):
        self.transaction_method.current(0)
        self.expense_type.current(0)
        self.amount.delete(0, tk.END)
        self.description.delete(0, tk.END)

    def __write_transaction(self):
        if not self.amount.get().isdigit():
            messagebox.showwarning('Error', 'Please only input number into amount')
            return

        Expense(self.transaction_method.get(),
                -float(self.amount.get()),
                self.expense_type.get(),
                self.description.get()).write_transaction_history()

        messagebox.showinfo('Finished', 'Transaction added')
        self.controller.show_frame('IndexPage')
        self.__default_option()

class DepositPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.transaction_method = ttk.Combobox(self,
                                               value=[method.value for method in TransactionMethod],
                                               state='readonly',
                                               font=('Arial', 14))
        self.transaction_method.current(0)
        self.transaction_method.pack(pady=20)

        self.amount_label = tk.Label(self, text='Amount:', font=('Arial', 12))
        self.amount_label.pack()
        self.amount = tk.Entry(self, width=30, font=('Arial', 12))
        self.amount.pack()

        self.description_label = tk.Label(self, text='Description:', font=('Arial', 12))
        self.description_label.pack()
        self.description = tk.Entry(self, width=30, font=('Arial', 12))
        self.description.pack(pady=20)

        self.submit_button = tk.Button(self,
                                       text='Add transaction',
                                       command=self.__write_transaction)
        self.submit_button.pack()

    def __default_option(self):
        self.transaction_method.current(0)
        self.amount.delete(0, tk.END)
        self.description.delete(0, tk.END)

    def __write_transaction(self):
        if not self.amount.get().isdigit():
           messagebox.showwarning('Error', 'Please only input number into amount')
           return

        Deposit(self.transaction_method.get(),
                float(self.amount.get()),
                self.description.get()).write_transaction_history()

        messagebox.showinfo('Finished', 'Transaction added')
        self.controller.show_frame('IndexPage')
        self.__default_option()

class HistoryPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.scrollbar = tk.Scrollbar(self, orient='vertical')
        self.scrollbar.grid(row=0, column=1, stick='ns')

        self.listbox = tk.Listbox(self,
                                  yscrollcommand=self.scrollbar.set,
                                  selectmode='single',
                                  font=('Courier', 12))
        self.scrollbar.config(command=self.listbox.yview)

        self.populate_list()
        self.listbox.grid(row=0, column=0, sticky='nsew')
        self.listbox.bind('<<ListboxSelect>>',
                          self.__on_select)

        self.back_button = tk.Button(self,
                                     text='Back',
                                     font=('Arial', 14),
                                     command=self.__back_to_index)
        self.back_button.grid(row=1, column=0, stick='nsew')

    def populate_list(self):
        # populate the history
        with DBHelper() as db:
            self.listbox.delete(0, tk.END)
            self.history = db.cursor.execute(db.query['get_history']).fetchall()
            for item in self.history:
                date = datetime.strptime(item[1], '%Y-%m-%d %H:%M:%S').date()
                self.listbox.insert(tk.END, f'$ {item[0]:<15} | {str(date):>5}')

    def __on_select(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            item = self.history[index]

        content = f'$ {item[0]}\n\n date: {item[1]}\n\n catagory: {item[2]}\n\n method: {item[3]}\n\n description: {item[4]}'
        CustomMessage(self, 'Info', content)

    def __back_to_index(self):
        self.controller.show_frame('IndexPage')

class CustomMessage(tk.Toplevel):
    def __init__(self, parent, title, content):
        super().__init__(parent)
        self.title(title)
        self.geometry('500x400')

        self.text = tk.Label(self,
                             text=content,
                             font=('Courier', 12))
        self.text.pack(padx=10, pady=10, fill='both', expand=True)
        tk.Button(self, text='Close', command=self.destroy).pack(pady=10)

if __name__ == '__main__':
    app = FinanceManager()
    app.mainloop()
