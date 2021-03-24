# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/15 18:02'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("预存活动列表")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("预存活动列表-001")
            .with_variables(**{})
            .post("/vendor/preDeposit/pageQueryPreDepositPromotion")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "pageInfo":{"pageNo":1,"pageSize":10},
                    "name":"",
                    "memberId":"${ENV(memberId)}",
                    "userId":"${ENV(memberId)}",
                    "vendorId":"${ENV(vendorId)}",
                    "depotCode":"${ENV(vendorCode)}",
                    "vendorCode":"${ENV(vendorCode)}"
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