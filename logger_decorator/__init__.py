from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def log_info(self):
        pass

    @abstractmethod
    def log_debug(self):
        pass

class Awx(Logger):
    def __init__(self):
        pass

    def log_info(self, message):
        print(message)

    def log_debug(self, method_name, message):
        title = f"<class: Awx> {method_name}"
        body = message
        output = f"""
        {title}
        {body}
        """
        print(output)

    def create_job(self, extra_var):
        """
        extra_var: dict
        {
            "var1": 1,
            "var2": "two",
            "var3": True,
            "var4": [
                {"item1": "value1"},
                {"item2": "value2"},
            ]
        }
        """
        self.log_info("create awx job")
        self.log_debug("create_job", extra_var)

# main
if __name__ == "__main__":
    extra_var = {
                "var1": 1,
                "var2": "two",
                "var3": True,
                "var4": [
                    {"item1": "value1"},
                    {"item2": "value2"},
                ],
            }
    awx = Awx()
    awx.create_job(extra_var)