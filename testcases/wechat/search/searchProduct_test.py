# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 14:47'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("搜索结果")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
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
                .with_json(
                {
                    "memberId":"${ENV(memberId)}",
                    "categoryId":"199",
                    "categoryLv":"2",
                    "couponId":"",
                    "coupon":"",
                    "promotionId":"",
                    "promotionType":'null',
                    "depotProduct":True,
                    "depotCode":"${ENV(vendorCode)}",
                    "sort":"DEFAULT_SORT",
                    "page":-2,
                    "searchType":"PRODUCT",
                    "type":0
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()