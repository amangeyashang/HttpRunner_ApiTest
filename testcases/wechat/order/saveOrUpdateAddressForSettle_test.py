# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/16 20:01'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("保存或更新地址")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("保存或更新地址-001")
            .with_variables(**{})
            .post("/users/address/new/saveOrUpdateAddressForSettle")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "memberId":"${ENV(memberId)}",
                    "lat":28.45362,
                    "lon":109.006128,
                    "userToken":"684f2aa256a6408980cbb1f56602e250",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .with_json(
                {
                    "id": "71",
                    "consigneeName": "总部员工",
                    "mobile": "18716280028"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()