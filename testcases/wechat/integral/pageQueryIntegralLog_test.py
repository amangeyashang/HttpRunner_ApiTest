# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/10 16:41'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("分页查询会员积分流水")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("分页查询会员积分流水-001")
                .with_variables(**{})
                .post("/users/integral/pageQueryIntegralLog")
                .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
                .with_json(
                {
                    "memberId":"${ENV(memberId)}",
                    "beginDate":"2021-03-01",
                    "endDate":"2021-03-31",
                    "pageInfo":
                        {
                            "pageNo":1,
                            "pageSize":20
                        }
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.status","S")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()