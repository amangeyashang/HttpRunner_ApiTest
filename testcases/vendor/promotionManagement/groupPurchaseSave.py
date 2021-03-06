# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/15 15:17'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("新增拼团")
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
            RunRequest("新增拼团-001")
            .with_variables(**{})
            .post("/vendor/groupPurchase/save")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "name":"新增拼团测试1",
                    "description":"",
                    "channels":["WECHAT_MALL"],
                    "scope":"SHOP",
                    "scopeShopIds":["546520236057329664"],
                    "effectMemberLevels":[0,1,2,3,4,5,6,7,8],
                    "startTime":"2021-04-15 15:16:13",
                    "endTime":"2021-04-30 15:16:15",
                    "commonStatus":"ENABLE",
                    "groupSize":"2",
                    "groupDiscount":"1",
                    "limitedQuantity":"1",
                    "entries":'true',
                    "products":
                        [
                            {
                                "productCode":"PD19112500000008",
                                "barCode":"19112500000008",
                                "productId":"694667064614473728",
                                "productName":"新鲜红肉小蜜柚2-2.5斤 当季现摘平和鲜柚 带箱新鲜水果红肉柚子",
                                "activeInventory":"10",
                                "groupPurchasePrice":100
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
            .assert_equal("body.msg","success")
            .assert_equal("body.data.message","添加成功")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()