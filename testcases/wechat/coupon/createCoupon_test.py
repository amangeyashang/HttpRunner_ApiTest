# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/9 17:37'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from .couponCenter_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("根据商品查优惠券")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["couponTypeId"])
        ),
        Step(
            RunRequest("根据商品查优惠券-001")
            .with_variables(**{})
            .post("/vendor/createCoupon")
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
                    "lat":"29.71797999388022",
                    "lon":"106.63042999999999",
                    "userToken":"c857660825954391ab036eed074861ad",
                }
            )
            .with_json(
                {
                    "quantity":1,
                    "couponTypeId":"$couponTypeId"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()