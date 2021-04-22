# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/15 20:04'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.userControl.getMemberId_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("更新会员权益")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["vendorCode","sellerId","vendorId"])
        ),
        Step(
            RunRequest("更新会员权益-001")
            .with_variables(**{})
            .post("/vendorBenefits/updateOrSave")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "id":'null',
                    "platformVipConfigId":1,
                    "vipVendorId":"$vendorId",
                    "type":"CLASS",
                    "vipEcommendRatio":"50",
                    "percentageRatio":"20",
                    "classDiscount":[],
                    "remark":"第三方的舒服的撒非",
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","操作成功")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()