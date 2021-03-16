# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/9 16:34'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("预支付")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("预支付-001")
            .with_variables(**{})
            .post("/cart/buildSettle")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "os":"min",
                    "memberId":"${ENV(memberId)}",
                    "lat":28.45362,
                    "lon":109.006128,
                    "userToken":"684f2aa256a6408980cbb1f56602e250",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .with_json(
                {
                    "paymentType":"WECHAT",
                    "productVos":
                        [
                            {
                                "depotCode":"${ENV(vendorCode)}",
                                "productCode":"${ENV(productCode)}",
                                "quantity":1
                            }
                        ],
                    "orderClient":"wechat",
                    "userId":"${ENV(memberId)}"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()