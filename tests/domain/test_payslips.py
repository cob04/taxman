import uuid

from taxman.domain import payslips as p


def test_payslip_model_init():
    code = uuid.uuid4()
    payslip =p.Payslip(code, fullname="Bob Beltcher",
                     income=40000,
                     nationality="Kenyan")
    assert payslip.code == code
    assert payslip.fullname == "Bob Beltcher"
    assert payslip.income == 40000
    assert payslip.nationality == "Kenyan"
