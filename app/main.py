from app.models.debt_model import dept_model
d = dept_model()
class mainapp:
    test_app = "app_module" + str(d.test_model) 

class testmain:
    val = "abc"

    @classmethod
    def print_app_info(cls):
        print(f"App Name: {cls.val}")

