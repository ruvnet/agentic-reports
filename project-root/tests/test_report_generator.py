from app.services.report_generator import generate_report

def test_generate_report():
    topic = "AI"
    report = generate_report(topic)
    assert isinstance(report, str)
