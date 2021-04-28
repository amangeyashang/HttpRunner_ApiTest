# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/15 11:37'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("新增满减促销")
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
            RunRequest("新增满减促销-001")
            .with_variables(**{})
            .post("/vendor/fullRedution/save")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "name":"满减促销测试1",
                    "description":"",
                    "channels":["WECHAT_MALL"],
                    "scope":"SHOP",
                    "scopeShopIds":["546520236057329664"],
                    "effectMemberLevels":[0,1,2,3,4,5,6,7,8],
                    "startTime":"2021-04-15 11:36:57",
                    "endTime":"2021-04-30 11:36:59",
                    "commonStatus":"ENABLE",
                    "products":[],
                    "limitProductIds":["694667064614473728"],
                    "limitProductCodes":["PD19112500000008"],
                    "allowCoupon":"false",
                    "fullRedutionRates":[{"full":100,"redution":90}],
                    "isStairCut":'false',
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode"
                }
            )
            .extract()
            .with_jmespath("body.data.content[0].id","fullRedutionId")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
            .assert_equal("body.data.message","添加成功")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()