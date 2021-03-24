# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/23 17:49'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from .queryOrderListBySeller_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("删除订单")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("request with functions")
                .call(RequestWithFunctions)
                .export(*["orderCode"])
        ),
        Step(
            RunRequest("删除订单-001")
            .with_variables(**{})
            .get("/vendorOrder/deleteOrder")
            .with_params(
                **{
                    "orderCode":"$orderCode",
                    "memberId":"${ENV(memberId)}",
                    "userId":"${ENV(memberId)}",
                    "vendorId":"${ENV(vendorId)}",
                    "depotCode":"${ENV(vendorCode)}",
                    "vendorCode":"${ENV(vendorCode)}"
                }
        )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()