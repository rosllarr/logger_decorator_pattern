from abc import ABC, abstractmethod

class Logger(ABC):
    def info(self) -> str:
        pass

    def debug(self) -> str:
        pass

class LoggerWrapper(Logger):
    def __init__(self, logger: Logger) -> None:
        self._logger = logger

    def info(self) -> str:
        return self._logger.info()
    
    def debug(self) -> str:
        return self._logger.debug()
    
class CreateAwxJob(LoggerWrapper):
    def __init__(self, template_id: int, extra_var: dict) -> None:
        self.template_id = template_id
        self.extra_var = extra_var

    def info(self) -> str:
        return f"create awx job"
    
    def debug(self) -> str:
        return f"""
        <class: CreateAwxJob>
        template_id = {self.template_id}
        extra_var = {self.extra_var}
        """
    
    def execute(self, log_level) -> None:
        if log_level == "info":
            print(self.info())

        if log_level == "debug":
            print(self.debug())
    
def main():
    log_level = "debug"
    template_id = 10
    extra_var = {
            "var1": 1,
            "var2": "two",
            "var3": True,
            "var4": [
                {"item1": "value1"},
                {"item2": "value2"},
            ],
        }
    create_awx_job = CreateAwxJob(
        template_id=template_id,
        extra_var=extra_var
    )
    create_awx_job.execute(log_level=log_level)

if __name__ == "__main__":
    main()


# class IAwx(ABC):
#     def create_job(self):
#         """Create new job on AWX server"""
#         pass

#     def get_job_info(self):
#         """Get infomation of processing job about:
#             - job id
#             - current status
#             - stdout
#         """
#         pass

# class Awx(LoggerWrapper):
#     def __init__(self, template_id, extra_var):
#         self.template_id = template_id
#         self.extra_var = extra_var

#     def create_job(self):
#         print("create awx job")
#         print(self.extra_var)

#     def get_job_info(self):
#         print("get job info")
#         self.job_id = 99
#         self.stdout = "===="
#         self.status = "successfuly"