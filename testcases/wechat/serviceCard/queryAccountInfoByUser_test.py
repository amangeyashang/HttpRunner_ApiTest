# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/9 17:09'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("根据用户查询账户信息")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("根据用户查询账户信息-001")
                .with_variables(**{})
                .get("/account/query/queryAccountInfoByUser")
                .with_params(
                **{
                    "userId":"${ENV(memberId)}",
                    "userType":"U",
                    "content":"查询中..."
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.message","成功")
                .assert_equal("body.status","S")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()