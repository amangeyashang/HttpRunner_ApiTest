# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/16 11:25'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.userControl.getMemberId_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from testcases.vendor.commodityManagement.getSelectCategory_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("Sku添加或修改")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["vendorCode","sellerId","vendorId","categoryIdF","categoryIdS","categoryId","categoryNameF","categoryNameS","categoryName"])
        ),
        Step(
            RunRequest("Sku添加或修改-001")
            .with_variables(**{})
            .post("/skuApply/saveOrUpdate")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "id":'null',
                    "applyName":"测试2",
                    "applyMobile":"18000000003",
                    "applyVendorCode":"VC10003",
                    "applyMemo":"",
                    "name":"同步商品1",
                    "spuCode":"SPU21041200000001",
                    "barCode":"13216546",
                    "specs":"[]",
                    "skuName":"",
                    "unit":"",
                    "logo":"http://wkhgs.oss-cn-hangzhou.aliyuncs.com/bd8910bc-1abc-4bf6-9b58-edd637913a94",
                    "images":[],
                    "introImages":[],
                    "videoImage":"",
                    "video":"",
                    "categoryMsg":"$categoryNameF>$categoryNameS>$categoryName",
                    "categoryIdF":"$categoryIdF",
                    "categoryIdS":"$categoryIdS",
                    "categoryId":"$categoryId",
                    "brandId":875232364626718700,
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.message","申请成功")
            .assert_equal("body.status","S")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()