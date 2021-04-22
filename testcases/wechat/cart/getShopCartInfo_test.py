# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 11:43'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("购物车列表")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*["depotCode"])
    )
    teststeps = [
        Step(
            RunRequest("购物车列表-001")
            .with_variables(**{})
            .post("/cart/getShopCartInfo")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "vendorCode":"$depotCode"
                }
            )
            .with_json(
                {
                    "memberId":"${ENV(memberId)}",
                    "channel":"WECHAT",
                    "depotCode":"$depotCode"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()