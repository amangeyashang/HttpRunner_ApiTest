# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/16 10:27'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from testcases.vendor.commodityManagement.getSelectCategory_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("Spu添加或修改")
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
            RunRequest("Spu添加或修改-001")
            .with_variables(**{})
            .post("/spuApply/saveOrUpdate")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "id":"",
                    "applyName":"测试2",
                    "applyMobile":"18000000003",
                    "applyVendorCode":"VC10003",
                    "applyMemo":"申请备注",
                    "categoryIdF":"$categoryIdF",
                    "categoryIdS":"$categoryIdS",
                    "categoryId":"$categoryId",
                    "brandId":"",
                    "brandName":"鲜货农业",
                    "name":"白菜",
                    "categoryMsg":"$categoryNameF>$categoryNameS>$categoryName",
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