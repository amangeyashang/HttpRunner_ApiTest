# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/10 10:28'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from .createOrder_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):
    config = (
        Config("订单详情")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["depotCode","summaryOrderCode"])
        ),
        Step(
            RunRequest("订单详情-001")
            .with_variables(**{})
            .post("/order/queryByOrderCode")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "os":"min",
                    "memberId":"${ENV(memberId)}",
                    "lat":29.71797999388022,
                    "lon":106.63042999999999,
                    "userToken":"f9f642a276f74c4f86f57b94f95e09ee",
                    "vendorCode":"$depotCode",
                }
            )
            .with_json(
                {
                    "orderCode":"$summaryOrderCode",
                    "state":"new"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()