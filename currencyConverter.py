import tkinter as tk 
from tkinter import PhotoImage

window = tk.Tk()
window.geometry("400x600")

background = PhotoImage(file = "E:\\Codeclause\\images.png")
bg = tk.Label(image = background)
bg.pack(pady=10)

current_options = ['INR','USD','CAD','CNY','JPY','KRW','GBP','EUR','AUD','BRL']
convert_options = ['INR','USD','CAD','CNY','JPY','KRW','GBP','EUR','AUD','BRL']

from_currency = tk.StringVar()
from_currency.set("Current Currency")
to_currency = tk.StringVar()
to_currency.set("Converted Currency")
amount_var=tk.IntVar()
amount_var.set("")

def convert_currency(amount, from_curr, to_curr):
    conversion_rates = {
        'INR': {'USD': 0.012,'CAD': 0.016,'CNY': 0.087,'JPY': 1.85,'KRW': 16.47,'GBP': 0.0096,'EUR': 0.011,'AUD': 0.018,'BRL': 0.061},  
        'USD': {'INR': 83.46,'CAD': 1.37,'CNY': 7.24,'JPY': 154.44,'KRW': 1374.43,'GBP': 0.80,'EUR': 0.94,'AUD': 1.53,'BRL': 5.11}, 
        'CAD': {'INR': 60.85,'USD': 0.73,'CNY': 5.28,'JPY': 112.56,'KRW': 1001.88,'GBP': 0.58,'EUR': 0.68,'AUD': 1.12,'BRL': 3.73},
        'CNY': {'INR': 11.78,'USD': 0.14,'CAD': 0.19,'JPY': 21.78,'KRW': 189.99,'GBP': 0.11,'EUR': 0.13,'AUD': 0.21,'BRL': 0.71},
        'JPY': {'INR': 0.54,'USD': 0.0065,'CAD': 0.0089,'CNY': 0.047,'KRW': 8.92,'GBP': 0.0052,'EUR': 0.0061,'AUD': 0.0099,'BRL': 0.033},
        'KRW': {'INR': 0.061,'USD': 0.00073,'CAD': 0.00100,'CNY': 0.0053,'JPY': 0.11,'GBP': 0.0000058,'EUR': 0.00068,'AUD': 0.0011,'BRL': 0.0037},
        'GBP': {'INR': 104.16,'USD': 1.25,'CAD': 1.71,'CNY': 9.03,'JPY': 192.74,'KRW': 1716.69,'EUR': 1.17,'AUD': 1.91,'BRL': 6.38},
        'EUR': {'INR': 89.12,'USD': 1.07,'CAD': 1.47,'CNY': 7.73,'JPY': 164.88,'KRW': 1468.65,'GBP': 0.86,'AUD': 1.64,'BRL': 5.46},
        'AUD': {'INR': 54.45,'USD': 0.65,'CAD': 0.90,'CNY': 4.72,'JPY': 100.74,'KRW': 897.17,'GBP': 0.52,'EUR': 0.61,'BRL': 3.34},
        'BRL': {'INR': 16.33,'USD': 0.20,'CAD': 0.27,'CNY': 1.42,'JPY': 30.23,'KRW': 268.86,'GBP': 0.16,'EUR': 0.18,'AUD': 0.30}
    }
    
    if from_curr in conversion_rates and to_curr in conversion_rates[from_curr]:
        rate = conversion_rates[from_curr][to_curr]
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

def converting():
    curr=from_currency.get()
    conv=to_currency.get()
    amountvar=amount_var.get()
    result=convert_currency(amountvar,curr,conv)
    if result is not None:
        result_label.config(text=f"{amountvar} {curr} is equivalent to {result:.2f} {conv}")
        print(f"{result:.2f}")
    else:
        result_label.config(text="Conversion rate not available for the selected currencies")
        print("Conversion rate not available for the selected currencies")
    from_currency.set("Current Currency")
    to_currency.set("Converted Currency")
    amount_var.set("")

title = tk.Label(text = "Currency Converter",font=('calibre',15,'bold'))

current = tk.OptionMenu(window, from_currency, *current_options)
convert = tk.OptionMenu(window, to_currency, *convert_options)

amount_label = tk.Label(window, text="Enter Amount : ", font=('calibre', 10))
amount_entry = tk.Entry(window,textvariable = amount_var,font=('calibre', 10))

result_label = tk.Label(window, text="", font=('calibre', 10, 'bold'))

btn = tk.Button(window,text = "Convert",font=('calibre',10,'bold'),command=converting)


title.pack(pady=15)
current.pack(padx=10, pady=10)
convert.pack(padx=10, pady=10)
amount_label.pack(pady=5)
amount_entry.pack(pady=5)
result_label.pack(pady=5)
btn.pack(pady=15)

window.mainloop()
