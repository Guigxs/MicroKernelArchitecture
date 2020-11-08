import CalculatorPlugin
import pkgutil
import inspect

class Add(CalculatorPlugin.Plugin):
    def __init__(self):
        super().__init__()
        self.name = "Addition"
        self.operator = "+"
    
    def compute(self, a, b):
        return int(a) + int(b)


class Application:
    def __init__(self, *, plugins: list=list()):
        self._plugins = plugins

    def run(self):
        print("-" * 10)
        print("Starting program")

        print("Initializing modules...")
        plugins = self._plugins
        operations = []
        for plugin in plugins:
            print(f"    - {plugin.name} ({plugin.operator})")
            operations.append(plugin.operator)
        print("Modules initialized !")
        
        x = ""
        while x != "E":
            if x == "":
                x = input("Enter an operation ('E' for exit): ") 

            elif x in operations:
                a = int(input("Enter A ('E' for exit): "))
                b = int(input("Enter B ('E' for exit): "))

                for plugin in plugins:
                    if x == plugin.operator:
                        print(plugin.compute(a, b))
                x = ""

            elif x == "E":
                x = "E"

            else:
                print("Unkown operation:", x)
                x = ""


        print("Program done")
        print("-" * 10)
        print()

def discoverPlugins():
    liste = []
    for _, plug, _ in pkgutil.iter_modules(["./plugins/."]):
        modules = __import__(f"plugins.{plug}", fromlist=["plugins"])
        classmember = inspect.getmembers(modules, inspect.isclass)

        for (_, i) in classmember:
            if issubclass(i, CalculatorPlugin.Plugin):
                print(i)
                liste.append(i())

    return liste

if __name__ == "__main__":
    internalPlugins = [Add()]
    externalPlugins = discoverPlugins()

    app = Application(plugins = internalPlugins + externalPlugins)
    app.run()