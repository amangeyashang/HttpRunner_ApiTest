# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/19 14:46'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("查询会员积分")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("查询会员积分-001")
            .with_variables(**{})
            .post("/users/integral/queryIntegral")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "memberId":"${ENV(memberId)}"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.status","S")
            .assert_equal("body.message","成功")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()