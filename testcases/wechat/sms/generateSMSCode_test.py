# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/11 9:37'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("发送短信")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("发送短信-001")
                .with_variables(**{})
                .post("/soa/miscService/generateSMSCode")
                .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
                .with_json(
                {
                    "mobile": "18716280028",
                    "type": "CHANGE_MOBILE_OR_PASSWORD",
                    "size": 6
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()