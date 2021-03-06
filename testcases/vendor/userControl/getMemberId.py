# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/12 10:05'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("卖家获取user信息")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("卖家获取user信息-001")
            .with_variables(**{})
            .post("/users/getMemberId")
            .with_headers(
                **{
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
                    "content-type": "application/json;charset=UTF-8",
                }
            )
            .with_params(
                **{
                    "Authorization":"f2498cbd-c2ac-4111-aa84-653620495d5c"
                }
            )
            .with_json({})
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()