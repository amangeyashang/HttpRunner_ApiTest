# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 14:33'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("我的优惠券")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("我的优惠券-未使用-001")
            .with_variables(**{})
            .post("/vendor/userCouponPage")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "memberId":"${ENV(memberId)}",
                    "vendorCode":"${ENV(vendorCode)}",
                }
            )
            .with_json(
                {
                    "couponState": "UNUSED",
                    "page": 1,
                    "size": 10
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        ),
        Step(
            RunRequest("我的优惠券-已使用-002")
            .with_variables(**{})
            .post("/vendor/userCouponPage")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "memberId":"${ENV(memberId)}",
                    "vendorCode":"${ENV(vendorCode)}",
                }
            )
            .with_json(
            {
                "couponState": "USED",
                "page": 1,
                "size": 10
            }
        )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        ),
        Step(
            RunRequest("我的优惠券-已过期-003")
            .with_variables(**{})
            .post("/vendor/userCouponPage")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "memberId":"${ENV(memberId)}",
                    "vendorCode":"${ENV(vendorCode)}",
                }
            )
            .with_json(
                {
                    "couponState": "EXPIRED",
                    "page": 1,
                    "size": 10
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()