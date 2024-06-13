import tkinter as tk

class temp_conv:
    def __init__(self):

        self.temp_frame = tk.Frame(padx = 10, pady = 10)
        self.temp_frame.grid()

        self.temp_heading = tk.Label(self.temp_frame, text = 'Temperature Converter', font = ('Arial', 16, 'bold'))
        self.temp_heading.grid(row = 0)

        instructions = "Please enter a temperature below and then press on of the buttons to convert it from Celcius to Farenheit."

        self.temp_instructions = tk.Label(self.temp_frame, text = instructions, wrap = 250, width = 40, justify ='left')
        self.temp_instructions.grid(row = 1)

        self.temp_entry = tk.Entry(self.temp_frame, font = ('Arial', 14))
        self.temp_entry.grid(row = 2, padx = 10, pady = 10)

        erorr = 'Please enter number'

        self.temp_error = tk.Label(self.temp_frame, text = '', fg = 'red')
        self.temp_error.grid(row = 3)

        self.button_frame = tk.Frame(self.temp_frame)
        self.button_frame.grid(row = 4)

        self.temp_cel = tk.Button(self.button_frame, text = 'To Degrees C', bg = "#990099", fg = "#FFFFFF", font = ('Arial', 14, 'bold'), width = 14, command = self.to_degtC)
        self.temp_cel.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.temp_far = tk.Button(self.button_frame, text = 'To Farenheit', bg = "#009900", fg = "#FFFFFF", font = ('Arial', 14, 'bold'), width = 14)
        self.temp_far.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.temp_help = tk.Button(self.button_frame, text = 'Help / Info', bg = "#CC6600", fg = "#FFFFFF", font = ('Arial', 14, 'bold'), width = 14)
        self.temp_help.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.temp_hist = tk.Button(self.button_frame, text = 'History / Export', bg = "#004C99", fg = "#FFFFFF", font = ('Arial', 14, 'bold'), width = 14, state = 'disabled')
        self.temp_hist.grid(row = 1, column = 1, padx = 5, pady = 5)

    def check_temp(self, min_value):
        error = 'Please enter a number that is more than {}'.format(min_value)

        try:
            response = self.temp_entry.get()
            response = float(response)

            if response < min_value:
                self.temp_error.config(text = error)
            else:
                return response
        
        except ValueError:
            self.temp_error.config(text = error)

    def to_degtC(self):

        self.check_temp(-459)
    
root = tk.Tk()
root.title('Temperature Convertor')
temp_conv()
root.mainloop()