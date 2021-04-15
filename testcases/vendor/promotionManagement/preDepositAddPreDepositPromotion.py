# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/15 15:50'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.userControl.getMemberId_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from .preDepositPageQueryPreDepositPromotion_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("充值赠送详情")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
                .call(RequestWithFunctions)
                .export(*["vendorCode","sellerId","vendorId","preDepositId"])
        ),
        Step(
            RunRequest("充值赠送详情-001")
            .with_variables(**{})
            .post("/vendor/preDeposit/addPreDepositPromotion")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "name":"充值赠送",
                    "description":"阿瑟打算多阿萨德按时",
                    "channels":["WECHAT_MALL"],
                    "scope":"SHOP",
                    "scopeShopIds":["546520236057329664"],
                    "effectMemberLevels":"0,1,2,3,4,5,6,7,8",
                    "startTime":"2021-04-15 15:49:52",
                    "endTime":"2021-04-30 15:49:54",
                    "status":"ENABLE",
                    "commonType":"COMMODITY",
                    "phaseType":"DAY",
                    "depositAmount":10000,
                    "phaseTotal":"1",
                    "productInfoList":
                        [
                            {
                                "categoryName":"蛋类",
                                "barCode":"131997",
                                "productCode":"PD20121800000001",
                                "productId":"835629025920565248",
                                "productName":"鲜鸡蛋   约500g/份",
                                "purchaseQuantityLimit":"",
                                "specialOfferPrice":"",
                                "logo":"9b9ee986-21e5-4786-90aa-193d3210cb51"
                            }
                        ],
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode"
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