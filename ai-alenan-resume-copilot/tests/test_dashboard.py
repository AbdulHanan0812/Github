import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

import app as app_module


class DashboardRouteTests(unittest.TestCase):
    def setUp(self):
        app_module.app.config["TESTING"] = True
        self.client = app_module.app.test_client()

        db = app_module.sessionLocal()
        db.query(app_module.Report).delete()
        db.query(app_module.User).delete()
        db.commit()
        db.close()

        user = app_module.User(username="tester", email="tester@example.com", password_hash="secret")
        db = app_module.sessionLocal()
        db.add(user)
        db.commit()
        db.refresh(user)
        db.close()
        self.user = user

    def test_dashboard_post_saves_report_with_expected_fields(self):
        app_module.resume_analyzer = lambda resume_text, user_goal: {
            "skills": ["Python"],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
        }

        with self.client.session_transaction() as sess:
            sess["user"] = "tester@example.com"
            sess["username"] = "tester"

        response = self.client.post(
            "/dashboard",
            data={"role": "Backend Engineer", "resume": "Python developer"},
            follow_redirects=False,
        )

        self.assertEqual(response.status_code, 200)

        db = app_module.sessionLocal()
        report = db.query(app_module.Report).filter_by(user_id=self.user.id).first()
        db.close()

        self.assertIsNotNone(report)
        self.assertEqual(report.role, "Backend Engineer")
        self.assertEqual(report.resume, "Python developer")
        self.assertIn("Python", report.result)


if __name__ == "__main__":
    unittest.main()
