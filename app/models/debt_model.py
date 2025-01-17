from app.schemas.debt_schema import schemas
s = schemas()
print(s.test_schemas)

class dept_model:
    test_model = "test_model" + str(s.test_schemas)

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from app.database.debt_DB import Base

class DebtData(Base):
    __tablename__ = 'debtinfo'
    #Debt Identification
    debt_id = Column(Integer, primary_key = True , index = True)
    creditor_name = Column(String, index = True)
    debtor_name = Column(String, index = True)
    #Debt Type
    debt_type = Column(String, index = True)
    #Collateral backed debt
    is_secure_debt = Column(Boolean, default = False)
    #Loan Details
    principal_amount = Column(Integer,index = True)
    interest_rate_annum = Column(Integer, index = True)
    #Fixed or Variabale Intrest
    interest_type = Column(Integer, index = True)
    loan_tenure = Column(Integer, index=True)
    #Outstanding Debt information
      # Remaining prinical to be paid
    OS_principal = Column(Integer, index=True)
      # Remaining interest to be paid
    OS_interest = Column(Integer, index=True)
      # Sum of remaining interest and principal
    OS_total = Column(Integer, index = True)
      # Any past amount that has not been paid
    overdue_amount = Column(Integer, index = True)
      # Debt status {Active, Done, defaulted}
    debt_status = Column(String, index = True)

