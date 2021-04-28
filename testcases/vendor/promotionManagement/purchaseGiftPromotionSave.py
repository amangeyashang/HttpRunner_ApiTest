# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/15 10:28'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("新增买赠满赠")
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
            RunRequest("新增买赠满赠-001")
            .with_variables(**{})
            .post("/vendor/purchaseGiftPromotion/save")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "name":"买赠满赠测试1",
                    "description":"",
                    "channels":["WECHAT_MALL"],
                    "scope":"SHOP",
                    "scopeShopIds":["546520236057329664"],
                    "effectMemberLevels":[0,1,2,3,4,5,6,7,8],
                    "startTime":"2021-04-15 10:15:00",
                    "endTime":"2021-04-30 10:15:06",
                    "commonStatus":"ENABLE",
                    "limitProductIds":["694667064614473728"],
                    "limitProductCodes":["PD19112500000008"],
                    "redemptionProductIds":[],
                    "redemptionProductCodes":[],
                    "limitType":"DISCOUNT_BY_PRODUCT_AMOUNT",
                    "isStairCut":'false',
                    "stairCount":0,
                    "conditions":[],
                    "userOnceGainLimit":"false",
                    "allowCoupon":"false",
                    "limitAmount":100,
                    "limitQuantity":"",
                    "giftType":"PRODUCT",
                    "coupons":[],
                    "pointGiftType":"BY_QUANTITY",
                    "pointQuantity":"",
                    "pointIncreaseTimes":"",
                    "giftProductIds":["694663830504099840"],
                    "giftProductCodes":["PD19112500000006"],
                    "giftProductQuantity":"1",
                    "limitGiftProductStock":"false",
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