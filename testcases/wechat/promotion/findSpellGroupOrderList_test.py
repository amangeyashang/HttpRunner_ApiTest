# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 15:31'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("拼团订单列表")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("拼团订单列表-001")
            .with_variables(**{})
            .post("/spellGroup/findSpellGroupOrderList")
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
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .with_json(
                {
                    "vendorCode":"${ENV(vendorCode)}",
                    "productCode":"PD20112000000015"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()