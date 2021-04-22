# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/9 18:32'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("热门搜索列表")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("热门搜索列表-001")
            .with_variables(**{})
            .post("/behavior/sortKeyword")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json"
                }
            )
            .with_json({""})
            .validate()
            .assert_equal("status_code",200)
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()