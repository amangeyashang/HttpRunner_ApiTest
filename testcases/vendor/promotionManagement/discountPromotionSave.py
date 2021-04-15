# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/14 17:02'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.userControl.getMemberId_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("新增折扣促销")
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
            RunRequest("新增折扣促销-001")
            .with_variables(**{})
            .post("/vendor/discountPromotion/save")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "name":"测试折扣促销1",
                    "description":"",
                    "channels":["WECHAT_MALL"],
                    "scope":"SHOP",
                    "scopeShopIds":["546520236057329664"],
                    "effectMemberLevels":[0,1,2,3,4,5,6,7,8],
                    "startTime":"2021-04-14 17:02:18",
                    "endTime":"2021-04-30 17:02:20",
                    "commonStatus":"ENABLE",
                    "limitProductIds":["873381841233522688"],
                    "limitProductCodes":["PD21040100000001"],
                    "limitType":"DISCOUNT_BY_PRODUCT_AMOUNT",
                    "isStairCut":'false',
                    "stairCount":1,
                    "discountRates":[{"rateCondition":100,"discountRate":"0.90"}],
                    "allowCoupon":'true',
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
            .assert_equal("body.data.message","添加成功")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()