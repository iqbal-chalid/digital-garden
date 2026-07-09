from functools import wraps
from time import perf_counter


class Debug:

    def __init__(self):
        self.reset()

    def reset(self):
        self.indent = ""
        self.message = ""
        self.counter = 0
        self.on = True
        self.called = 0
        self.func_called = {}
        self.level = 0

    def space(self):
        print(" ")

    def line(self, length=80):
        self.print("-" * length)

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

    def print_condition(self, label, val):
        if val:
            self.print_green(label)
        else:
            self.print_red(label)

    def print_val(self, var, val):
        self.print(f"{var} : {val}")

    def fx(self, func_name):
        self.called += 1
        self.func_called[func_name] = self.func_called.get(func_name, 0) + 1
        self.on = True
        self.print_cyan(
            f"{self.level}|Fx: "
            + func_name
            + f" -> F{self.func_called[func_name]} : G{self.called}"
        )
        self.inc()

    def inc(self):
        self.indent += "  "
        self.level += 1

    def dec(self):
        self.indent = self.indent[:-2]
        self.level -= 1

    def get_counter(self):
        return self.counter

    def ON(self):
        self.on = True

    def OFF(self):
        self.on = False

    def print_list(self, label, list_print, highlight):
        print(self.indent, end="")
        print(label, end="")
        print(" : ", end="")
        print("[", end="")
        length = len(list_print)

        if type(highlight) == int:
            start = highlight
            end = start + 1
        elif (type(highlight) == list) and (len(highlight) == 2):
            start = highlight[0]
            end = highlight[1]

        for index, m in enumerate(list_print):

            if start <= index < end:
                print(f"\033[32m{m}\033[0m", end="")
            else:
                print(f"{m}", end="")

            if index != length - 1:
                print(", ", end="")

        print("]")

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

    def print_summary(self, title, dict_var):
        self.reset()
        self.space()

        self.print_cyan(title)
        for k, v in dict_var.items():
            self.print_val(k, v)

        self.line(40)
        self.space()

    def debug(
        self,
        *,
        show_elapsed=False,
        show_args=False,
        show_return=False,
        name=None,
    ):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                func_name = name or func.__name__
                self.fx(func_name)
                g_counter = self.called

                if show_args:
                    self.print(f"args : {args}")

                start = perf_counter()

                try:
                    result = func(*args, **kwargs)
                finally:
                    elapsed = perf_counter() - start

                    if show_elapsed:
                        self.print_green(
                            f"⏱️ {func_name} -- elapsed : {elapsed:.6f} sec (G{g_counter})"
                        )

                    self.dec()

                if show_return:
                    self.print(f"return : {result}")

                return result

            return wrapper

        return decorator
