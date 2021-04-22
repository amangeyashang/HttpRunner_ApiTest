# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 14:47'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from .searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from testcases.wechat.classify.getCategoryByVendorCode_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("搜索结果")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["depotCode","categoryId"])
        ),
        Step(
            RunRequest("搜索结果-001")
            .with_variables(**{})
            .post("/product/searchProduct")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "lat":29.71798,
                    "lon":106.63043,
                    "vendorCode":"$depotCode",
                }
            )
            .with_json(
                {
                    "memberId":"${ENV(memberId)}",
                    "categoryId":"$categoryId",
                    "categoryLv":"2",
                    "couponId":"",
                    "coupon":"",
                    "promotionId":"",
                    "depotProduct":True,
                    "depotCode":"$depotCode",
                    "sort":"DEFAULT_SORT",
                    "page":-2,
                    "searchType":"PRODUCT",
                    "type":0
                }
            )
            .extract()
            .with_jmespath("body.data.content[0].item[0].productCode","productCode")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()