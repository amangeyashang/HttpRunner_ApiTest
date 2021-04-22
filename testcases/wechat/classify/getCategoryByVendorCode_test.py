# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 14:44'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("店铺分类信息")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["depotCode"])
        ),
        Step(
            RunRequest("店铺分类信息-001")
            .with_variables(**{})
            .get("/product/getCategoryByVendorCode")
            .with_params(
                **{
                    "os":"min",
                    "memberId":"${ENV(memberId)}",
                    "lat":"29.71797999388022",
                    "lon":"106.63042999999999",
                    "userToken":"a07a113e2bc043058e10d36382a816a4",
                    "vendorCode":"$depotCode"
                }
            )
            .extract()
            .with_jmespath("body.data[0].children[0].id","categoryId")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()