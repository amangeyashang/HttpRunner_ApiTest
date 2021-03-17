# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/9 20:43'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("创建订单")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*["summaryOrderCode"])
    )
    teststeps = [
        Step(
            RunRequest("创建订单-001")
            .with_variables(**{})
            .post("/mallOrder/createOrder")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "consigneeId":71,
                    "paymentType":"WECHAT",
                    "deliverType":"USER_TRANSPORT",
                    "userRemark":"",
                    "productVos":
                        [
                            {
                                "depotCode":"${ENV(vendorCode)}",
                                "productCode":"${ENV(productCode)}",
                                "quantity":1
                            }
                        ],
                    "orderClient":"wechat",
                    "userId":"${ENV(memberId)}",
                    "deportSelectedCouponPromotion":
                        [
                            {
                                "depotCode":"${ENV(vendorCode)}",
                                "selectedCouponId":"864618667424419840",
                                "selectedPromotionId":'null'
                            }
                        ]
                }
            )
            .extract()
            .with_jmespath("body.data.summaryOrderCode","summaryOrderCode")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()