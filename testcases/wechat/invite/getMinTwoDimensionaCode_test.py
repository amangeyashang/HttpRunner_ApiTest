# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/10 17:54'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("获取带参小程序二维码")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("获取带参小程序二维码-001")
            .with_variables(**{})
            .get("/weChat/getMinTwoDimensionaCode")
            .with_params(
                **{
                    "os":"min",
                    "memberId":"${ENV(memberId)}",
                    "lat":29.71797999388022,
                    "lon":106.63042999999999,
                    "userToken":"92b792df1b304a8d937d8119a4e50f3f",
                    "vendorCode":"${ENV(vendorCode)}",
                    "minPath":"18716280028,VC10003,U"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
            .assert_equal("body.status","S")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()