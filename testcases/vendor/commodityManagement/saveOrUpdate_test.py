# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/15 16:29'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("新增或修改商铺商品分类")
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
            RunRequest("新增或修改商铺商品分类-001")
            .with_variables(**{})
            .post("/proVendorCategory/saveOrUpdate")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "classifyName":"测试",
                    "seoKeywords":"",
                    "classifySort":1,
                    "isEnable":1,
                    "level":3,
                    "type":["44","45"],
                    "parentId":"45",
                    "classifyIco":"",
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