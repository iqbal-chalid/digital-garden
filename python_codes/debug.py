class Debug:

    def __init__(self):
        self.indent = ""
        self.message = ""
        self.counter = 0
        self.on = True

    def print_cyan(self, message):
        self.print(f"\033[36m{message}\033[0m")

    def print_green(self, message):
        self.print(f"\033[32m{message}\033[0m")

    def print_red(self, message):
        self.print(f"\033[31m{message}\033[0m")

    def print(self, message):
        if not self.on:
            return

        self.message = self.indent + message
        print(self.message)
        self.counter += 1

    def print_val(self, var, val):
        self.print(f"{var} : {val}")

    def fx(self, message):
        self.on = True
        self.print_cyan("Fx: " + message)
        self.inc()

    def inc(self):
        self.indent += "  "

    def dec(self):
        self.indent = self.indent[:-2]

    def get_counter(self):
        return self.counter

    def ON(self):
        self.on = True

    def OFF(self):
        self.on = False

    def print_list_diff(self, label, list_print, list_compare):
        print(self.indent, end="")
        print(label, end="")
        print(" : ", end="")
        print("[", end="")
        length = len(list_print)
        for index, m in enumerate(list_print):
            if list_print[index] == list_compare[index]:
                print(f"{m}", end="")
            else:
                print(f"\033[32m{m}\033[0m", end="")

            if index != length - 1:
                print(", ", end="")

        print("]")
