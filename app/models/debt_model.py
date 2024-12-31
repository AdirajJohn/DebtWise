from app.schemas.debt_schema import schemas
s = schemas()
print(s.test_schemas)

class dept_model:
    test_model = "test_model" + str(s.test_schemas)