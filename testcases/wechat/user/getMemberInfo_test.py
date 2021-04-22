# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/9 16:50'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("获取用户信息")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("获取用户信息-001")
            .with_variables(**{})
            .get("/users/getMemberInfo")
            .with_params(
                **{
                    "os":"min",
                    "memberId":"${ENV(memberId)}",
                    "lat":28.45362,
                    "lon":109.006128,
                    "userToken":"684f2aa256a6408980cbb1f56602e250",
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()