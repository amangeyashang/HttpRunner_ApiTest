# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/10 14:17'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("查询有效预存活动")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["depotCode"])
        ),
        Step(
            RunRequest("查询有效预存活动-001")
            .with_variables(**{})
            .post("/promotion/preDeposit/queryValidPreDepositPromotion")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "vendorCode":"$depotCode"
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