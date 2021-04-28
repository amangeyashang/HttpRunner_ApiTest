# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/12 14:58'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("获取平台商品分类")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["vendorCode","sellerId","vendorId",])
        ),
        Step(
            RunRequest("获取平台商品分类-001")
            .with_variables(**{})
            .post("/vendorProduct/getSelectCategory")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "page":1,
                    "level":1,
                    "parentCategoryId":"",
                    "isAll":'false',
                    "size":100,
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode"
                }
            )
            .extract()
            .with_jmespath("body.data.content[2].id","categoryIdF")
            .with_jmespath("body.data.content[2].name","categoryNameF")
            .with_jmespath("body.data.content[2].children[1].id","categoryIdS")
            .with_jmespath("body.data.content[2].children[1].name","categoryNameS")
            .with_jmespath("body.data.content[2].children[1].children[5].id","categoryId")
            .with_jmespath("body.data.content[2].children[1].children[5].name","categoryName")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()