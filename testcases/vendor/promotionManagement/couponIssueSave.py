# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/14 16:11'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from .couponUsedPage_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("发放优惠券")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["vendorCode","sellerId","vendorId","couponId"])
        ),
        Step(
            RunRequest("发放优惠券-001")
            .with_variables(**{})
            .post("/vendorCoupon/couponIssue/save")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "items":[{"couponTypeId":"$couponTypeId","couponTypeName":"$couponTypeName"}],
                    "userMobile":"18000000003",
                    "totalQuantity":1,
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()