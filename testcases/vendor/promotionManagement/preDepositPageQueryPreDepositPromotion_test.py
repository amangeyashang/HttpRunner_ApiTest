# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/15 14:19'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.userControl.getMemberId_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("充值赠送列表")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["vendorCode","sellerId","vendorId",])
        ),
        Step(
            RunRequest("充值赠送列表-001")
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
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode"
                }
            )
            .extract()
            .with_jmespath("body.infoList[0].id","preDepositId")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.message","成功")
            .assert_equal("body.status","S")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()