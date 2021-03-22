# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/17 14:56'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("快捷拼团入口")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("快捷拼团入口-001")
            .with_variables(**{})
            .post("/promotion/groupPurchase/getGroupPurchasePromotions")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "latitude":29.71797999388022,
                    "longitude":106.63042999999999
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()