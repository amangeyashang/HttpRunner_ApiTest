# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/11 19:23'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("登录")
            .variables(**{})
            .base_url("${ENV(base_url_ui_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("登录-001")
            .with_variables(**{})
            .post("/users/loginCheck")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/x-www-form-urlencoded",
                }
            )
            .with_data(
                {
                    "account": "18000000003",
                    "password": "123456"
                }
            )
            .validate()
            .extract()
            .with_jmespath("body.data.sessionId","sessionId")
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()