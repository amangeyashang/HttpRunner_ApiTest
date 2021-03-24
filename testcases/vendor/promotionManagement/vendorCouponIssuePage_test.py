# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/23 19:34'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("商家优惠券发放列表")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("商家优惠券发放列表-001")
            .with_variables(**{})
            .post("/vendorCoupon/couponIssue/vendorCouponIssuePage")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "userMobile":"",
                    "couponTypeEnumStr":"",
                    "page":1,
                    "size":10,
                    "memberId":"${ENV(memberId)}",
                    "userId":"${ENV(memberId)}",
                    "vendorId":"${ENV(vendorId)}",
                    "depotCode":"${ENV(vendorCode)}",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","没有相关数据！")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()